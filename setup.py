from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="densenet-api",
    version="0.1",
    author="tv3141",
    author_email="tv3141@users.noreply.github.com",
    description="DenseNet API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tv3141/densenet_api",
    packages=find_packages(),
    install_requires=[],
    tests_require=[],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    entry_points={
        'console_scripts': [
            'densenet_api = app.main:run_app',
        ]
    }
)