# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from setuptools import setup, find_packages
from io import open  # io.open needed for Python 2 compat
import re

# azure v0.x is not compatible with this package
# azure v0.x used to have a __version__ attribute (newer versions don't)
try:
    import azure

    try:
        ver = azure.__version__
        raise Exception(
            "This package is incompatible with azure=={}. ".format(ver)
            + 'Uninstall it with "pip uninstall azure".'
        )
    except AttributeError:
        pass
except ImportError:
    pass


with open("README.md", "r") as fh:
    _long_description = fh.read()

filename = "src/azure/iot/hub/constant.py"
version = None

with open(filename, "r") as fh:
    if not re.search("\n+VERSION", fh.read()):
        raise ValueError("VERSION  is not defined in constants.")

with open(filename, "r") as fh:
    for line in fh:
        if re.search("^VERSION", line):
            constant, value = line.strip().split("=")
            if not value:
                raise ValueError("Value for VERSION not defined in constants.")
            else:
                # Strip whitespace and quotation marks
                # Need to str convert for python 2 unicode
                version = str(value.strip(' "'))
            break

setup(
    name="azure-iot-hub",
    version=version,
    description="Microsoft Azure IoTHub Service Library",
    license="MIT License",
    license_files=("LICENSE",),
    url="https://github.com/Azure/azure-iot-hub-python/",
    author="Microsoft Corporation",
    author_email="opensource@microsoft.com",
    long_description=_long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[
        "msrest>=0.6.21,<1.0.0",
        # NOTE: Python 2.7, 3.5 support dropped >= 1.4.0
        "uamqp>=1.2.14,<2.0.0",
        "azure-core>=1.10.0,<2.0.0",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3*, <4",
    packages=find_packages(
        where="src",
        exclude=[
            # Exclude packages that will be covered by PEP420 or nspkg
            "azure",
            "azure.iot",
        ]
    ),
    package_dir={"": "src"},
    zip_safe=False,
)
