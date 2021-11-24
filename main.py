from fastapi import FastAPI


app = FastAPI(title='Simple API')


@app.get('/home/{item}')
async def get_some_info(item: str):
    return f"Hello world {item}"
