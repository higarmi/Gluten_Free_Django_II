# -*- coding: utf-8 -*-
"""
    ticket role
    ~~~~~~~~~~~

    An interpreted text role to link docs to lighthouse issues.

    :copyright: Copyright 2013 by Daniele Varrazzo.
"""

from docutils import nodes, utils
from docutils.parsers.rst import roles

def ticket_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    try:
        num = int(text.replace('#', ''))
    except ValueError:
        msg = inliner.reporter.error(
            "ticket number must be... a number, got '%s'" % text)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    url_pattern = inliner.document.settings.env.app.config.ticket_url
    if url_pattern is None:
        msg = inliner.reporter.warning(
            "ticket not configured: please configure ticket_url in conf.py")
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    url = url_pattern % num
    roles.set_classes(options)
    node = nodes.reference(rawtext, 'ticket ' + utils.unescape(text),
            refuri=url, **options)
    return [node], []

def setup(app):
    app.add_config_value('ticket_url', None, 'env')
    app.add_role('ticket', ticket_role)

