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

@app.get('/courses/{course_id}')
async def get_courses(course_id:int):
    course = courses[course_id]
    course.update({"id":course_id})

    return course

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host= '0.0.0.0', port = 8000, reload= True)