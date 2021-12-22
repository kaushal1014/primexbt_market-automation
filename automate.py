import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

#Choice
question=input("Would you like to sell or buy orders:")
# LOG IN
driver = webdriver.Chrome(executable_path="C:\\pythonProjects\\spotify on loop player\\chromedriver.exe")
action = ActionChains(driver)
driver.maximize_window()
driver.get("https://primexbt.com/my/margin/btc82907/trade")
email_input = driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys('bobinsky51@gmail.com')
password_input = driver.find_element_by_xpath("//input[@id='mat-input-1']").send_keys('Abc123!!')
login_button = driver.find_element_by_xpath("/html/body/prm-root/id-id/div/div/ng-component/form/id-card-actions/button")
login_button.click()
print("Login successful")
time.sleep(10)


try:
    pop_up= driver.find_element_by_xpath('//*[@id="mat-dialog-title-0"]/button')
    pop_up.click()
except NoSuchElementException:
    pass
time.sleep(10)

# switch frame
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/prm-root/prm-my/prm-iframe-trade/div/div/iframe"))



if "buy" in question:
    #BUY GRID
    #Here is where I will be submitting the initial market buy order followed by limit buy orders
    buy_order= driver.find_element_by_xpath('/html/body/main/section/section/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/button[2]')
    buy_order.click()                       

    time.sleep(5)
    place_stop_loss = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[3]/div[1]/div/span')
    place_stop_loss.click()

    stop_loss_price_checkbox= driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[3]/div[2]/div[1]/span/label/span[1]').click()
    stop_loss_price = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').clear()
    time.sleep(2)
    stop_loss_price2 = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').send_keys("45000")
    time.sleep(3)
    send_order= driver.find_element_by_xpath('/html/body/section/div/footer/div[1]/button[2]').click()
    time.sleep(3)
    confirm_order= driver.find_element_by_xpath('/html/body/section[2]/div/footer/div[1]/button[2]').click()
    print("Initial buy order bought")
    time.sleep(5)
    
    #fill price of the initial buy order
    fill_price=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/table/tbody/tr/td[4]/span/span/span').text
    float_fill_price=float(fill_price.replace(',' , ''))


    for i in range(1):
        count=2
        count2=3
        buy_order= driver.find_element_by_xpath('/html/body/main/section/section/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/button[2]')
        buy_order.click()

        #drop down to select stop buy order
        try:
            dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
            time.sleep(5)
            dropdown.click()
            
        except ElementNotInteractableException:
            try:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/div')
                time.sleep(5)
                dropdown.click()
            except ElementNotInteractableException:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                time.sleep(5)
                dropdown.click()

        time.sleep(5)
        stop_market = driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]').click()

        stop_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').clear()
        
        time.sleep(3)
        price_to_be_sent=float_fill_price+10.00
        stop_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').send_keys(str(price_to_be_sent))
        try:
            # check if red error box to switch into limit order option
            time.sleep(5)
            error = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[2]/div/div').text

            if "Entry Price you set must be higher or equal" in error:
                #drop down to select limit buy order
                try:
                    dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
                    time.sleep(5)
                    dropdown.click()
                    
                except ElementNotInteractableException:
                    dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                    time.sleep(5)
                    dropdown.click()
                time.sleep(5)
                limit_order= driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[2]').click()
                time.sleep(7)
            # clear previous variable
                del error
                error = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[2]/div/div').text
                
                if "Entry Price you set must be lower or equal" in error:
                    print("Skipping order 1")
                    closebutton= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/header/button').click()
                    time.sleep(3)
                    break
                else:
                    pass
            else:
                pass
        except NoSuchElementException:
            pass

        place_stop_loss = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[1]/div/span')
                                            
        place_stop_loss.click()

        stop_loss_price_checkbox= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[1]/span/label/span[1]').click()
                                                                
        stop_loss_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').clear()
        time.sleep(2)
        stop_loss_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').send_keys("45000")
        time.sleep(3)
        send_order= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[1]/button[2]').click()
        time.sleep(3)
        confirm_order= driver.find_element_by_xpath(f'/html/body/section[{count2}]/div/footer/div[1]/button[2]').click()
        print("Order buy 1 done")

    

    for i in range(1):
        count=3
        count2=4
        buy_order= driver.find_element_by_xpath('/html/body/main/section/section/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/button[2]')
        buy_order.click()

        try:
            dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
            time.sleep(5)
            dropdown.click()
            
        except ElementNotInteractableException:
            try:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/div')
                time.sleep(5)
                dropdown.click()
            except ElementNotInteractableException:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                time.sleep(5)
                dropdown.click()

        time.sleep(5)
        stop_market = driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]').click()

        stop_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').clear()
        
        time.sleep(3)
        price_to_be_sent=float_fill_price+20.00
        stop_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').send_keys(str(price_to_be_sent))
        try:
            time.sleep(5)
            error = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[2]/div/div').text
            if "Entry Price you set must be higher or equal" in error:
                try:
                    dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
                    time.sleep(5)
                    dropdown.click()
                    
                except ElementNotInteractableException:
                    dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                    time.sleep(5)
                    dropdown.click()
                time.sleep(5)
                limit_order= driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[2]').click()
                time.sleep(7)

                del error
                error = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[2]/div/div').text
                
                if "Entry Price you set must be lower or equal" in error:
                    print("Skipping order 2")
                    closebutton= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/header/button').click()
                    time.sleep(3)
                    break
                else:
                    pass
            else:
                pass
        except NoSuchElementException:
            pass

        place_stop_loss = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[1]/div/span')
                                            
        place_stop_loss.click()

        stop_loss_price_checkbox= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[1]/span/label/span[1]').click()
                                                                
        stop_loss_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').clear()
        time.sleep(2)
        stop_loss_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').send_keys("45000")
        time.sleep(3)
        send_order= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[1]/button[2]').click()
        time.sleep(3)
        confirm_order= driver.find_element_by_xpath(f'/html/body/section[{count2}]/div/footer/div[1]/button[2]').click()
        print("Order buy 2 done")


    
    for i in range(1):
        count=4
        count2=5
        buy_order= driver.find_element_by_xpath('/html/body/main/section/section/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/button[2]')
        buy_order.click()

        try:
            dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
            time.sleep(5)
            dropdown.click()
            
        except ElementNotInteractableException:
            try:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/div')
                time.sleep(5)
                dropdown.click()
            except ElementNotInteractableException:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                time.sleep(5)
                dropdown.click()

        time.sleep(5)
        stop_market = driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]').click()

        stop_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').clear()
        
        time.sleep(3)
        price_to_be_sent=float_fill_price+30.00
        stop_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').send_keys(str(price_to_be_sent))
        try:
            time.sleep(5)
            error = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[2]/div/div').text

            if "Entry Price you set must be higher or equal" in error:
                try:
                    dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
                    time.sleep(5)
                    dropdown.click()
                    
                except ElementNotInteractableException:
                    dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                    time.sleep(5)
                    dropdown.click()
                time.sleep(5)
                limit_order= driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[2]').click()
                time.sleep(7)

                del error
                error = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[2]/div/div').text
                
                if "Entry Price you set must be lower or equal" in error:
                    print("Skipping order 3")
                    closebutton= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/header/button').click()
                    time.sleep(3)
                    break
                else:
                    pass
            else:
                pass
        except NoSuchElementException:
            pass

        place_stop_loss = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[1]/div/span')
                                            
        place_stop_loss.click()

        stop_loss_price_checkbox= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[1]/span/label/span[1]').click()
                                                                
        stop_loss_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').clear()
        time.sleep(2)
        stop_loss_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').send_keys("45000")
        time.sleep(3)
        send_order= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[1]/button[2]').click()
        time.sleep(3)
        confirm_order= driver.find_element_by_xpath(f'/html/body/section[{count2}]/div/footer/div[1]/button[2]').click()
        print("Order buy 3 done")


    
