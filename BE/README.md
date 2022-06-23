
## Intro
Used FastAPI, python3


## How to run
```
pip install -r requirements.txt

uvicorn main:app
```


## Swagger
http://localhost:8000/docs


## Schedule batch
used 'fastapi_utils.tasks:repeat_every' on schedule.py


## DB

used PostgreSQL v14

- create table

```postgresql
CREATE TABLE public.quote_mt (
	id numeric NOT NULL DEFAULT nextval('quote_mt_id_seq'::regclass),
	symbol varchar NULL,
	"name" varchar NULL,
	price varchar NULL,
	currency varchar NULL,
	is_active varchar NULL,
	is_fiat varchar NULL,
	last_updated timestamp NULL,
	create_dtm timestamp NULL DEFAULT now(),
	cid varchar NULL,
	CONSTRAINT quote_mt_pkey PRIMARY KEY (id)
);
CREATE INDEX quote_mt_create_dtm_idx ON public.quote_mt USING btree (create_dtm, symbol);
CREATE INDEX quote_mt_currency_idx ON public.quote_mt USING btree (currency, symbol, last_updated);
CREATE INDEX quote_mt_symbol_idx ON public.quote_mt USING btree (symbol);

```

## !
- constants(CMC_PRO_API_KEY) is not uploaded due to security reason
