from bs4 import BeautifulSoup
def has_current_platform_from_html(html):


    soup = BeautifulSoup(html, 'html.parser')
    char_elements = soup.find_all('div', class_='char-info')
    hasCurrentPlatform = " "
    for char_elem in char_elements:
        elem = char_elem.contents[5].contents[1]
        money = elem.string[1::]
        money = money.replace('K', '')
        money = money.replace('M', '')
        if float(money) > 0:
            print(money)
            hasCurrentPlatform = "YES"
            return hasCurrentPlatform
    return hasCurrentPlatform

