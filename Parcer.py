import requests
from bs4 import BeautifulSoup


# The parsing of "tablitsi_dozodnosti_liniy_icn" link. Returns list of lists, each including one row of initial table
def tables_parse():
    table_dozodnosti_liniy_content = []
    page = requests.get("https://usicn.com/ru/tablitsi_dozodnosti_liniy_icn/")
    page_content = BeautifulSoup(page.content, 'html.parser')

    for line in page_content.find_all('tr'):
        line_in_table_content = []
        for cell in line.find_all('td'):
            if cell.string is not None:
                line_in_table_content.append(cell.string)
            else:
                for span in cell.find_all('span'):
                    line_in_table_content.append(span.text.strip())
        table_dozodnosti_liniy_content.append(line_in_table_content)
    # Removal of excess cells infront
    del table_dozodnosti_liniy_content[0]
    return table_dozodnosti_liniy_content


# The parsing of "linii_icn_grafiki_i_tseni" link. Returns list of lists, each including one row of initial table
def costs_parse():
    table_grafiki_i_tseni_content = []
    page = requests.get("https://usicn.com/ru/linii_icn_grafiki_i_tseni/")
    page_content = BeautifulSoup(page.content, 'html.parser')

    for line in page_content.find_all('tr'):
        line_in_table_content = []
        for cell in line.find_all('td'):
            if cell.string is not None:
                line_in_table_content.append(cell.text.strip('\n '))
            else:
                for span in cell.find_all('span'):
                    line_in_table_content.append(span.text.strip())
        table_grafiki_i_tseni_content.append(line_in_table_content)
    return table_grafiki_i_tseni_content
