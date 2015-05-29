
#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

def search_lyrics(artist, name):
	search = artist + " " + name # what to enter in the search bar

	display = Display(visible=0, size=(800, 600))
	display.start()

	driver = webdriver.Firefox()
	driver.get("http://azlyrics.com/")	# navigte to azlyrics
	search_bar = driver.find_element_by_name("q")
	search_bar.send_keys(search + Keys.RETURN)

	link = driver.find_element_by_xpath("//td[@class='text-left visitedlyr']/a[1]").get_attribute('href') 	# first search result
	driver.get(link)

 	# eventually add a statement here that checks if the song title matches, if no go back and select next link


	# # i'm cheating here

	hacky_text = driver.find_element_by_css_selector('.col-xs-12.col-lg-8.text-center').text

	driver.quit()
	display.stop()

	return hacky_text


print search_lyrics("", "hello seattle")