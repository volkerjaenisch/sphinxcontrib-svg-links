
from docutils.parsers.rst.directives.images import Image


class ImageSVG(Image):

    def __init__(self, name, arguments, options, content, lineno,
                 content_offset, block_text, state, state_machine):
        options['SVGLinks'] = True
        super().__init__(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
