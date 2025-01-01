import os.path as osp
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize

def readme():
    with open('README.md') as f:
        return f.read()

def get_requirements(filename='requirements.txt'):
    here = osp.dirname(osp.realpath(__file__))
    with open(osp.join(here, filename), 'r') as f:
        return [line.strip() for line in f.readlines()]

def build_ext_modules():
    # ここで初めて numpy を import する
    import numpy as np

    def numpy_include():
        try:
            return np.get_include()
        except AttributeError:
            return np.get_numpy_include()

    ext_modules = [
        Extension(
            'prtreid.metrics.rank_cylib.rank_cy',
            ['prtreid/metrics/rank_cylib/rank_cy.pyx'],
            include_dirs=[numpy_include()],
        )
    ]
    # 必要ならオプションを追加
    return cythonize(ext_modules)

setup(
    name="prtreid",
    version="0.0.1",
    description="A library for deep learning person re-ID in PyTorch",
    license="MIT",
    long_description=readme(),
    packages=find_packages(),
    install_requires=get_requirements(),
    extras_require={"labels": get_requirements("requirements_labels.txt")},
    keywords=["Person Re-Identification", "Deep Learning", "Computer Vision"],
    # ext_modules をビルド時に初めて呼ぶ
    ext_modules=build_ext_modules()
)
