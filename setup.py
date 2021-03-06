import os
import glob

from setuptools import setup, find_packages

SETUP_PTH = os.path.dirname(os.path.abspath(__file__))

def readme():
    with open('README.md') as f: # Set GitHub repo README as package README
        return f.read()

setup(
        name="DefectsWithTheBoys",
        packages=find_packages(),
        version="0.0.1",
        install_requires=["numpy>=1.18.1", "pymatgen>=2020.1.28", "matplotlib>=3.1""monty>=3.0.2"],
        # That I know of...
        package_data={"DefectsWithTheBoys.pycdt.utils": ["*.yaml"]},
        # Standard PyCDT settings, will probably delete soon
        author="Seán Kavanagh",
        author_email="sean.kavanagh.19@ucl.ac.uk",
        maintainer="Seán Kavanagh",
        maintainer_email="sean.kavanagh.19@ucl.ac.uk",
        url="http://github.com/kavanase/DefectsWithTheBoys",
        description="Collection of Python modules & functions to perform "
                    "and process solid-state defect calculations",
        long_description=readme(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Development Status :: 2 - Release",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Scientific/Engineering :: Physics",
            "Topic :: Scientific/Engineering :: Chemistry",
            "Topic :: Software Development :: Libraries :: Python Modules"
            ],
        license="MIT",
        scripts=glob.glob(os.path.join(SETUP_PTH, "scripts", "*")),
        test_suite="nose.collector",
        tests_require=["nose"]
)
