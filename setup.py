from setuptools import find_packages
from distutils.core import setup, Command
from distutils.command.build import build
import shutil
import subprocess
import os, sys
import os.path


__HERE__ = os.path.abspath(os.path.dirname(__file__))

__NAME__ = "arc1docs"
__DESC__ = "Documentation for ArC1",
__VERSION__ = "2.0.0"
__MAINTAINER__ = "Spyros Stathopoulos"
__EMAIL__ = "devel@arc-instruments.co.uk"
__URL__ = "http://www.arc-instruments.co.uk/products/arc-one/"

with open(os.path.join(__HERE__, "README.md"), encoding='utf-8') as readme:
    __LONG_DESC__ = readme.read()


requirements = [
    "importlib-resources>=1.1.0; python_version < '3.7'",
]


class BuildDocs(Command):

    description = "Generate the manual"
    user_options = []

    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def compile_docs(self):
        if sys.platform == 'win32':
            pandoc = shutil.which('pandoc.exe')
        else:
            pandoc = shutil.which('pandoc')
        subprocess.run([pandoc, 'manual.txt', '--number-sections', \
            '--template=template.html5', '--css=manual.css',\
            '--pdf-engine=weasyprint', '-o', \
            os.path.join('arc1docs','manual.pdf')])

    def run(self):
        self.compile_docs()


class Build(build):

    user_options = build.user_options + []

    def run(self):
        self.run_command("build_docs")
        super().run()


cmdclass = {}
cmdclass['build_docs'] = BuildDocs
cmdclass['build'] = Build

packages = find_packages(include=["arc1docs"])

setup(
    name = __NAME__,
    version = __VERSION__,
    description = "Documentation for ArC1",
    long_description = __LONG_DESC__,
    long_description_content_type = 'text/markdown',
    author = __MAINTAINER__,
    author_email = __EMAIL__,
    url = __URL__,
    project_urls = {
        "Source Code": "https://github.com/arc-instruments/arc1-docs"
    },
    license = 'GPL3',
    platforms = ['any'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages = packages,
    python_requires = '>=3.3',
    install_requires = requirements,
    package_data = {
        'arc1docs': ['manual.pdf']
    },
    cmdclass = cmdclass
)
