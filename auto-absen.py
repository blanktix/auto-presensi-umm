import requests
from bs4 import BeautifulSoup

r = requests.Session()


creds = open("creds.txt","r").read().split()

baseurl = "https://infokhs.umm.ac.id/"
page = {
    'login': "login",
    'jadwal': "jadwal-kuliah",
}

def login(creds):
    usr = creds[0]
    pwd = creds[1]
    home=r.post(url=baseurl+page["login"],data={"username": creds[0], "password": creds[1]})
    presensi()


def presensi():
    menu = r.get(baseurl+page["jadwal"]).text
    soup = BeautifulSoup(menu, "html.parser")
    
    tbl_presensi=list(soup.find_all('a', attrs={'class': "btn btn-xs btn-success"}))
    for tbl_matkul in tbl_presensi:
        jdwl =r.get(tbl_matkul.get('href')).text
        soup_jdwl =BeautifulSoup(jdwl, "html.parser")
        tbl_hadir=list(soup_jdwl.find_all('a', attrs={'class': "btn btn-xs btn-success"}))

        if len(tbl_hadir)!=0:
            for tbl in tbl_hadir:
                r.get(tbl.get('href'))
                matkul = soup_jdwl.find_all('div', attrs={'class': "col-sm-9"})
                print(f"Presensi matkul:  {matkul[2].get_text()} berhasil")
if __name__ == "__main__":
    login(creds)