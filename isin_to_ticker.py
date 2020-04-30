import requests

def isin_to_ticker(isin):
    """take ISIN as input and return Yahoo symbol"""
    request_url = "https://query2.finance.yahoo.com/v1/finance/search?q=" + isin + "&quotesCount=6&newsCount=0&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&newsQueryId=news_ss_symbols&enableCb=false&enableNavLinks=false&vespaNewsTimeoutMs=600"
    response = requests.get(request_url).content
    return(str(response).split(":")[7].split(",")[0].replace('"',""))

