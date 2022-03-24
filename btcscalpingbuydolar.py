from selenium import webdriver
from threading import Timer
import time
import datetime
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import xlsxwriter
from decimal import *
import math

PATH = "C:\\Users\\deniz\\Documents\\Python CryptoBot Stuff\\Gecko Driver"

#BTC = BTC
#MAKE SURE TO REFRESH THE BINANCE PAGE BEFORE TRADES.


#SANAL CASH(BTC)
BTC_Buy_Money = 0.00
BTC_Sel_Money = 0.00
BTC_CASH = 100.00


#COIN CHECKER(BTC)
BTC_OnTrading = 0


#Global BTC Variables
BTC_LastPrice = 0.00
BTC_TTS = 0.00
BTC_RSI3 = 0.00
BTC_RSI14 = 0.00
BTC_ADXDI_G = 0.00
BTC_ADXDI_R = 0.00



#Excel Versiyon
Genel_Excel_Sayi_OLD = 0
Genel_Excel_Sayi = 1
Genel_Excel_Sayi_P_BTC = 1


Excel_Versiyon = 0

# CoinDrivers(BTC)
driverBTC = webdriver.Firefox(PATH) #Actually BTC
driverBTC_BINANCE = webdriver.Firefox(PATH)


#DATE&TIME
now = datetime.datetime.now()
#now = datetime.datetime.now()




def ExcelFileCreate():
    #FOR GLOBAL VARIABLE
    global now
    #FOR BTC VARIABLE MAKE GLOBAL
    global BTC_Sheet
    global BTC_Sheet_Profit
    global BTC_Workbook


    
    # Excel File Create(BTC)
    now = datetime.datetime.now()
    BTC_Workbook = xlsxwriter.Workbook(r'C:\\Users\\deniz\\Documents\\Python CryptoBot Stuff\\Coins\\Coin1\\BTC_DATE_' + now.strftime("%d_%m_%y") + "_" + str(Excel_Versiyon) + ".xlsx")


    # Excel Sheet Create(BTC)
    BTC_Sheet = BTC_Workbook.add_worksheet(name="BTC")
    BTC_Sheet_Profit = BTC_Workbook.add_worksheet(name="PROFIT")


    #Modify Excel Sheet(BTC)
    BTC_Sheet.set_header("BTC")
    BTC_Sheet.write(0, 0, "Versiyon")
    BTC_Sheet.write(0, 1, "Last Price")
    BTC_Sheet.write(0, 2, "TTS")
    BTC_Sheet.write(0, 3, "Stochastic RSI(3)")
    BTC_Sheet.write(0, 4, "Stochastic RSI(14)")
    BTC_Sheet.write(0, 5, "ADX(G)")
    BTC_Sheet.write(0, 6, "ADX(R)")
    BTC_Sheet.set_column("D:D", 15)
    BTC_Sheet.set_column("E:E", 15)


    

    # Modify Excel Sheet(BTC)
    BTC_Sheet_Profit.write(0, 0, "Date")
    BTC_Sheet_Profit.write(0, 1, "Profit")
    BTC_Sheet_Profit.write(0, 2, "Cash")


    BTC_Sheet_Profit.set_column("A:A", 20)
    BTC_Sheet_Profit.set_column("B:B", 20)
    BTC_Sheet_Profit.set_column("C:C", 20)



#CoinWebsite_Opener
def CoinData_Website():

    # OPEN DRIVER(BTC)
    driverBTC.get("https://www.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT")
    driverBTC.maximize_window()
    time.sleep(30)

    print("-----Buy Login Finish-----")
    #OPEN DRIVER PLUG-IN
    driverBTC.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]/div/div").click()
    time.sleep(4)
    driverBTC.find_element_by_class_name("input-2pz7DtzH").send_keys("Trend Trader Strategy")
    time.sleep(4)
    driverBTC.find_element_by_class_name("container-1e-eHKCj").click()
    time.sleep(4)
    driverBTC.find_element_by_class_name("input-2pz7DtzH").send_keys("Stochastic RSI")
    time.sleep(4)
    driverBTC.find_element_by_class_name("container-1e-eHKCj").click()
    time.sleep(4)
    driverBTC.find_element_by_class_name("input-2pz7DtzH").send_keys("MACD")
    time.sleep(4)
    driverBTC.find_element_by_class_name("container-1e-eHKCj").click()
    time.sleep(4)
    driverBTC.find_element_by_class_name("close-3NTwKnT_").click()
    time.sleep(30)
    print("-----System Ready(BTC_BUY)-----")
    
    time.sleep(3)

    driverBTC_BINANCE.get("https://www.binance.com/en/trade/BTC_USDT") #BU BUY İÇİN
    time.sleep(60)





