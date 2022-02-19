from setuptools import setup

setup(
    name = 'error-handler',
    packages = ['handler'],
    version = '1',
    description = 'Error handler with Telegram alerts',
    url = 'https://github.com/xjxckk/error-handler/',
    download_url = 'https://github.com/xjxckk/error-handler/archive/refs/tags/v1.tar.gz',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)