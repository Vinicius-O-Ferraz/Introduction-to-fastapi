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