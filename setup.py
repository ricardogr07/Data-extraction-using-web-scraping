from setuptools import setup, find_packages

setup(
    name='LinkedInWebscraper',
    version='0.1',
    packages=find_packages(where='src'),  # Specify that the code is in the src/ directory
    package_dir={'': 'src'},  # Tell setuptools that packages are under the src/ directory
    install_requires=[
        # Add any dependencies you want to install along with your project here, like:
        # 'requests',
        # 'pandas',
    ],
)
