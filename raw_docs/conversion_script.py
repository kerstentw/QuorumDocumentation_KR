#!/usr/bin/env python
"""
Convert a word (doc/docx) file to markdown

Requires a copy of LibreOffice to be installed.
"""
import sys
import os
import subprocess

MD_TYPE = "gfm"
SOFFICE = r'/Applications/LibreOffice.app/Contents/MacOS/soffice'
PANDOC = r'pandoc'

SOURCES = "./docs"
SOURCE_FORMATTER= SOURCES + "/{file_name}"
TARGET = "./md/{file_name}"

def convertToMD(infile, outfile):
    """Convert the given infile to the given outfile in markdown format, via
    LibreOffice and Pandoc"""
    root, __ = os.path.splitext(infile)
    htmlfile = root.split("/")[-1] + ".html"
    subprocess.call([SOFFICE, '--invisible', '--convert-to',
                     'html', infile])
    subprocess.call([PANDOC, '-f', 'html', '-t', MD_TYPE, '-o', outfile,
                     htmlfile])
    os.remove(htmlfile)


def main(argv=None):
    abs_file_list = [(SOURCE_FORMATTER.format(file_name = fil), TARGET.format(file_name = fil).replace(".docx",".md")) for fil in os.listdir(SOURCES)]

    for filgroup in abs_file_list:
        convertToMD(*filgroup)



if __name__ == "__main__":
    sys.exit(main())
