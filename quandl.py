import urllib2

###
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
###

"""
def getQ(ticker):
    netIncome = Quandl.get(("DMDRN/"+ticker+"_NET_INC"), trim_start="2002-12-31", trim_end="2012-12-31")
    revenue = Quandl.get(("DMDRN/"+ticker+"_REV_LAST"), trim_start="2002-12-31", trim_end="2012-12-31")
    ROC = Quandl.get(("DMDRN/"+ticker+"_ROC"), trim_start="2002-12-31", trim_end="2012-12-31")
    print(netIncome, revenue, ROC)
    plt.subplot(3,1,1)
    plt.title(ticker)
    plt.ylabel("Net Income")
    plt.plot(netIncome.index, netIncome)
    plt.subplot(3,1,2)
    plt.ylabel("Revenue")
    plt.plot(revenue.index, revenue)
    plt.subplot(3,1,3)
    plt.ylabel("Return on Capital")
    plt.plot(ROC.index, ROC)
    plt.show()
"""



def grabQuandl(ticker):

    netIncomeAr = []
    revAr = []
    ROCAr = []


    endLink = 'sort_order=asc'

    endLink2 = 'sort_order=asc&auth_token=asdfasdfsagsvasd'
    try:
        netIncome = urllib2.urlopen('http://www.quandl.com/api/v1/datasets/OFDP/DMDRN_'+ticker+'_NET_INC.csv?&'+endLink).read()
        revenue = urllib2.urlopen('http://www.quandl.com/api/v1/datasets/OFDP/DMDRN_'+ticker+'_REV_LAST.csv?&'+endLink).read()
        ROC = urllib2.urlopen('http://www.quandl.com/api/v1/datasets/OFDP/DMDRN_'+ticker+'_ROC.csv?&'+endLink).read()

        splitNI = netIncome.split('\n')
        print 'Net Income:'
        for eachNI in splitNI[1:-1]:
            print eachNI
            netIncomeAr.append(eachNI)

        print '_________'
        splitRev = revenue.split('\n')
        print 'Revenue:'
        for eachRev in splitRev[1:-1]:
            print eachRev
            revAr.append(eachRev)


        print '_________'
        splitROC = ROC.split('\n')
        print 'Return on Capital:'
        for eachROC in splitROC[1:-1]:
            print eachROC
            ROCAr.append(eachROC)


        incomeDate, income = np.loadtxt(netIncomeAr, delimiter=',',unpack=True,
                                        converters={ 0: mdates.strpdate2num('%Y-%m-%d')})

        revDate, revenue = np.loadtxt(revAr, delimiter=',',unpack=True,
                                        converters={ 0: mdates.strpdate2num('%Y-%m-%d')})

        rocDate, ROC = np.loadtxt(ROCAr, delimiter=',',unpack=True,
                                        converters={ 0: mdates.strpdate2num('%Y-%m-%d')})





        fig = plt.figure()

        ax1 = plt.subplot2grid((6,6),(0,0), rowspan=2, colspan=6)
        ax1.plot(incomeDate, income)

        ax2 = plt.subplot2grid((6,6),(2,0), sharex=ax1, rowspan=2, colspan=6)
        ax2.plot(revDate, revenue)

        ax3 = plt.subplot2grid((6,6),(4,0), sharex=ax1, rowspan=2, colspan=6)
        ax3.plot(rocDate, ROC)


        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.subplots_adjust(hspace=0.53)

        plt.show()

    except Exception, e:
        print 'failed the main quandl loop for reason of',str(e)

grabQuandl('YHOO')