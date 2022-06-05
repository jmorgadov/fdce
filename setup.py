from setuptools import Extension, setup, find_packages

setup(
    name="fdce",
    version="0.1.1a3",
    description="Finite difference coefficient estimator",
    author="Jorge Morgado Vega",
    author_email="jorge.morgadov@gmail.com",
    requires=["numpy"],
    packages=find_packages(),
    python_requires=">=3.8",
    ext_modules=[
        Extension("fdce._extension._fdce", ["fdce/_extension/_fdce.c"]),
    ]
)
