import webbrowser as wb


## python script for checking the working ip of the concerned cmwscomself.
## It will check all the ip and whichever one is working it will
update the database
## accordingly

def get_WorkingIP():
    strUrl = "http://192.168.40."
    for i in range(10):
        strUrl = strUrl + str(i + 2) + "/cmscom"
        wb.open_new_tab(strUrl)
        strUrl = "http://192.168.40."



if __name__ == "__main__" :
    get_WorkingIP()
