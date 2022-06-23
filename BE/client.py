from fastapi.exceptions import HTTPException
import httpx
import asyncio
import hmac
import hashlib
import constants

TEST_URL = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
COIN_MARKET_BASE_URL = "https://pro-api.coinmarketcap.com"

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': constants.CMC_PRO_API_KEY,
}
key = "safekey"

async def request(preReqList:list):
    async with httpx.AsyncClient(headers=headers) as client:
        reqList = [req['method'](client, f"{COIN_MARKET_BASE_URL}{req['uri']}", params=req['params']) for req in preReqList]

        # gather is for multiple request
        resList = (await asyncio.gather(*reqList))
        
        for i, res in enumerate(resList): 
            if res.status_code == 200:
                print("status code :: 200")
            else:
                print(f"ERROR :: {res.status_code} :: {res.text}")
                raise HTTPException(status_code=res.status_code, detail=f'reqNo: {i} : {res.text}')

        return list(map(lambda req: req.json()['data'], resList))

async def get(client, uri, params):
    return await client.get(uri, params=params)
