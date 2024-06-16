from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service("C:/Users/pc/Desktop/chrome.exe")

webdriver.Chrome(service=s) 