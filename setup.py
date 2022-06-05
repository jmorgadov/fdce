import numpy as np
from setuptools import Extension, find_packages, setup

setup(
    name="fdce",
    version="0.1.1a3",
    description="Finite difference coefficient estimator",
    long_description="",
    author="Jorge Morgado Vega",
    author_email="jorge.morgadov@gmail.com",
    requires=["numpy"],
    packages=find_packages(),
    python_requires=">=3.8",
    ext_modules=[
        Extension(
            "fdce._extension._fdce",
            ["fdce/_extension/_fdce.c"],
            include_dirs=[np.get_include()],
        )
    ]
)
