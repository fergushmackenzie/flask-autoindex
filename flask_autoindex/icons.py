# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .entry import File, Default


by_extension = [
    ('<i class="large file code outline icon"></i>', ['py', 'pyc', 'php', 'c', 'cpp', 'h']),
    ('<i class="large file text icon">', ['md', 'markdown', 'rst', 'rtf']),
    ('<i class="large html5 icon"></i>', ['html', 'htm', 'cgi']),
    ('<i class="large file code outline icon"></i>', ['asp', 'vb']),
    ('<i class="large file code outline icon"></i>', 'rb'),
    ('<i class="large html5 icon"></i>', 'xhtml'),
    ('<i class="large css3 icon"></i>', ['css', 'less']),
    ('<i class="large database icon"></i>', ['db', 'sqlite', 'sqlite3', 'sql']),
    ('<i class="large settings icon">', ['conf', 'cfg', 'ini', 'reg', 'sys']),
    ('<i class="large file archive outline icon"></i>', ['zip', 'tar', 'gz', 'tgz', '7z', 'alz', 'rar', \
                            'bin', 'cab']),
    ('<i class="large file archive outline icon"></i>', 'jar'),
    ('<i class="large coffee icon"></i>', ['java', 'jsp']),
    ('<i class="large terminal icon"></i>', 'sh'),
    ('<i class="large file pdf outline icon"></i>', 'pdf'),
    ('<i class="large rss icon"></i>', 'rss'),
    ('<i class="large circle icon"></i>', ['iso', 'vcd', 'toast']),
    ('<i class="large file powerpoint outline icon"></i>', ['ppt', 'pptx']),
    ('<i class="large file excel outline icon"></i>', ['xls', 'xlsx', 'csv']),
    ('<i class="large file word outline icon"></i>', ['doc', 'docx']),
    ('<i class="large setting icon"></i>', ['bat', 'com']),
    ('<i class="large image icon"></i>', 'ics'),
    ('<i class="large file text icon"></i>', Default)
]
by_filename = [
    ('<i class="large file text icon"></i', ['Makefile', 'Rakefile'])
]
by_mimetype = [
    ('<i class="large file text icon"></i>', 'text/*'),
    ('<i class="large image icon"></i>', 'image/*'),
    ('<i class="large file audio outline icon"></i>', 'audio/*'),
    ('<i class="large file video outline icon"></i>', 'video/*')
]


def to_list(val):
    if not isinstance(val, list):
        return [val]
    else:
        return val


for icon, exts in by_extension:
    for ext in to_list(exts):
        File.add_icon_rule_by_ext(icon, ext)
for icon, filenames in by_filename:
    for name in to_list(filenames):
        File.add_icon_rule_by_name(icon, name)
for icon, mimetypes in by_mimetype:
    for mimetype in to_list(mimetypes):
        File.add_icon_rule_by_mimetype(icon, mimetype)
