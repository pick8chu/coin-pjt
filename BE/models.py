from decimal import Decimal
from sqlalchemy import Column, ForeignKey, Integer, String, Float, BigInteger, DateTime, Date, Numeric, Boolean, Text, BigInteger, null # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from database import Base

class Quote(Base):
    __tablename__ = "quote_mt"

    id = Column(Numeric, primary_key=True, server_default="nextval('quote_mt_id_seq'::regclass)")
    symbol = Column(String(50))
    name = Column(String(50))
    is_active = Column(String(1), server_default="null")
    is_fiat = Column(String(1), server_default="null")
    price = Column(String(50))
    currency = Column(String(50))
    last_updated = Column(DateTime)
    cid = Column(String(50))

    def convertFromDict(dict):
        quote = Quote()
        quote.symbol = dict['symbol']
        quote.name = dict['name']
        quote.is_active = dict['is_active'] if 'is_active' in dict else None
        quote.is_fiat = dict['is_fiat'] if 'is_fiat' in dict else None
        if 'USD' in dict['quote']:        
            quote.price = dict['quote']['USD']['price']
            quote.currency = 'USD'
        elif 'KRW' in dict['quote']:        
            quote.price = dict['quote']['KRW']['price']
            quote.currency = 'KRW'
        quote.last_updated = dict['last_updated']
        quote.cid = dict['id']
        return quote
