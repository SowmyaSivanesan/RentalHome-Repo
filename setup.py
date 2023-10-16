from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rental_home_management/__init__.py
from rental_home_management import __version__ as version

setup(
	name="rental_home_management",
	version=version,
	description="web application ",
	author="Sowmiya",
	author_email="sowmiya@aerele.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
