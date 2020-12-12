from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'discord_publisher',
    version = '1.0.1',
    description = 'Discord 공지 채널에 메세지를 발신해보세요!',
    author = 'Happytree Samsung',
    author_email = 'samsunghappytree123@naver.com',
    url = 'https://github.com/samsunghappytree123/discord-publisher',
    project_urls={
        "Homepage": "https://github.com/samsunghappytree123/discord-publisher",
        "Source":"https://github.com/samsunghappytree123/discord-publisher",
        "Tracker":"https://github.com/samsunghappytree123/discord-publisher/issues"
    },
    install_requires =  ['aiohttp', 'asyncio'],
    keywords = ['discord', 'discord.py', 'discord_publisher', 'discord-publisher'],
    long_description = long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)