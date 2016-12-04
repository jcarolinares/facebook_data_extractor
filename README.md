# Facebook Data Extractor
A Python parser that extracts the info you want from an official downloaded facebook archive

Made by Julián Caro Linares

* email: jcarolinares@gmail.com
* twitter: @jcarolinares

#How to use
Python version and libraries:
* Python 3
* BeautifulSoup

First of all, if you don't have Python 3.X on your computer, you'll need to install it.

<a href="https://www.python.org/downloads/">Official Python 3 page</a>

You'll also need the library BeautifulSoup:

$ apt-get install python-bs4

Or

$ pip install beautifulsoup4

<a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup">More info</a>

After that, you'll need to download your Facebook data.

Follow the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup"> official Facebook guide</a>, section "Download info":

"Download Your Info: This includes a lot of the same information available to you in your account and activity log, including your Timeline info, posts you have shared, messages, photos and more. Additionally, it includes information that is not available simply by logging into your account, like the ads you have clicked on, data like the IP addresses that are logged when you log into or out of Facebook, and more. To download your information, go to your Settings and click Download a copy of your Facebook data."


You'll probably have to wait an email from Faccebook with the data link.

When you had downloaded your facebook data, extract the file in the same folder of this program.

Now executes the python program "facebook_data_extractor.py" using python3:

* Your facebook name ID is the name that comes in your facebook data folder:
  In the case "facebook-yournamessurnames" you should write "yournamessurnames"

* Write the keywords for your search separated with commas, for example, "train,happy,dog"

If the program founds comments that match these keywords it'll show them in the terminal.

You also have a new file called "timeline_results-yourkeywords.txt" where you have all the search results with their date.



=============

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Facebook data extractor</span> por <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Julián Caro Linares</span> licensed by <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br /><br />
