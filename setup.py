from setuptools import setup, find_packages

setup(
    name="magicMahler",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy",
        "tqdm",
        "imageio"
    ],
    description="A Python package for working with polytopes, polar bodies, and Mahler volumes.",
    author="Vlassis Mastrantonis",
    author_email="vmastr@umd.edu",
    url="https://github.com/vmastr/magicMahler",
)
