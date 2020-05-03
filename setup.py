from setuptools import find_packages
from distutils.core import setup, Command
from distutils.command.build import build
import subprocess
import os, sys
import os.path


__HERE__ = os.path.abspath(os.path.dirname(__file__))
__VERSION__ = "1.5.0rc3"


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

    def run(self):
        if sys.platform == 'win32':
            fname = "build.bat"
        else:
            fname = "build.sh"
        subprocess.run([os.path.join(__HERE__, fname)])


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
    name = "arc1docs",
    version = __VERSION__,
    description = "Documentation for ArC1",
    url = "https://github.com/arc-instruments/arc1-docs",
    license = 'GPL3',
    packages = packages,
    python_requires = '>=3.6',
    install_requires = requirements,
    package_data = {
        'arc1docs': ['manual.pdf']
    },
    cmdclass = cmdclass
)
