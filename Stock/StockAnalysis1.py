#coding=utf-8
import tushare as ts

def get_all_price(code_list,f):
	df = ts.get_realtime_quotes(STOCK)
	print >> f,df

def get_gdp_data():
	df = ts.get_gdp_pull()
	print >> f,df

if __name__ == '__main__':
	STOCK = ['600219',	##南方铝业
			 '600002',  ##万科A
			 '600036',  ##招商银行
			 '600750',  ##江中药业
			 '600338',  ##潍柴动力
			 '600792']  ##盐湖股份
	
	f = open("OutFile/2017_9_12.csv",'w+')

	#get_all_price(STOCK,f)
	get_gdp_data()