if "sell" in question:
    sell_order= driver.find_element_by_xpath("/html/body/main/section/section/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/button[1]").click()
    time.sleep(5)
    place_stop_loss = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[3]/div[1]/div/span')
    place_stop_loss.click()

    stop_loss_price_checkbox= driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[3]/div[2]/div[1]/span/label/span[1]').click()
    stop_loss_price = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').clear()
    time.sleep(2)
    stop_loss_price2 = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').send_keys("50000")
    time.sleep(5)
    send_order= driver.find_element_by_xpath('/html/body/section/div/footer/div[1]/button[2]').click()
    time.sleep(3)
    confirm_order= driver.find_element_by_xpath('/html/body/section[2]/div/footer/div[1]/button[2]').click()
    print("Initial sell order bought")
    time.sleep(5)
    fill_price=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/table/tbody/tr/td[4]/span/span/span').text
    float_fill_price=float(fill_price.replace(',' , ''))

    

    for i in range(1):
        count=2
        count2=3
        sell_order= driver.find_element_by_xpath("/html/body/main/section/section/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/button[1]").click()
        time.sleep(5)

        try:
            dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
            time.sleep(5)
            dropdown.click()
            
        except ElementNotInteractableException:
            try:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/div')
                time.sleep(5)
                dropdown.click()
            except ElementNotInteractableException:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                time.sleep(5)
                dropdown.click()

        time.sleep(3)
        stop_market = driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]').click()

        stop_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').clear()
        
        time.sleep(3)
        price_to_be_sent=float_fill_price-10.00
        stop_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').send_keys(str(price_to_be_sent))


        place_stop_loss = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[1]/div/span')
                                            
        place_stop_loss.click()

        stop_loss_price_checkbox= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[1]/span/label/span[1]').click()
                                                                
        stop_loss_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').clear()
        time.sleep(2)
        stop_loss_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').send_keys("50000")
        time.sleep(3)
        send_order= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[1]/button[2]').click()
        time.sleep(3)
        confirm_order= driver.find_element_by_xpath(f'/html/body/section[{count2}]/div/footer/div[1]/button[2]').click()
        print(f"Order sell 1 done")

            

        

    for i in range(1):
        count=3
        count2=4
        sell_order= driver.find_element_by_xpath("/html/body/main/section/section/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/button[1]").click()
        time.sleep(5)

        try:
            dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
            time.sleep(5)
            dropdown.click()
            
        except ElementNotInteractableException:
            try:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/div')
                time.sleep(5)
                dropdown.click()
            except ElementNotInteractableException:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                time.sleep(5)
                dropdown.click()

        time.sleep(3)
        stop_market = driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]').click()

        stop_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').clear()
        
        time.sleep(3)
        price_to_be_sent=float_fill_price-20.00
        stop_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').send_keys(str(price_to_be_sent))


        place_stop_loss = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[1]/div/span')
                                            
        place_stop_loss.click()

        stop_loss_price_checkbox= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[1]/span/label/span[1]').click()
                                                                
        stop_loss_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').clear()
        time.sleep(2)
        stop_loss_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').send_keys("50000")
        time.sleep(3)
        send_order= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[1]/button[2]').click()
        time.sleep(3)
        confirm_order= driver.find_element_by_xpath(f'/html/body/section[{count2}]/div/footer/div[1]/button[2]').click()
        print("Order sell 2 done")

    for i in range(1):
        count=4
        count2=5
        sell_order= driver.find_element_by_xpath("/html/body/main/section/section/div/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/button[1]").click()
        time.sleep(5)

        try:
            dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div')
            time.sleep(5)
            dropdown.click()
            
        except ElementNotInteractableException:
            try:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/div')
                time.sleep(5)
                dropdown.click()
            except ElementNotInteractableException:
                dropdown = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[1]/div[2]/div[1]/span[2]/div/select')
                time.sleep(5)
                dropdown.click()

        time.sleep(3)
        stop_market = driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]').click()

        stop_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').clear()
        
        time.sleep(3)
        price_to_be_sent=float_fill_price-30.00
        stop_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[2]/div[1]/div[2]/span[2]/span/span/input').send_keys(str(price_to_be_sent))


        place_stop_loss = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[1]/div/span')
                                            
        place_stop_loss.click()

        stop_loss_price_checkbox= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[1]/span/label/span[1]').click()
                                                                
        stop_loss_price = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').clear()
        time.sleep(2)
        stop_loss_price2 = driver.find_element_by_xpath(f'/html/body/section[{count}]/div/div/div[2]/div[3]/div[2]/div[2]/span[2]/span/span/input').send_keys("50000")
        time.sleep(3)
        send_order= driver.find_element_by_xpath(f'/html/body/section[{count}]/div/footer/div[1]/button[2]').click()
        time.sleep(3)
        confirm_order= driver.find_element_by_xpath(f'/html/body/section[{count2}]/div/footer/div[1]/button[2]').click()
        print("Order sell 3 done")
    driver.close()

