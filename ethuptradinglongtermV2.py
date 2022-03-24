from selenium import webdriver
from threading import Timer
import time
from datetime import datetime
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import xlsxwriter
from decimal import *
import math

PATH = "C:\\Users\\deniz\\Documents\\Python CryptoBot Stuff\\Gecko Driver"

#ETHUP = ETHUP
#MAKE SURE TO REFRESH THE BINANCE PAGE BEFORE TRADES.


#SANAL CASH(ETHUP)
ETHUP_Buy_Money = 0.00
ETHUP_Sel_Money = 0.00
ETHUP_CASH = 100.00


#COIN CHECKER(ETHUP)
ETHUP_OnTrading = 0


#Global ETHUP Variables
ETHUP_LastPrice = 0.00
ETHUP_Ichimoku = 0.00
ETHUP_RSI3 = 0.00
ETHUP_RSI14 = 0.00
ETHUP_ADXDI_G = 0.00
ETHUP_ADXDI_R = 0.00



#Excel Versiyon
Genel_Excel_Sayi_OLD = 0
Genel_Excel_Sayi = 1
Genel_Excel_Sayi_P_ETHUP = 1


Excel_Versiyon = 0

# CoinDrivers(ETHUP)
driverETHUP = webdriver.Firefox(PATH) #Actually ETHUP
driverETHUP_BINANCE = webdriver.Firefox(PATH)


#DATE&TIME
now = datetime.now()
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")
#now = datetime.now()




def ExcelFileCreate():
    #FOR GLOBAL VARIABLE
    global now
    #FOR ETHUP VARIABLE MAKE GLOBAL
    global ETHUP_Sheet
    global ETHUP_Sheet_Profit
    global ETHUP_Workbook


    
    # Excel File Create(ETHUP)
    now = datetime.now()
    ETHUP_Workbook = xlsxwriter.Workbook(r'C:\\Users\\deniz\\Documents\\Python CryptoBot Stuff\\Coins\\Coin1\\ETHUP_DATE_' + now.strftime("%d_%m_%y") + "_" + str(Excel_Versiyon) + ".xlsx")


    # Excel Sheet Create(ETHUP)
    ETHUP_Sheet = ETHUP_Workbook.add_worksheet(name="ETHUP")
    ETHUP_Sheet_Profit = ETHUP_Workbook.add_worksheet(name="PROFIT")


    #Modify Excel Sheet(ETHUP)
    ETHUP_Sheet.set_header("ETHUP")
    ETHUP_Sheet.write(0, 0, "Versiyon")
    ETHUP_Sheet.write(0, 1, "Last Price")
    ETHUP_Sheet.write(0, 2, "Ichimoku")
    ETHUP_Sheet.write(0, 3, "Stochastic RSI(3)")
    ETHUP_Sheet.write(0, 4, "Stochastic RSI(14)")
    ETHUP_Sheet.write(0, 5, "ADX(G)")
    ETHUP_Sheet.write(0, 6, "ADX(R)")
    ETHUP_Sheet.set_column("D:D", 15)
    ETHUP_Sheet.set_column("E:E", 15)


    

    # Modify Excel Sheet(ETHUP)
    ETHUP_Sheet_Profit.write(0, 0, "Date")
    ETHUP_Sheet_Profit.write(0, 1, "Profit")
    ETHUP_Sheet_Profit.write(0, 2, "Cash")


    ETHUP_Sheet_Profit.set_column("A:A", 20)
    ETHUP_Sheet_Profit.set_column("B:B", 20)
    ETHUP_Sheet_Profit.set_column("C:C", 20)



#CoinWebsite_Opener
def CoinData_Website():

    # OPEN DRIVER(ETHUP)
    driverETHUP.get("https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT") #ETH GRAPH TO BE USED INSTEAD OF ETHUP FOR BTTER RESULTS.
    driverETHUP.maximize_window()
    time.sleep(30)

    print("-----Buy Login Finish-----")
    #OPEN DRIVER PLUG-IN
    driverETHUP.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]/div/div").click()
    time.sleep(4)
    driverETHUP.find_element_by_class_name("input-3n5_2-hI").send_keys("Ichimoku")
    time.sleep(4)
    driverETHUP.find_element_by_class_name("container-3Ywm3-oo").click()
    time.sleep(4)
    driverETHUP.find_element_by_class_name("input-3n5_2-hI").send_keys("Stochastic RSI")
    time.sleep(4)
    driverETHUP.find_element_by_class_name("container-3Ywm3-oo").click()
    time.sleep(4)
    driverETHUP.find_element_by_class_name("input-3n5_2-hI").send_keys("MACD Histogram")
    time.sleep(4)
    driverETHUP.find_element_by_class_name("container-3Ywm3-oo").click()
    time.sleep(4)
    driverETHUP.find_element_by_class_name("close-2sL5JydP").click()
    time.sleep(30)
    print("-----System Ready(ETHUP_BUY)-----")
    
    time.sleep(3)

    driverETHUP_BINANCE.get("https://www.binance.com/en/trade/ETHUP_USDT") #BU BUY İÇİN
    time.sleep(60)





