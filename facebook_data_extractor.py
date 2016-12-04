#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Facebook data extractor

A Python parser that extracts the info that you want from an official downloaded facebook archive

Made by Julián Caro Linares

email: jcarolinares@gmail.com
twitter: @jcarolinares

License: CC-BY-SA

'''

#Libraries
from bs4 import BeautifulSoup
import requests

#Global variables
user=""
search_keywords=""
info_type={"ads":"ads.htm","contacs":"contact_info.htm","events":"events.htm","friends":"friends.htm","messages":"messages.htm","mobile_devices":"mobile_devices.htm","photos":"photos.htm","places":"places.htm","pokes":"pokes.htm","security":"security.htm","surveys":"survey_responses.htm","synced_photos":"synced_photos.htm","timeline":"timeline.htm","videos":"videos.htm"}

#Functions
class comment:
    def new(self,user,date,comment,keywords):
        self.user=str(user)
        self.date=str(date)
        self.comment=str(comment)
        self.keywords=str(keywords)

    def print_comment():
        print("\nDate: \n")
        print(self.date)
        print("Comment: \n")
        print(self.comment)

    def get_user(self):
        return self.user
    def get_date(self):
        return self.date
    def get_comment(self):
        return self.comment
    def get_keywords(self):
        return self.keywords

def timeline_parser():
    global user
    comments_counter=0
    search_keywords=input("\n\nInsert your search keywords separated with commas:\n")
    search_keywords=search_keywords.lower().split(",")

    file_route='./facebook-'+user+'/html/'+info_type["timeline"]

    #Data parser
    #Extracting the file
    soup=BeautifulSoup(open(file_route),'lxml')

    comments_text=soup.find_all('div',class_="comment") #It's only takes real comments, not share or likes. To take this raw info, use the dates_text instead
    dates_text=soup.find_all('div',class_="meta") #Used for taking addional info like likes, shared links or others. No formated info


    #Making the file name
    file_name="timeline_results"
    for keyword in search_keywords:
        file_name=file_name+"-"+keyword

    file_name=file_name+".txt"
    f=open(file_name,"a")

    #Looking for the desired comments
    for index in range(len(comments_text)):

        for keyword in search_keywords:
            if(keyword in comments_text[index].get_text().lower()):
                print("\n\n"+comments_text[index].find_previous_sibling().get_text())#Takes the date of the comment
                print (comments_text[index].get_text())
                f.write("\n\n"+comments_text[index].find_previous_sibling().get_text())
                f.write("\n\n"+comments_text[index].get_text()+"\n\n")
                comments_counter=comments_counter+1
                break


    #Used for taking addional info like "likes", shared links and others. Not formated info, putted at the end of the file results
    print("\n\n--- ADDITIONAL INFO, SHARES AND LIKES ---\n")
    f.write("\n\n--- ADDITIONAL INFO, SHARES AND LIKES ---\n")
    for date in dates_text:
        for keyword in search_keywords:
            if(keyword in date.next_element.next_element):
                print("\n"+date.get_text())
                print("\n"+date.next_element.next_element)
                f.write("\n\n"+date.get_text())
                f.write("\n\n"+date.next_element.next_element+"\n\n")
                comments_counter=comments_counter+1
                break

    f.close()

    #End of the program
    if(comments_counter>0):
        print("\n\n---COMMENTS FOUND: ", comments_counter," ---\n")
    else:
        print("\n\n---NO COMMENTS FOUND---")

    #Facebook timeline page syntax
    #print("\nYou published "+str(len(comments_text))+" comments in your timeline")

    #"<div class="meta">Friday, 2 December 2016 at 15:33 UTC+01</div>"
    #<div class="comment">This is a comment</div>

#Main execution
def main():
    global user
    user=input("\n\nInsert your facebook name ID (namesurnames):\n")

    timeline_parser()#searchs and extracts data from the timeline.htm data


if __name__ == "__main__":
 main()
