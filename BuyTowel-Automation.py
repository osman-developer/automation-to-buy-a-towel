from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
# define urls
mainUrl='https://www.walmart.com/'
urlShop='https://www.walmart.com/cp/auto/91083?athcpid=9a49d87e-f003-4ec2-93c8-6a8efe03c787&athpgid=athenaHomepage&athznid=athenaModuleZone&athmtid=AthenaFeaturedCategory&athtvid=1&athena=true'
urlCateg='https://www.walmart.com/browse/spring-cleaning/0/0/?_refineresult=true&_be_shelf_id=3726918&search_sort=100&facet=shelf_id:3726918&povid=91083+%7C+2020-04-21+%7C+spring%20cleaning'
urlItem='https://www.walmart.com/ip/Chemical-Guys-MIC36503-Workhorse-XL-Yellow-Professional-Grade-Microfiber-Towel-24-x-16-Interior-3-Pack/408912159'

#define the strings to fill the form
firstnameStr = 'Maria'
lastnameStr = ' J Horowitz'
streeStr = '4810  Ralph Drive'
phoneStr = '440-301-6157'
cityStr = 'Warrensville Heights'
emailStr = '3vnnwouw8e8@temporary-mail.net'
stateStr = 'Ohio'
zipcodeStr = '44128'
creditStr = '378282246310005'
monthStr = '11'
yearStr = '20'
cvvStr = '1111'
#open the window in max size
browser = webdriver.Chrome()

#navigation
browser.maximize_window()
browser.get(mainUrl)
browser.get(urlShop)
browser.get(urlCateg)
browser.get(urlItem)

# checks for the span of text 'add to cart' and clicks on it
wait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add to cart']"))).click()
# checks for the span of text 'check out' and clicks on it
wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Check out']"))).click()
# checks for the span of text 'continue without account' and clicks on it

wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue without account']"))).click()
# checks for the span of text 'continue' and clicks on it
wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue']"))).click()

time.sleep(2)
#filling the form 
firstname = browser.find_element_by_id("firstName")
firstname.send_keys(firstnameStr)

lastname = browser.find_element_by_id('lastName')
lastname.send_keys(lastnameStr)

street = browser.find_element_by_id('addressLineOne')
street.send_keys(streeStr)

phone = browser.find_element_by_id('phone')
phone.send_keys(phoneStr)

#clearing the city text area first because it has a value
city = browser.find_element_by_id('city').clear()
city = browser.find_element_by_id('city')
city.send_keys(streeStr)

email =browser.find_element_by_id('email')
email.send_keys(emailStr)

state = browser.find_element_by_id('state')
state.send_keys(stateStr)

#clearing the city text area first because it has a value
zipcode = browser.find_element_by_id('postalCode').clear()
time.sleep(1)

zipcode = browser.find_element_by_id('postalCode')
zipcode.send_keys(zipcodeStr)

#searching for a span containing 'continue'
wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue']"))).click()
time.sleep(2)
wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,  "/html/body/div[1]/div/div[3]/div[2]/div/div/div/div[6]/div/button[1]/span"))).click()

# Network_Mode = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/div/div/div[6]/div/button[1]/span")))
# Network_Mode.click()
time.sleep(5)
browser.execute_script("window.scrollTo(0, 400)") 

credit = browser.find_element_by_id('creditCard')
credit.send_keys(creditStr)

month = browser.find_element_by_id('month-chooser')
month.send_keys(monthStr)

year = browser.find_element_by_id('year-chooser')
year.send_keys(yearStr)

cvv = browser.find_element_by_id('cvv')
cvv.send_keys(cvvStr)

wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Review your order']"))).click()
time.sleep(8)
wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Place order']"))).click()
