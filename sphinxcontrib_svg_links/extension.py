from sphinxcontrib_svg_links.directives import ImageSVG
from docutils import nodes

from sphinxcontrib_svg_links.writer import visit_image_html, depart_image_html


def setup(app):

    app.add_directive("image-svg", ImageSVG)

    # override only the html writer visit methods for image-svg
    # to react on the svglinks option
    app.add_node(
        nodes.image,
        override=True,
        html=(visit_image_html, depart_image_html),
    )

    #
    # app.connect("builder-inited", run_autoapi)
    # app.connect("source-read", source_read)
    # # Use a lower priority than the default to ensure that we can
    # # inject into the toctree before Sphinx tries to use it
    # # in another doctree-read transformer.
    # app.connect("doctree-read", doctree_read, priority=400)
    # app.connect("build-finished", build_finished)
    # if "viewcode-find-source" in app.events.events:
    #     app.connect("viewcode-find-source", viewcode_find)
    # if "viewcode-follow-imported" in app.events.events:
    #     app.connect("viewcode-follow-imported", viewcode_follow_imported)
    # app.add_config_value("autoapi_root", API_ROOT, "html")
    # app.add_config_value("autoapi_ignore", [], "html")
    # app.add_config_value("autoapi_options", _DEFAULT_OPTIONS, "html")
    # app.add_config_value("autoapi_member_order", "bysource", "html")
    # app.add_config_value("autoapi_file_patterns", None, "html")
    # app.add_config_value("autoapi_dirs", [], "html")
    # app.add_config_value("autoapi_keep_files", False, "html")
    # app.add_config_value("autoapi_add_toctree_entry", True, "html")
    # app.add_config_value("autoapi_template_dir", None, "html")
    # app.add_config_value("autoapi_include_summaries", None, "html")
    # app.add_config_value("autoapi_python_use_implicit_namespaces", False, "html")
    # app.add_config_value("autoapi_python_class_content", "class", "html")
    # app.add_config_value("autoapi_generate_api_docs", True, "html")
    # app.add_config_value("autoapi_prepare_jinja_env", None, "html")
    # app.add_autodocumenter(documenters.AutoapiFunctionDocumenter)
    # app.add_autodocumenter(documenters.AutoapiPropertyDocumenter)
    # app.add_autodocumenter(documenters.AutoapiDecoratorDocumenter)
    # app.add_autodocumenter(documenters.AutoapiClassDocumenter)
    # app.add_autodocumenter(documenters.AutoapiMethodDocumenter)
    # app.add_autodocumenter(documenters.AutoapiDataDocumenter)
    # app.add_autodocumenter(documenters.AutoapiAttributeDocumenter)
    # app.add_autodocumenter(documenters.AutoapiModuleDocumenter)
    # app.add_autodocumenter(documenters.AutoapiExceptionDocumenter)
    # directives.register_directive("autoapi-nested-parse", NestedParse)
    # directives.register_directive("autoapisummary", AutoapiSummary)
    # app.setup_extension("sphinx.ext.autosummary")
    # app.add_event("autoapi-skip-member")
    # app.setup_extension("sphinx.ext.inheritance_diagram")
    # app.add_directive("autoapi-inheritance-diagram", AutoapiInheritanceDiagram)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }