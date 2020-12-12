import aiohttp
import asyncio

class Publisher:
    def __init__(self, token:str, channel_id:int, message_id:int):
        self.token = token
        self.channel_id = channel_id
        self.message_id = message_id
    
    async def postnotices(self):
        async with aiohttp.ClientSession() as session:
            headers = {
                'Authorization' : f'Bot {self.token}'
            }
            url = "https://discord.com/api/v6/channels/{}/messages/{}/crosspost".format(self.channel_id, self.message_id)
            async with session.post(url=url, headers=headers) as re:
                if re.status == 200:
                    return print("공지 발신을 성공했습니다.")
                elif re.status == 400:
                    return print("잘못된 요청입니다.")
                elif re.status == 401 or re.status == 403:
                    return print("권한이 없어 공지를 발신하지 못했습니다.")
                elif re.status == 404:
                    return print("메세지 또는 채널이 없습니다.")
                elif re.status == 429:
                    return print("너무 많은 요청을 보냈습니다.")
                else:
                    return print(re.status)

    def postnotice(self):
        asyncio.run(Publisher.postnotices(self))