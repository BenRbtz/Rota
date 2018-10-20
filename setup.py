from setuptools import setup, find_packages

setup(
    name="rota",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires=">=3.6",
    install_requires=['XlsxWriter>=1.1'],
    tests_require=['pytest']
)