#CoinData_Catcher
def DataCatcher():
    #TK
    global fileCoinData
    global liveFeedData

    # FOR GLOBAL VARIABLE
    global now
    global Genel_Excel_Sayi
    global Genel_Excel_Sayi_P_ETHUP
    global Genel_Excel_Sayi_P_OMG
    global Genel_Excel_Sayi_P_ATOM

    global Excel_Versiyon

    #SANAL CASH(ETHUP)
    global ETHUP_CASH
    global ETHUP_Buy_Money
    global ETHUP_Sel_Money
    

    #FOR ETHUP VARIABLE MAKE GLOBAL
    global ETHUP_Workbook
    global ETHUP_Sheet
    global ETHUP_Sheet_Profit
    global ETHUP_LastPrice
    global ETHUP_Ichimoku
    global ETHUP_RSI3
    global ETHUP_RSI14
    global ETHUP_OnTrading
    global ETHUP_ADXDI_G
    global ETHUP_ADXDI_R
    global ETHUP_MACD_MOMENTUM
    

    


    print("-----ETHUP BUY Jenerasyon " + str(Genel_Excel_Sayi) + "-----")
    now = datetime.now()
    ETHUP_Sheet.write(Genel_Excel_Sayi, 0, now.strftime("%H:%M:%S"))



    
    ETHUP_Coin_3 = driverETHUP.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div").text
    print("ETHUP Stochastic RSI(3) is: " + ETHUP_Coin_3)
    ETHUP_RSI3 = float(ETHUP_Coin_3.replace("−", ""))
    ETHUP_Sheet.write(Genel_Excel_Sayi, 3, ETHUP_RSI3)

    ETHUP_Coin_14 = driverETHUP.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div").text
    print("ETHUP Stochastic RSI(14) is: " + ETHUP_Coin_14)  
    ETHUP_RSI14 = float(ETHUP_Coin_14.replace("−", ""))
    ETHUP_Sheet.write(Genel_Excel_Sayi, 4, ETHUP_RSI14)

    ETHUP_Coin_Ichimoku = driverETHUP.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div").text
    ETHUP_Coin_Ichimoku = ETHUP_Coin_Ichimoku.replace("M", "")
    ETHUP_Coin_Ichimoku = ETHUP_Coin_Ichimoku.replace("K", "")
    print("ETHUP Ichimoku(Conversion Line) is: " + ETHUP_Coin_Ichimoku)
    ETHUP_Ichimoku_NUM = float(ETHUP_Coin_Ichimoku) #Ichimoku is Ichimoku now.
    ETHUP_Sheet.write(Genel_Excel_Sayi, 2, ETHUP_Ichimoku)

    ETHUP_Coin = driverETHUP.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[5]/div[2]").text
    #ETHUP_Coin = ETHUP_Coin.replace("USDT", "")
    #ETHUP_Coin = ETHUP_Coin[0:6]
    print("ETHUP Last Close Price is: " + ETHUP_Coin)
    ETHUP_LastPrice = float(ETHUP_Coin)
    ETHUP_Sheet.write(Genel_Excel_Sayi, 1, ETHUP_LastPrice)

    #ETHUP_Coin_MACD = driverETHUP.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div").text
    #ETHUP_MACD_NUM = float(ETHUP_Coin_MACD.replace("−", ""))

    #if "−" in ETHUP_Coin_MACD: #Ichimoku IS NEGATIVE CONDITION
    #    ETHUP_MACD = 0

    #elif "−" not in ETHUP_Coin_MACD: #Ichimoku IS POSITIVE CONDITION
    #    ETHUP_MACD = 1
        #ETHUP_Ichimoku_NUM = float(ETHUP_Coin_Ichimoku)

    RSI_DIFF = ETHUP_RSI14 - ETHUP_RSI3

    
    global ETHUP_AMOUNT #CHANGEABLE ACCORDING TO BALANCE. Bu amount alınan profitlere veya zararlara göre kendini updatelemeli.
    #ETHUP_AMOUNT_INT = math.floor(ETHUP_AMOUNT)
    #ETHUP_AMOUNT_DEC = round(float(ETHUP_AMOUNT),1)
    global ETHUP_AMOUNT_CONVERTED #= ETHUP_AMOUNT/ETHUP_LastPrice 
    global USDT_BUY_BALANCE
    #global ETHUP_Ichimoku_NUM

    action_chains = ActionChains(driverETHUP_BINANCE)

    
    #MACD MOMENTUM ÇEKİLECEK. ÖNCEKİ MOMENTUM İLE KARŞILAŞTIRILACAK. EĞER YENİ VALUE ÖNCEKİ VALUEDAN BÜYÜKSE BUY conditionina ekle.
    #ICHİMOKU Ichimoku YERİNE ÇEKİLECEK. ICHİMOKUNUN BASE LİNE I VE CONVERSİON LİNE I ÇEKİLECEK. ŞİMDİLİK base line kullılacak. PRİCE > ICHIMOKU cloud(base line) KRİTERLERE EKLENECEK.

    if (ETHUP_RSI3 >= ETHUP_RSI14 and ETHUP_LastPrice > ETHUP_Ichimoku_NUM and ETHUP_RSI3 > 0 and ETHUP_RSI14 > 0 and ETHUP_OnTrading == 0):
        #BUY COIN
        print("Buy")
        ETHUP_Sheet_Profit.write(Genel_Excel_Sayi_P_ETHUP, 1, str(ETHUP_LastPrice))
        ETHUP_Buy_Money = ETHUP_LastPrice
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        time.sleep(1)
        print(current_time)
        time.sleep(1)
        
        #ETHUP_MACD_MOMENTUM = ETHUP_Coin_MACD

        


        time.sleep(1)
        print("ETHUP")
        print("-----------------")

        #Place limit amount to buy coin.
        time.sleep(2)
        
        #driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[1]/div/span[2]").click() clicks the Market button.
        #time.sleep(2)

        #driverETHUP_BINANCE.find_element_by_id("FormRow-BUY-total").send_keys(str(float(ETHUP_AMOUNT)))
        #time.sleep(2)
        #driverETHUP_BINANCE.find_element_by_id("FormRow-BUY-total").send_keys(str(ETHUP_AMOUNT))
        #time.sleep(2)       
        driverETHUP_BINANCE.find_element_by_class_name("css-v6fymx").click() #buy 100% button
        time.sleep(3)
        ETHUP_AMOUNT = driverETHUP_BINANCE.find_element_by_id("FormRow-BUY-quantity").get_attribute("value") #to compare in the while statement
        time.sleep(1)
        ETHUP_AMOUNT_CONVERTED = float(ETHUP_AMOUNT)
        time.sleep(2)
        driverETHUP_BINANCE.find_element_by_id("orderformBuyBtn").click() #Rarely some other element below this one will receive the click, so another click command is added after to prevent any errors.
        time.sleep(3)

        y = 0
        while y < 2:
            y = y + 1
            
            if len(driverETHUP_BINANCE.find_elements_by_class_name("css-1j1sbq7")) > 0:  #checks to see if the %100 selection button is still selected, meaning the bot wont able to sell due to Insufficient Balance bug. If the itme exists, then it refreshes the page and tries buying again.
                driverETHUP_BINANCE.refresh()
                time.sleep(3)
                driverETHUP_BINANCE.find_element_by_class_name("css-15vandh").click() #finds an item to send keys to. For scrolling
                time.sleep(2)
                action_chains.send_keys(Keys.PAGE_DOWN).perform()        
                time.sleep(3)
                driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[1]/div[1]/div/span[2]").click() #Clicks the Market tab.
                time.sleep(3)
                driverETHUP_BINANCE.find_element_by_class_name("css-v6fymx").click() #BUY 100% BUTTON
                time.sleep(2)
                driverETHUP_BINANCE.find_element_by_id("orderformBuyBtn").click()              
                continue
            
            elif len(driverETHUP_BINANCE.find_elements_by_class_name("css-1j1sbq7")) == 0:
                break
            
            else:
                print("wtf")
                
        #driverETHUP_BINANCE.find_element_by_id("orderformBuyBtn").click()
        #time.sleep(2)
        #driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[3]/div[1]/form/div[3]/div/div[7]").click() buy 100% button
        #time.sleep(1)
        #driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[3]/div[1]/form/div[3]/div/div[3]").click() buy 0% button

        USDT_CURRENT_BALANCE = driverETHUP_BINANCE.find_element_by_class_name("css-rrzt34").text
        USDT_CURRENT_BALANCE_NUMBER = USDT_CURRENT_BALANCE.replace(" USDT", "")
        USDT_BUY_BALANCE = USDT_CURRENT_BALANCE_NUMBER
        time.sleep(10) #Grace period for the coin amount to be accumulated.

        now = datetime.now()
        ETHUP_Sheet_Profit.write(Genel_Excel_Sayi_P_ETHUP, 0, now.strftime("%d-%m-%y %H:%M:%S"))
        Genel_Excel_Sayi_P_ETHUP += 1
        ETHUP_OnTrading = 1

    else:
        #DOING NOTHING
        print("Waiting")
        

    if ((ETHUP_RSI3 < ETHUP_RSI14 and RSI_DIFF > 3.3 and ETHUP_OnTrading == 1) or (ETHUP_RSI3 == 0 and ETHUP_RSI14 == 0 and ETHUP_OnTrading == 1)):
        #SELL COIN
        print("Coin Sell")
        ETHUP_Sheet_Profit.write(Genel_Excel_Sayi_P_ETHUP, 1, str(ETHUP_LastPrice))
        ETHUP_Sel_Money = ETHUP_LastPrice
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        time.sleep(1)
        print(current_time)
        time.sleep(1)

        
        #driverETHUP_BINANCE.find_element_by_id("FormRow-SELL-total").send_keys(str(float(ETHUP_AMOUNT_SELL)))
        #time.sleep(2)
        driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/form/div[3]/div/div[7]").click() #SELL 100% BUTTON
        time.sleep(2)  

        coin_balance = driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/div/div[2]/span").text
        coin_balance_number = coin_balance.replace(" ETHUP", "") #SHOULD BE ETHUP TO BE REPLACED. 
        time.sleep(2)


        while float(coin_balance_number) != ETHUP_AMOUNT_CONVERTED * 1.5:

            if float(coin_balance_number) > (ETHUP_AMOUNT_CONVERTED * 0.98): #bazen buy order verildikten sonra binance hatalı alım yapıp, yaklaşık %0.3 civarı daha az mal alıyor. Bu yüzden ona göre if statement yazıldı.
            #if len(driverETHUP_BINANCE.find_elements_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/div/div[2]/span")) > 0: #as long as it can see the coin balance, it will click the sell button until it can actually sell.
                print("buM")
                driverETHUP_BINANCE.find_element_by_id("orderformSellBtn").click()
                time.sleep(3)
                break

            elif float(coin_balance_number) <= (ETHUP_AMOUNT_CONVERTED * 0.98):

                coin_balance = driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/div/div[2]/span").text
                coin_balance_number = coin_balance.replace(" ETHUP", "") #SHOULD BE ETHUP TO BE REPLACED. 
                time.sleep(3)                                                                          
                
                if float(coin_balance_number) > (ETHUP_AMOUNT_CONVERTED * 0.98): #to break if the accumulation for the coin is made within this if statement. Saliseler ile error vermesin diye yakalama kodu.
                    driverETHUP_BINANCE.find_element_by_id("orderformSellBtn").click()
                    time.sleep(3)
                    break
                
                elif float(coin_balance_number) <= (ETHUP_AMOUNT_CONVERTED * 0.98):
                    driverETHUP_BINANCE.find_element_by_id("orderformSellBtn").click() #code to keep clicking the sell button until the desired amount of coin is obtained.
                    time.sleep(5)
                    print("...")
                    time.sleep(2)
                    USDT_CURRENT_BALANCE = driverETHUP_BINANCE.find_element_by_class_name("css-rrzt34").text
                    USDT_CURRENT_BALANCE_NUMBER = USDT_CURRENT_BALANCE.replace(" USDT", "")
                    time.sleep(1)
                    if USDT_CURRENT_BALANCE_NUMBER != USDT_BUY_BALANCE:
                        break
                    elif USDT_CURRENT_BALANCE_NUMBER == USDT_BUY_BALANCE:
                        continue
                    else:
                        print("wtf len")

                else:
                    print("wtf man")
            
            
            else:
                print("wtf")
                time.sleep(2)
            

        time.sleep(3)

        #driverETHUP_BINANCE.find_element_by_id("orderformSellBtn").click()
        #time.sleep(2)
        #BURAYA IF STATEMENT I KOY: EĞER Kİ AŞAĞIDAKİ ELEMENTİ BULAMAZSA SAYFAYI REFRESHLETİP, AŞAĞI İNDİRİP TEKRAR MARKET TAB İNE GETİRT. DAHA SONRA TEKRAR %100 E BASTIRT, SAT VE AMOUNT BOX UNU SIFIRLA. 
        #ERROR VERMESİNİN NEDENİ INSUFFİCİENT FUNDS BUG OLUYO ELİMİZDE FUNDS OLSA BİLE.
        x = 0
        while x < 2:
            x = x + 1
            
            if len(driverETHUP_BINANCE.find_elements_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/form/div[3]/div/div[7]")) > 0:   
                #driverETHUP_BINANCE.find_element_by_xpath("(//div[@class='css-v6fymx'])[2]").click() #SELL %100 BUTTON
                #time.sleep(2) 
                #driverETHUP_BINANCE.find_element_by_xpath("(//div[@class='css-4l9ic'])[2]").click() #SELL 0% BUTTON 
                #time.sleep(2)
                break
            
            elif len(driverETHUP_BINANCE.find_elements_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/form/div[3]/div/div[7]")) == 0:
                driverETHUP_BINANCE.refresh()
                time.sleep(3)
                driverETHUP_BINANCE.find_element_by_class_name("css-15vandh").click() #finds an item to send keys to. For scrolling
                time.sleep(2)
                action_chains.send_keys(Keys.PAGE_DOWN).perform()        
                time.sleep(3)
                driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[1]/div[1]/div/span[2]").click() #Clicks the Market tab.
                time.sleep(3) 
                driverETHUP_BINANCE.find_element_by_xpath("/html/body/div[1]/div/div/div[7]/div/div[2]/div[2]/form/div[3]/div/div[7]").click() #SELL 100% BUTTON
                time.sleep(2)
                driverETHUP_BINANCE.find_element_by_id("orderformSellBtn").click()
                continue
            
            else:
                print("wtf")
        
        #time.sleep(3)
        #driverETHUP_BINANCE.find_element_by_xpath("(//div[@class='css-v6fymx'])[2]").click() #SELL 100% BUTTON
        #time.sleep(2)

        #driverETHUP_BINANCE.find_element_by_xpath("(//div[@class='css-4l9ic'])[2]").click() #SELL 0% BUTTON
        time.sleep(3)        
        
        # TAKE PROFIT YAPTIKTAN SONRA MOLA VERME KODU.
        #if ETHUP_LastPrice >= ETHUP_Buy_Money*1.08:
        #    time.sleep(6300)
        
        #else:
        #    pass
            
        

        #Excel shit
        now = datetime.now()
        ETHUP_Sheet_Profit.write(Genel_Excel_Sayi_P_ETHUP, 0, now.strftime("%d-%m-%y %H:%M:%S") )
        ETHUP_CASH = (((ETHUP_Sel_Money - ETHUP_Buy_Money) / ETHUP_Buy_Money) * 100 )+ ETHUP_CASH
        ETHUP_Sheet_Profit.write(Genel_Excel_Sayi_P_ETHUP, 2, "Cash: " + str(ETHUP_CASH))
        Genel_Excel_Sayi_P_ETHUP += 1
        ETHUP_OnTrading = 0
    
    else:
        #DOING NOTHING
        print("Waiting")


    if len(driverETHUP_BINANCE.find_elements_by_class_name("css-1j1sbq7")) > 0:
        driverETHUP_BINANCE.find_element_by_class_name("css-4l9ic").click() #clicks the 0% button to reset the bar.
        time.sleep(2)
    
    else:
        pass
    
    time.sleep(1)
    print( "----ETHUP: " + str(ETHUP_CASH) + "$ ----")

    
    Genel_Excel_Sayi += 1

    # per day 4320
    # per hour 180
    if Genel_Excel_Sayi > 180:
        ETHUP_Workbook.close()
        Excel_Versiyon += 1
        Genel_Excel_Sayi = 1
        Genel_Excel_Sayi_P_ETHUP = 1
        Genel_Excel_Sayi_P_OMG = 1
        Genel_Excel_Sayi_P_ATOM = 1
        ExcelFileCreate()

    
    Timer(14400, DataCatcher).start() 
    

ExcelFileCreate()
CoinData_Website()
DataCatcher()