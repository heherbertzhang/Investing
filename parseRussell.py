def parseRus():
    tickers = []
    try:
        with open('russell3000.txt', 'r') as fp:
            for line in fp:
                ticker = line.split(' ')[-1].strip()
                tickers.append(ticker)
    except Exception as e:
        print str(e)

    print tickers
    return tickers