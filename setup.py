from setuptools import setup, find_packages
import pyver

__version__, __version_info__ = pyver.get_version (pkg = "plantain",
                                                   public = True)

setup (
    name = 'plantain',
    version = __version__,
    description = "Command line tool for managing Mandrill templates.",
    long_description = file ("README.rst").read (),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        + "GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Utilities",
    ],
    keywords = "Mandrill templates commandline API",
    author = "J C Lawrence",
    author_email = "claw@kanga.nu",
    url = "https://github.com/clearclaw/plantain",
    license = "Proprietary",
    packages = find_packages (exclude = ["tests",]),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        "logtool",
        "mandrill",
        "configobj",
        "path.py",
        "pyver",
    ],
    entry_points = {
        "console_scripts": [
        "banana = banana.main:main",
        "plantain = plantain.main:main",
        ],
    },
)
