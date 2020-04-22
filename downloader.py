from pandas_datareader import data

class Downloader():
  def __init__(self, ticker, start_date, end_date, adj_close_only=True):
    """
    adj_close_only is set on True as Default. Explicitly set it to False if you want the complete yahoo finance historical price data.
    """
    self.ticker = ticker
    self.start_date = start_date
    self.end_date = end_date
    self.adj_close_only = adj_close_only

  def get_daily_prices(self):
    """
    returns a dataframe containing the daily prices from Yahoo, using pandas_datareader data.DataReader method
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
    except:
      pass
      
  def save_to_csv(self,path='data/'):
    """
    Saves the dataframe into a csv file. Default path is a data folder in the current working directory.
    """
    try:
      csv_file_name = self.ticker + '_from_{}_to_{}.csv'.format(self.start_date, self.end_date)
      self.get_daily_prices().to_csv(path + csv_file_name)
    except AttributeError:
      print("Please make sure you're entering a valid ticker symbol and valid start and end dates.")



start = '2010-1-1'
end = '2020-4-17'
yahoo = Downloader('^FCHI',start, end)
yahoo.save_to_csv(r'C:\Users\Driss Sqalli\Desktop')
