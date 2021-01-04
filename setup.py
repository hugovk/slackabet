from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


def local_scheme(version):
    """Skip the local version (eg. +xyz of 0.6.1.dev4+gdf99fe2)
    to be able to upload to Test PyPI"""
    return ""


setup(
    name="slackabet",
    description="Convert text into Slack alphabet emoji",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hugo van Kemenade",
    url="https://github.com/hugovk/slackabet",
    license="MIT",
    keywords=[
        "CLI",
        "converter",
        "convert",
        "text",
        "Slack",
        "alphabet",
        "emoji",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["slackabet = slackabet.cli:main"]},
    zip_safe=True,
    use_scm_version={"local_scheme": local_scheme},
    setup_requires=["setuptools_scm"],
    install_requires=['pyperclip; platform_system != "Linux"'],
    extras_require={"tests": ["hypothesis-auto", "pytest", "pytest-cov"]},
    python_requires=">=3.6",
    project_urls={
        "Source": "https://github.com/hugovk/slackabet",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Artistic Software",
        "Topic :: Text Processing",
    ],
)
