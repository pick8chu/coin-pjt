from requests import session
from routes.coinmarket.controllers import addQuoteList
from fastapi_utils.tasks import repeat_every
from database import SQLALCHEMY_DATABASE_URI
from fastapi_utils.session import FastAPISessionMaker

sessionmaker = FastAPISessionMaker(SQLALCHEMY_DATABASE_URI)

@repeat_every(seconds=60 * 60)    # 1 hr
async def scheduledAddQuoteList():
    print("executed :: scheduledAddQuoteList")
    with sessionmaker.context_session() as db:
        await addQuoteList(db)
