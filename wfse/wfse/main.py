from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return {'message': 'welcome to Web For Simple Enjoy'}