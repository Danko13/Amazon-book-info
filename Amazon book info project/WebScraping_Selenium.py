from selenium import webdriver

textsearch = input('Enter your desired product: ')

# opening the browser
browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
browser.get("http://www.amazon.com/")

# find the search box and send_keys with textsearch
search = browser.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
search.send_keys(textsearch)
search.find_element_by_xpath("//input[@class='nav-input']").click()

# find the first product and clicking on it
first = browser.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/h2')
first.click()

# extract product data
name = browser.find_element_by_xpath('//*[@id="productTitle"]').text
author = browser.find_element_by_xpath('//*[@id="bylineInfo"]/span/span[1]/a[1]').text
price = browser.find_element_by_xpath('//*[@id="buyNewSection"]/h5/div/div[2]/div/span[2]').text

print (name)
print (author)
print (price)

browser.quit()