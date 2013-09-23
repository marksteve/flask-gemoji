import os
from setuptools import setup

readme_path = os.path.join(os.path.dirname(
  os.path.abspath(__file__)),
  'README.md',
)
long_description = open(readme_path).read()

setup(
  name='flask-gemoji',
  version='0.1.2',
  packages=['flask_gemoji'],
  author="Mark Steve Samson",
  author_email='hello@marksteve.com',
  description="Add gemojis to your Flask apps",
  long_description=long_description,
  url='https://github.com/marksteve/flask-gemoji',
  include_package_data=True,
  zip_safe=False,
)
