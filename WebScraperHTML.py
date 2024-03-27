#This is a webscraper where it gets information for you from any HTML doc you want

#first pip install beautifulsoup4

#import from beautifulsoup4
from bs4 import BeautifulSoup

#how to read into an HTML File and make sure it is in the same folder

with open("ScraperHTML.html", "r") as f:#first open the file and read into the file then set it as f
    #set the doc variable and beautiful soup then put file name then html parser so we can read it
    doc = BeautifulSoup(f, "html.parser")

#print the doc to see all the contens in the terminal
#print(doc)


#if you want see it in an organized way then use this command and it will put it all in order
#print(doc.prettify())


#if you are looking for certain information, you can do that by finding it using the tag name
# this one will only print the first one with the tag not all of them, the one that has all of them is later on
#so we are doing the title tag 
#tag = doc.title 
#print the tag
#print(tag)



#if you want to get the string inside the tag then you can do this
#tag = doc.title
#after you print the tag add the .string so you can can access the tag string
#print(tag.string)



#if you want to modify the tags
#tag = doc.title
#tag.string = "hello" #take the tag.string and make the string = to anything 
#print(tag)#print the tag
#after doing this and you print the full doc again it will change the first title tag to hello
#print(doc)



#if you are trying to find all the speciifc types of tags do this
#right here use find all and then for the tag we are looking for we did p
#tags = doc.find_all("p")
#then print it out, it prints all the p tags and all the strings inside
#print(tags)


#how to access the nested tags inside the tag
#tags = doc.find_all("p")[0]#leave it at index zero because we want to access the very first tag
#print(tags.find_all("b"))#then to the same find all, and leave the b tag which will give all the oens you want
























