from bs4 import BeautifulSoup

with open( 'Web_Scrapping\home.html' ,'r') as html_file :
    content = html_file.read()
    # print(content)


    soup = BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    # tags = soup.find('h1')
    # tags = soup.find_all('h1')
    # print(tags)


    # h1_tags = soup.find_all('h1')
    # for i in h1_tags:
    #     print(i.text)
    

    # div_card = soup.find_all('div',class_="card")
    # for i in div_card:
    #     print(i)
    #     print(i.text)
    #     print(i.a.text)

    