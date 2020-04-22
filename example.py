#An example importing MSFT data.
from downloader import Downloader

start = '2003-4-1'
example_ticker = 'MSFT'
MSFT_df = Downloader(example_ticker,start_date = start, adj_close_only= False)
MSFT_df.save_to_csv()