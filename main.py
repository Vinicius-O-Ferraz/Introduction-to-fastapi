from typing import Optional, List
from fastapi import FastAPI
from fastapi import HTTPException, status
from models import Course

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
async def get_course(course_id:int):
    try:
        course = courses[course_id]
        course.update({"id":course_id})
        return course

    except KeyError:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = 'course not found')

@app.post('/courses', status_code= status.HTTP_201_CREATED)
async def post_course(course:Course):
    next_id = len(courses) + 1
    if course.id not in courses:
        courses[next_id] = course
        return course
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f'A course with that id; {Course.id} already exists ')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host= '0.0.0.0', port = 8000, reload= True)