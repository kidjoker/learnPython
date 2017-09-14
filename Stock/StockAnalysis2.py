import tushare as ts
from sqlalchemy import create_engine

if __name__ == '__main__':
	df = ts.get_gdp_pull()
	engine = create_engine('mysql://root:jasonkimi@47.52.119.111/stock?charset=utf8')

	df.to_sql('gdp_data',engine,if_exists='append')