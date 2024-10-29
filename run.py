import edge_tts

async def list_voices():
    voices = await edge_tts.Voice.list()
    for voice in voices:
        print(voice)

import asyncio
asyncio.run(list_voices())
