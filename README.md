# get_fide_rating_with_scrapy
get fide player info from https://ratings.fide.com/profile/XXXXXXX page using scrapy

This is working on Mon Dec 30 01:38:00 PM CET 2024
but as soon as the fide modifies its web page you need to find the new xpaths with the information.

Before running this you need to install the python module "scrapy" (```pip install scrapy```).

# how to run the program
* edit the file ```FIDE/spiders/Fide.py``` and paste the Fide Ids you want to search (variable self.fide_ids)
* then execute ```scrapy crawl fide_spider -O fide_rating.csv``` 
* the results are in the new file ```fide_rating.csv``` and they look as:

```
name,std_rating,rapid_rating,blitz_rating,fide_id
"Gomez Carreno, Martin",2220,2091,2111,
"Martinez Fernandez, Raul",2200,2069,2138,
"Hernandez Ramos, David",2115,2138,1972,
```
