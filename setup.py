#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
from genius_chatbot.version import __version__, __author__
from pathlib import Path
import os
import re
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements

readme = Path('README.md').read_text()
version = __version__
requirements = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'),
                                       session=PipSession())
requirements_api = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements_api.txt'),
                                       session=PipSession())
requirements_rag = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements_rag.txt'),
                                       session=PipSession())
requirements_lmm = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements_lmm.txt'),
                                       session=PipSession())
requirements_memgpt = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements_memgpt.txt'),
                                         session=PipSession())
requirements_pgvector = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements_pgvector.txt'),
                                         session=PipSession())
requirements_chromadb = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements_chromadb.txt'),
                                         session=PipSession())
readme = re.sub(r"Version: [0-9]*\.[0-9]*\.[0-9][0-9]*", f"Version: {version}", readme)
with open("README.md", "w") as readme_file:
    readme_file.write(readme)
description = 'Create various chat agents based off YAML or JSON files of predefined configs'

setup(
    name='genius-agent',
    version=f"{version}",
    description=description,
    long_description=f'{readme}',
    long_description_content_type='text/markdown',
    url='https://github.com/Knuckles-Team/genius-agent',
    author=__author__,
    author_email='knucklessg1@gmail.com',
    maintainer=__author__,
    maintainer_email='knucklessg1@gmail.com',
    license='MIT',
    packages=['genius_agent'],
    include_package_data=True,
    install_requires=[str(requirement.requirement) for requirement in requirements],
    extras_require={
        'rag': [str(requirement.requirement) for requirement in requirements_rag],
        'chromadb': [str(requirement.requirement) for requirement in requirements_chromadb],
        'pgvector': [str(requirement.requirement) for requirement in requirements_pgvector],
        'api': [str(requirement.requirement) for requirement in requirements_api],
        'memgpt': [str(requirement.requirement) for requirement in requirements_memgpt],
    },
    py_modules=['genius_agent'],
    package_data={'genius_agent': ['genius_agent']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: Public Domain',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    entry_points={'console_scripts': ['genius-agent = genius_agent.genius_agent:main']},
)
