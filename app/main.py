from fastapi import FastAPI
from dataclasses import asdict
from fastapi.middleware.cors import CORSMiddleware
from api.config import conf
from api.consts import ALLOW_SITE
from api.router import api_router


######### Default Setting #########
c=conf()   # ! ==> Default: dev
config=asdict(c)
app=FastAPI()
###################################

######### CORS Setting ############
app.add_middleware(
    CORSMiddleware,
    # CORS Setting
    # origins에는 protocal, domain, port만 등록한다.
    allow_origins=config[ALLOW_SITE],
    allow_credentials=True, # cookie 포함 여부를 설정한다. 기본은 False
    allow_methods=["*"],    # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다.
    allow_headers=["*"],	# 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.
)
###################################

##### Route endpoint setting ######
app.include_router(api_router)
###################################