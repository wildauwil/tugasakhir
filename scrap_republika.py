import requests
from bs4 import BeautifulSoup
import pandas as pd


class scrap_republika:

	main_url = "https://republika.co.id/index/politik/2019/01/01"
	result = requests.get(main_url)
	result.text[:1000]

	soup = BeautifulSoup(result.text, 'html.parser')
	print(soup.prettify()[:1000])

	def getAndParseURL(url):
		result = requests.get(url)
		soup = BeautifulSoup(result.text, 'html.parser')
		return(soup)

	soup.find("div", class_ = "txt_subkanal txt_index")
	soup.find("div", class_ = "txt_subkanal txt_index").h2.a

	containers = soup.find_all("div", class_ = "txt_subkanal txt_index")
	pages = soup.find("div", class_ = "pagination")
	   
	print(type(containers))
	print(len(containers))

	main_page_politik_urls = []
	for line in containers:
	    #print(c)
	    x = line.find('h2').a
	    a_link = x.get('href')
	    #print(a_link)
	    main_page_politik_urls.append(a_link)
	    
	if soup.find("div", class_ = "pagination"):
	    #a = soup.find("div", class_ = "pagination")
	    y = pages.find('a')
	    link_page = y.get('href')
	    print(link_page)
	    soup_page = getAndParseURL(link_page)

	    containers = soup_page.find_all("div", class_ = "txt_subkanal txt_index")
	    print(len(containers))

	    for c in containers:
	        #print(c)
	        x = c.find('h2').a
	        a_link = x.get('href')
	        #print(a_link)
	        main_page_politik_urls.append(a_link)
	    
	    
	main_page_politik_urls[:42]

	print(str(len(main_page_politik_urls)) + " fetched products URLs")
	print("One example:")
	main_page_politik_urls[0]


	def getPolitikURLs(url):
		result = requests.get(url)
		soup = BeautifulSoup(result.text, 'html.parser')

		pages = soup.find("div", class_ = "pagination")

	    # remove the index.html part of the base url before returning the results
		return([x.h2.a.get('href') for x in soup.findAll("div", class_ = "txt_subkanal txt_index")])

		if soup.find("div", class_ = "pagination"):
	        #a = soup.find("div", class_ = "pagination")
			y = pages.find('a')
			link_page = y.get('href')
	        
			soup_page = getAndParseURL(linkku)
			return([x.h2.a.get('href') for x in soup_page.findAll("div", class_ = "txt_subkanal txt_index")])
    
    

	#str(int(pages_urls[-1].split("/")[6]) + 1 )
	pages_urls = []
	tahun = ["2019"]
	bulan = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
	tgl = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
	new_page = "https://republika.co.id/index/politik/2019/01/01"

	#while requests.get(new_page).status_code == 200:
	for y in bulan:
	    for x in tgl:
	            pages_urls.append(new_page)
	            new_page = pages_urls[-1].split("/")[0] + "/" + pages_urls[-1].split("/")[1] + "/" + pages_urls[-1].split("/")[2] + "/" + pages_urls[-1].split("/")[3] + "/" + "politik/" + '2019/'+ y + "/" + x 
	    
	    
	    #new_page = pages_urls[-1].split("/")[0] + "/" + pages_urls[-1].split("/")[1] + "/" + pages_urls[-1].split("/")[2] + "/" + pages_urls[-1].split("/")[3] + "/" + pages_urls[-1].split("/")[4] + "/" + pages_urls[-1].split("/")[5] + "/" + str(x) + "/" + pages_urls[-1].split("/")[7]
	    
	print(str(len(pages_urls)) + " fetched URLs")
	print("Some examples:")
	pages_urls[0:10]

	politikURLs = []
	for page in pages_urls:
  	  	politikURLs.extend(getPolitikURLs(page))

	print(str(len(politikURLs)) + " fetched URLs")
	print("Some examples:")
	politikURLs[3222:3229]

	names = []
	deskripsi = []
	tgl = []
	link_url = []
	#categories = []

	filename = "corpusrepublika.csv"
	f = open(filename, "w", encoding="utf-8")

	headers = "title` deskripsi` date"
	f.write(headers)
	
	# scrape data for every politik URL: this may take some time
	for url in politikURLs:
		soup = getAndParseURL(url)
	        
	        # product name
		title_box = soup.find('div', attrs={'class':'wrap_detail'}).h1
		title = title_box.text
	        #print (title)
		names.append(title)
	        
	        # deskripsi
		des_box = soup.find('div', attrs={'class':'artikel'})
		tes = des_box.findAll('p')
		des = ''
		for x in tes:
			des = des + x.text
		deskripsi.append(des)
	        
	        # tanggal published
		tgl_box = soup.find('div', attrs={'class':'date_detail'})
		tgl_p = tgl_box.text
		tgl.append(tgl_p)

		print("title: " + title)
		print("deskripsi: " + des)
		print("date: " + tgl_p)

		f.write("\n" + title.replace("\r\n\t\t\t\t\t\t\t", "") + "`" + des + "`" + tgl_p.replace(",", "|") )
	f.close()

	scraped_data = pd.DataFrame({'name': names, 'deskripsi' : des, 'tanggal' : tgl} )
	scraped_data.head(900)
        



