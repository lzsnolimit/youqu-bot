import edge_tts

async def edge_tss(TEXT) -> str:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
