import uvicorn
from fastapi import FastAPI
from config import HOST, PORT, RELOAD
from db.base import database
from modules.channel.app.routes import channels_router


app = FastAPI(title='Telegram channel exchange')
app.include_router(channels_router, prefix='/channels')


@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def startup():
    await database.disconnect()


@app.get('/')
async def root():
    return {'msg': 'Hello world'}


if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=PORT, reload=RELOAD, debug=True)
