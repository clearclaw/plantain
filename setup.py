from setuptools import setup, find_packages
import pyver

__version__, __version_info__ = pyver.get_version (pkg = "banana")

setup (name = 'banana',
  version = __version__,
  description = "Command line tool for managing Mandrill templates.",
  long_description = "Command line tool for managing Mandrill templates.",
  classifiers = [],
  keywords = "",
  author = "J C Lawrence",
  author_email = "jcl@kanga.nu",
  url = "http://matterport.com/",
  license = "Proprietary",
  packages = find_packages (exclude = ["tests",]),
  include_package_data = True,
  zip_safe = False,
  install_requires = [
    "boto",
    "mppy",
    "path.py",
    "requests",
  ],
  entry_points = {
    "console_scripts": [
      "banana = banana.main:main",
      ],
    },
  )
