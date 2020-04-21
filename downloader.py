from pandas_datareader import data

class Downloader():
  def __init__(self, ticker, start_date, end_date, adj_close=True):
    self.ticker = ticker
    self.start_date = start_date
    self.end_date = end_date
    self.adj_close = adj_close

  def get_daily_prices(self):
    """get daily prices from Yahoo"""
    try:
      if self.adj_close :
        close_prices_df = data.DataReader(name=self.ticker, start=self.start_date, end=self.end_date, data_source = 'yahoo')['Adj Close']
      else:
        close_prices_df = data.DataReader(name=self.ticker, start=self.start_date, end=self.end_date, data_source = 'yahoo')    
      return close_prices_df
    except:
      pass
      
  def daily_prices_to_csv(self):
    try:
      self.get_daily_prices().to_csv(self.ticker + '_from_{}_to_{}.csv'.format(self.start_date, self.end_date))
    except AttributeError:
      print("Please make sure you're entering a valid ticker symbol and valid start and end dates.")




start = '2010-1-1'
end = '2020-4-17'
yahoo = Downloader('^FCHI',start, end)
yahoo.daily_prices_to_csv()
