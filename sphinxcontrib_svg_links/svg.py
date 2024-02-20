import xml.etree.ElementTree as ET
from pathlib import Path

SVGLINKS_PREFIX = "svglink://"

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')

def patch_svg(node, writer):
    """
    SVG elements should link to sphinx content. This is done by clueing speudo URIs to
    the SVG elements.

        <a xlink:href="svglink://#other-reference-label">
            <ellipse cx="235" cy="220" rx="40" ry="40" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)"
                     pointer-events="all"/>
        </a>

    In this example the ellipse links to the speudo URI "svglink://#other-reference-label" which represents
    the target label "#other-reference-label". The target "#other-reference-label" should
    be defined elsewhere e.g. it may link to a chapter_

    .. _other-reference-label:

    This is a chapter
    -----------------

    Each speudo URI has to start with "svglink://".
    THe linking can be done comfortably by using draw.io or inkscape or any other capable SVG editor.

    This routine patches the SVG file so that the speudo URIs are replaced by the
    correct relative URIs to the target referenced.

    :param node: The current node that is rendered
    :param writer: The writer to which renders the node
    :return: the relative path to the patched SVG file
    """

    # Get the SVG file path
    # The current base dir is the parent of the current file
    current_doc_dir = Path(writer.builder.current_docname).parent
    # and the original_uri attribute of the node gives aus the relative SVG file path
    svg_file_path = current_doc_dir / Path(node.attributes['original_uri'])

    # Parse the SVG file
    with open(svg_file_path, "rb") as f:
        etree = ET.parse(f)

    root = etree.getroot()

    # Iterate over all hrefs in the SVG file
    for child in root.findall(".//*[@xlink:href]"):
        # Get the speudo URI
        speudo_URI = child.attrib['xlink:href']
        if not speudo_URI.startswith(SVGLINKS_PREFIX):
            continue
        # cut the reference part from the speudo URI
        reference = speudo_URI[len(SVGLINKS_PREFIX):]
        # Strip '#' to get the reference label
        if reference.startswith('#'):
            reference = reference[1:]
        # lookup the reference via the labels dict
        labels = writer.builder.env.domains['std'].labels
        if reference in labels:
            ref_tupel = labels[reference]
            # local link or link to file in same directory
            if len(ref_tupel) == 3:
                new_reference = ref_tupel[0] + '.html' + '#' + ref_tupel[1]
            else:
                # Link to file in other directory needs a path
                new_reference = '/'.join(ref_tupel[:-3]) + ref_tupel[-3] + '.html' + '#' + ref_tupel[-2]
            # Replace the link to the speudo URI with the new reference
            child.attrib['xlink:href'] = '../' + new_reference
            # Tell the browser to measure the relative paths from the parent of the embedded SVG object.
            child.attrib['target'] = '_parent'
        else:
            # ToDo Error handling if reference can not be found
            pass
    # Determine the new location in the filesystem for the patched SVG file in the "build" dir.
    # ToDo: Catch file name collisions [SVG image is embedded twice], better naming convention
    new_svg_file_path = Path(writer.builder.outdir) / writer.builder.imagedir / (node.attributes['original_uri'] + '.1.svg')

    # Write the SVG file
    with open(new_svg_file_path, "wb") as f:
        etree.write(f)

    # Return the relative URI for the SVG <object> to find its data
    return Path(writer.builder.imgpath) / Path(node.attributes['original_uri'] + '.1.svg').name