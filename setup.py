from setuptools import setup, find_packages
 
setup(
    name = 'discord_publisher',
    version = '1.0.0',
    description = 'Discord 공지 채널에 메세지를 발신해보세요!',
    author = 'Happytree Samsung',
    author_email = 'samsunghappytree123@naver.com',
    url = 'https://github.com/samsunghappytree123/discord-publisher',
    install_requires =  ['aiohttp', 'asyncio'],
    keywords = ['discord', 'discord.py', 'discord_publisher', 'discord-publisher']
)