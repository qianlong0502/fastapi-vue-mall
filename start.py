import uvicorn
from main import app
from fastapi.middleware.cors import CORSMiddleware


if __name__ == '__main__':
    # 前端页面url
    origins = [
        "*"
    ]

    # 后台api允许跨域
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    uvicorn.run(app, host="127.0.0.1", port=8895)
