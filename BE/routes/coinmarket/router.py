from csv import list_dialects
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from . import controllers
from database import get_db

router = APIRouter()

#  quote Cache / Update frequency: Every 60 seconds.
@router.get("/quotes/{symbols}")
async def getQuotes(symbols:str='BTC,ETH', currencys:str='KRW'):
    return await controllers.getQuotes(symbols, currencys)

@router.get("/quote-history/{symbols}")
async def getQuoteHistory(dateFrom:str, dateTo:str, symbols:str='BTC,USDT', currencys:str='USD', db: Session = Depends(get_db)):
    return await controllers.getQuoteHistory(dateFrom, dateTo, symbols, currencys, db)
     
@router.post("/quotes/{symbols}")
async def addQuotes(symbols: str='BTC,USDT,ETH,XRP,ATOM', currencys: str='USD,KRW', db: Session = Depends(get_db)):
    await controllers.addQuotes(symbols, currencys, db)
     
@router.post("/quotes/list")
async def addQuoteList(db: Session = Depends(get_db)):
    await controllers.addQuoteList(db)
     
