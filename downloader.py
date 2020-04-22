import pandas as pd
from pandas_datareader import data
from pandas.tseries.offsets import BDay
from pandas_datareader._utils import RemoteDataError

class Downloader():
  start_date = '2010-1-1'
  end_date = (pd.datetime.today() - BDay(1)).strftime('%Y-%m-%d')
  def __init__(self, ticker, start_date = start_date, end_date=end_date, adj_close_only=True):
    """
    adj_close_only is set on True by default. Explicitly set it to False if you want the complete yahoo finance historical price data.
    start_date is set as 2010-1-1 by default.
    end_date is set as the last business day by default.
    """
    self.ticker = ticker
    self.start_date = start_date
    self.end_date = end_date
    self.adj_close_only = adj_close_only

  def get_daily_prices(self):
    """
    return dataframe containing daily prices from Yahoo, using pandas_datareader data.DataReader method
    """
    try:
      if self.adj_close_only :
        close_prices_df = data.DataReader(name=self.ticker, 
                                          start=self.start_date, 
                                          end=self.end_date, 
                                          data_source = 'yahoo')['Adj Close']
      else:
        close_prices_df = data.DataReader(name=self.ticker, 
                                          start=self.start_date, 
                                          end=self.end_date, 
                                          data_source = 'yahoo')    
      return close_prices_df
    except RemoteDataError:
      print("No data found for symbol {} using Yahoo Finance.".format(self.ticker))

      
  def save_to_csv(self,path='data/'):
    """
    Save dataframe into csv file. Default path is a data folder in the current working directory.
    """
    try:
      csv_file_name = "/" + self.ticker + "_from_{}_to_{}.csv".format(self.start_date, self.end_date)
      self.get_daily_prices().to_csv(path + csv_file_name)
    except AttributeError:
      pass

