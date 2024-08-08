from fastapi import FastAPI

app = FastAPI()

courses= {
    1:{
        'title': 'C for embedded systems',
        'classes': 112,
        'hours':58
    },
    2:{
        'title': 'C programming for dummies',
        'classes':14,
        'hours': 15
    }
}

@app.get('/courses')
async def get_courses():
    return courses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host= '0.0.0.0', port = 8000)