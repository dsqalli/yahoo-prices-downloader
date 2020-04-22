from downloader import *
start = '2003-4-1'
end = '2008-12-31'

MSFT = Downloader('MSFT',start_date = start, end_date = end, adj_close_only=True)
MSFT.save_to_csv()