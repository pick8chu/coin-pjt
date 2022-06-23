from fastapi import FastAPI, Depends, Request, Response, Query, Body
from routes.coinmarket.router import router
from fastapi.middleware.cors import CORSMiddleware
import schedule 
import hmac
import hashlib
import logging

key = "safekey"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# logger.addHandler(logHandler)

app = FastAPI()
app.include_router(router)

# @app.middleware("http")
# async def log_request(request, call_next):
#     logger.info(f'{request.method} {request.url}')
#     response = await call_next(request)
#     logger.info(f'Status code: {response.status_code}')
#     body = b""
#     async for chunk in response.body_iterator:
#         body += chunk
    
#     # TODO: list body cannot be convert to hmac -> it won't work as an auth.
#     body = body    
#     #'bytes' object has no attribute 'encode'
#     signature = hmac.new(key.encode('utf-8'), body, hashlib.sha256).hexdigest()
    
#     return Response(
#         content={"data":body, 'signature':signature},
#         status_code=response.status_code,
#         headers=dict(response.headers),
#         media_type=response.media_type
#     )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["http://localhost:8080", "Access-Control-Allow-Origin"],
)

@app.on_event("startup")
async def scheduledAddQuoteList():
    await schedule.scheduledAddQuoteList()