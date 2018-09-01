from bs4 import BeautifulSoup
import requests as rq

print("This tool for getting data from any website")
print()
print('''1)Only Source Code       2)Find for specific tag
3) Find for tag's element text (ex: href="/action_page.php"
                                     output:/action_page.php)''')
print()

print('ok')

option = input("Select for option >>>")
url_input_first = input("Is your site 1)HTTP or 2)HTTPS >>>")
url_input = input("Please enter your website (ex:domain.com) >>>")


def http():
  myurl = rq.get("http://" + url_input)
  if (option == "1"):
    myurl.content
    soup = BeautifulSoup(myurl.content)
    print(soup.prettify())
  elif (option == "2"):
    tag_name = input("Please Enter Tag (ex: h1, p, a):")
    myurl.content
    soup = BeautifulSoup(myurl.content)
    linkler = soup.find_all(tag_name)
    for link in linkler:
      print(link)
  elif (option == "3"):
    tag_name_forelement = input("Please Enter Tag Name:")
    element = input("Please Enter Element:")
    myurl.content
    linkler = soup.find_all(tag_name_forelement)
    for link in linkler:
      soup = BeautifulSoup(myurl.content)
      print(link.get(element))

def https():
  myurl = rq.get("https://" + url_input)
  if (option == "1"):
    myurl.content
    soup = BeautifulSoup(myurl.content)
    print(soup.prettify())
  elif (option == "2"):
    tag_name = input("Please Enter Tag (ex: h1, p, a):")
    myurl.content
    soup = BeautifulSoup(myurl.content)
    linkler = soup.find_all(tag_name)
    for link in linkler:
      print(link)
  elif (option == "3"):
    tag_name_forelement = input("Please Enter Tag Name:")
    element = input("Please Enter Element:")
    myurl.content
    soup = BeautifulSoup(myurl.content)
    linkler = soup.find_all(tag_name_forelement)
    for link in linkler:
      print(link.get(element))

def error():
  print("An Error Occured. Please try again!!!")

if (url_input_first == "1"):
  http()
if (url_input_first == "2"):
  https()
else:
  print()
