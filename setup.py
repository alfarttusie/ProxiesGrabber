from setuptools import setup, find_packages

setup(
    name="ProxiesGrabber",
    version="1.0.6",
    author="alfarttusie",
    author_email=" muhammed@alfarttusie.com",
    description="A Python package for scraping free proxy lists from various online sources.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alfarttusie/ProxiesGrabber",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
