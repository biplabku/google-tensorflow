import webbrowser as wb
import requests

## python script for checking the working ip of the concerned cmwscomself.
## It will check all the ip and whichever one is working it will
# update the database
## accordingly

def get_WorkingIP():
    strUrl = "https://www.github.com/biplabku"
    for i in range(2):
        wb.open_new_tab(strUrl)
        strUrl = strUrl + "?tab=repositories"



def check_StatusOfIP():
    strUrl = "https://www.linkedin.com/"
    r = requests.get(strUrl)
    print (r.status_code)


if __name__ == "__main__" :
    get_WorkingIP()
    check_StatusOfIP()
