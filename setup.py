from setuptools import setup, find_packages
 
setup(
    name = 'discord_publisher',
    version = '0.1',
    description = 'for explain about pypi deploy',
    author = 'Happytree Samsung',
    author_email = 'samsunghappytree123@naver.com',
    url = 'https://github.com/samsunghappytree123/discord-publisher',
    install_requires =  ['aiohttp', 'asyncio'],
    packages = find_packages(exclude = []),
    keywords = ['discord', 'discord.py', 'discord_publisher', 'discord-publisher'],
    python_requires = '>=3',
    package_data = {},
    zip_safe = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)