#CoinData_Catcher
def DataCatcher():
    #TK
    global fileCoinData
    global liveFeedData

    # FOR GLOBAL VARIABLE
    global now
    global Genel_Excel_Sayi
    global Genel_Excel_Sayi_P_BTC
    global Genel_Excel_Sayi_P_OMG
    global Genel_Excel_Sayi_P_ATOM

    global Excel_Versiyon

    #SANAL CASH(BTC)
    global BTC_CASH
    global BTC_Buy_Money
    global BTC_Sel_Money
    

    
    #FOR BTC VARIABLE MAKE GLOBAL
    global BTC_Workbook
    global BTC_Sheet
    global BTC_Sheet_Profit
    global BTC_LastPrice
    global BTC_TTS
    global BTC_RSI3
    global BTC_RSI14
    global BTC_OnTrading
    global BTC_ADXDI_G
    global BTC_ADXDI_R
    


    print("-----BTC BUY Jenerasyon " + str(Genel_Excel_Sayi) + "-----")
    now = datetime.datetime.now()
    BTC_Sheet.write(Genel_Excel_Sayi, 0, now.strftime("%H:%M:%S"))



    
    BTC_Coin_3 = driverBTC.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div").text
    print("BTC Stochastic RSI(3) is: " + BTC_Coin_3)
    BTC_RSI3 = float(BTC_Coin_3.replace("−", ""))
    BTC_Sheet.write(Genel_Excel_Sayi, 3, BTC_RSI3)

    BTC_Coin_14 = driverBTC.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div").text
    print("BTC Stochastic RSI(14) is: " + BTC_Coin_14)
    BTC_RSI14 = float(BTC_Coin_14.replace("−", ""))
    BTC_Sheet.write(Genel_Excel_Sayi, 4, BTC_RSI14)

    BTC_Coin_TTS = driverBTC.find_element_by_xpath("(//div[@class='valuesWrapper-1ukbb5SP'])[2]").text
    BTC_Coin_TTS = BTC_Coin_TTS.replace("M", "")
    BTC_Coin_TTS = BTC_Coin_TTS.replace("K", "")
    print("BTC TTS is: " + BTC_Coin_TTS)
    BTC_TTS = float(BTC_Coin_TTS) #TTS is TTS now.
    BTC_Sheet.write(Genel_Excel_Sayi, 2, BTC_TTS)

    BTC_Coin = driverBTC.find_element_by_class_name("priceWrapper-12IXdGf3").text
    BTC_Coin = BTC_Coin.replace("USDT", "")
    BTC_Coin = BTC_Coin[0:6]
    print("BTC Last Price is: " + BTC_Coin)
    BTC_LastPrice = float(BTC_Coin)
    BTC_Sheet.write(Genel_Excel_Sayi, 1, BTC_LastPrice)


    global BTC_AMOUNT #CHANGEABLE ACCORDING TO BALANCE. Bu amount alınan profitlere veya zararlara göre kendini updatelemeli.
    #BTC_AMOUNT_INT = math.floor(BTC_AMOUNT)
    #BTC_AMOUNT_DEC = round(float(BTC_AMOUNT),1)
    global BTC_AMOUNT_CONVERTED #= BTC_AMOUNT/BTC_LastPrice 
    action_chains = ActionChains(driverBTC_BINANCE)


    if (BTC_RSI3 >= BTC_RSI14 and BTC_RSI3 > 15 and BTC_OnTrading == 0):
        #BUY COIN
        print("Buy")
        BTC_Sheet_Profit.write(Genel_Excel_Sayi_P_BTC, 1, str(BTC_LastPrice))
        BTC_Buy_Money = BTC_LastPrice


        time.sleep(1)
        print("BTC")
        print("-----------------")

        #Place limit amount to buy coin.
        time.sleep(2)
        
        #driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[1]/div/span[2]").click() clicks the Market button.
        #time.sleep(2)

        #driverBTC_BINANCE.find_element_by_id("FormRow-BUY-total").send_keys(str(float(BTC_AMOUNT)))
        #time.sleep(2)
        #driverBTC_BINANCE.find_element_by_id("FormRow-BUY-total").send_keys(str(BTC_AMOUNT))
        #time.sleep(2)       
        driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[3]/div[1]/form/div[3]/div/div[7]").click() #buy 100% button
        time.sleep(3)
        BTC_AMOUNT = driverBTC_BINANCE.find_element_by_id("FormRow-BUY-quantity").get_attribute("value") #to compare in the while statement
        time.sleep(1)
        BTC_AMOUNT_CONVERTED = float(BTC_AMOUNT)
        time.sleep(2)
        driverBTC_BINANCE.find_element_by_id("orderformBuyBtn").click() #Rarely some other element below this one will receive the click, so another click command is added after to prevent any errors.
        time.sleep(3)

        y = 0
        while y < 1:
            y = y + 1
            
            if len(driverBTC_BINANCE.find_elements_by_class_name("css-1j1sbq7")) > 0:  #checks to see if the %100 selection button is still selected, meaning the bot want able to sell due to Insufficient Balance bug. If the itme exists, then it refreshes the page and tries buying again.
                driverBTC_BINANCE.refresh()
                time.sleep(3)
                driverBTC_BINANCE.find_element_by_class_name("css-15vandh").click() #finds an item to send keys to. For scrolling
                time.sleep(2)
                action_chains.send_keys(Keys.PAGE_DOWN).perform()        
                time.sleep(3)
                driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[1]/div/span[2]").click() #Clicks the Market tab.
                time.sleep(3)
                driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[3]/div[1]/form/div[3]/div/div[7]").click() #BUY 100% BUTTON
                time.sleep(2)
                driverBTC_BINANCE.find_element_by_id("orderformBuyBtn").click()              
                break
            
            elif len(driverBTC_BINANCE.find_elements_by_class_name("css-1j1sbq7")) == 0:
                break
            
            else:
                print("wtf")
                
        #driverBTC_BINANCE.find_element_by_id("orderformBuyBtn").click()
        #time.sleep(2)
        #driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[3]/div[1]/form/div[3]/div/div[7]").click() buy 100% button
        #time.sleep(1)
        #driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[3]/div[1]/form/div[3]/div/div[3]").click() buy 0% button


        time.sleep(10) #Grace period for the coin amount to be accumulated.

        now = datetime.datetime.now()
        BTC_Sheet_Profit.write(Genel_Excel_Sayi_P_BTC, 0, now.strftime("%d-%m-%y %H:%M:%S"))
        Genel_Excel_Sayi_P_BTC += 1
        BTC_OnTrading = 1

    else:
        #DOING NOTHING
        print("Waiting")

    
    if (BTC_RSI3 < BTC_RSI14 and BTC_OnTrading == 1):
        #SELL COIN
        print("Coin Sell")
        BTC_Sheet_Profit.write(Genel_Excel_Sayi_P_BTC, 1, str(BTC_LastPrice))
        BTC_Sel_Money = BTC_LastPrice
        time.sleep(1)

        
        #driverBTC_BINANCE.find_element_by_id("FormRow-SELL-total").send_keys(str(float(BTC_AMOUNT_SELL)))
        #time.sleep(2)
        driverBTC_BINANCE.find_element_by_xpath("(//div[@class='css-v6fymx'])[2]").click() #SELL 100% BUTTON
        time.sleep(2)

        coin_balance = driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[3]/div[2]/div/div[2]/span").text
        coin_balance_number = coin_balance.replace(" BTC", "") #SHOULD BE BTC TO BE REPLACED.
        time.sleep(2)


        while float(coin_balance_number) != BTC_AMOUNT_CONVERTED * 1.5:

            if float(coin_balance_number) > (BTC_AMOUNT_CONVERTED * 0.98): #bazen buy order verildikten sonra binance hatalı alım yapıp, yaklaşık %0.3 civarı daha az mal alıyor. Bu yüzden ona göre if statement yazıldı.
            #if len(driverETHUP_BINANCE.find_elements_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/div/div[2]/span")) > 0: #as long as it can see the coin balance, it will click the sell button until it can actually sell.
                print("buM")
                driverBTC_BINANCE.find_element_by_id("orderformSellBtn").click()
                time.sleep(3)
                break

            elif float(coin_balance_number) <= (BTC_AMOUNT_CONVERTED * 0.98):

                coin_balance = driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/div/div[2]/span").text
                coin_balance_number = coin_balance.replace(" BTC", "") #SHOULD BE BTC TO BE REPLACED.
                time.sleep(3)
                
                if float(coin_balance_number) > (BTC_AMOUNT_CONVERTED * 0.98): #to break if the accumulation for the coin is made within this if statement. Saliseler ile error vermesin diye yakalama kodu.
                    driverBTC_BINANCE.find_element_by_id("orderformSellBtn").click()
                    time.sleep(3)
                    break
                
                elif float(coin_balance_number) <= (BTC_AMOUNT_CONVERTED * 0.98):
                    driverBTC_BINANCE.find_element_by_id("orderformSellBtn").click() #code to keep clicking the sell button until the desired amount of coin is obtained.
                    time.sleep(5)
                    print("...")
                    continue

                else:
                    print("wtf man")
            
            
            else:
                print("wtf")
                time.sleep(2)
            

        time.sleep(3)

        #driverBTC_BINANCE.find_element_by_id("orderformSellBtn").click()
        #time.sleep(2)
        #BURAYA IF STATEMENT I KOY: EĞER Kİ AŞAĞIDAKİ ELEMENTİ BULAMAZSA SAYFAYI REFRESHLETİP, AŞAĞI İNDİRİP TEKRAR MARKET TAB İNE GETİRT. DAHA SONRA TEKRAR %100 E BASTIRT, SAT VE AMOUNT BOX UNU SIFIRLA. 
        #ERROR VERMESİNİN NEDENİ INSUFFİCİENT FUNDS BUG OLUYO ELİMİZDE FUNDS OLSA BİLE.
        x = 0
        while x < 1:
            x = x + 1
            
            if len(driverBTC_BINANCE.find_elements_by_xpath("(//div[@class='css-v6fymx'])[2]")) > 0:   
                #driverBTC_BINANCE.find_element_by_xpath("(//div[@class='css-v6fymx'])[2]").click() #SELL %100 BUTTON
                #time.sleep(2) 
                #driverBTC_BINANCE.find_element_by_xpath("(//div[@class='css-4l9ic'])[2]").click() #SELL 0% BUTTON 
                #time.sleep(2)
                break
            
            elif len(driverBTC_BINANCE.find_elements_by_xpath("(//div[@class='css-v6fymx'])[2]")) == 0:
                driverBTC_BINANCE.refresh()
                time.sleep(3)
                driverBTC_BINANCE.find_element_by_class_name("css-15vandh").click() #finds an item to send keys to. For scrolling
                time.sleep(2)
                action_chains.send_keys(Keys.PAGE_DOWN).perform()        
                time.sleep(3)
                driverBTC_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[1]/div/span[2]").click() #Clicks the Market tab.
                time.sleep(3)
                driverBTC_BINANCE.find_element_by_xpath("(//div[@class='css-v6fymx'])[2]").click() #SELL 100% BUTTON
                time.sleep(2)
                driverBTC_BINANCE.find_element_by_id("orderformSellBtn").click()
                time.sleep(2)
                
                if len(driverBTC_BINANCE.find_elements_by_class_name("css-nv3j7q")) > 0:
                    driverBTC_BINANCE.find_element_by_class_name("css-nv3j7q").click()
                    time.sleep(2)
                
                elif len(driverBTC_BINANCE.find_elements_by_class_name("css-nv3j7q")) == 0:
                    break
                
                else:
                    "wtf ulan"
                
            
            else:
                print("wtf")
        
        #time.sleep(3)
        #driverBTC_BINANCE.find_element_by_xpath("(//div[@class='css-v6fymx'])[2]").click() #SELL 100% BUTTON
        #time.sleep(2)

        #driverBTC_BINANCE.find_element_by_xpath("(//div[@class='css-4l9ic'])[2]").click() #SELL 0% BUTTON
        time.sleep(3)        
        
        

        #Excel shit
        now = datetime.datetime.now()
        BTC_Sheet_Profit.write(Genel_Excel_Sayi_P_BTC, 0, now.strftime("%d-%m-%y %H:%M:%S") )
        BTC_CASH = (((BTC_Sel_Money - BTC_Buy_Money) / BTC_Buy_Money) * 100 )+ BTC_CASH
        BTC_Sheet_Profit.write(Genel_Excel_Sayi_P_BTC, 2, "Cash: " + str(BTC_CASH))
        Genel_Excel_Sayi_P_BTC += 1
        BTC_OnTrading = 0
    
    else:
        #DOING NOTHING
        print("Waiting")


    print( "----BTC: " + str(BTC_CASH) + "$ ----")

    
    Genel_Excel_Sayi += 1

    # per day 4320
    # per hour 180
    if Genel_Excel_Sayi > 180:
        BTC_Workbook.close()
        Excel_Versiyon += 1
        Genel_Excel_Sayi = 1
        Genel_Excel_Sayi_P_BTC = 1
        Genel_Excel_Sayi_P_OMG = 1
        Genel_Excel_Sayi_P_ATOM = 1
        ExcelFileCreate()

    
    Timer(1800, DataCatcher).start() #Bu sayı 910 olmalı
    

ExcelFileCreate()
CoinData_Website()
DataCatcher()