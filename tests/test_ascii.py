import pytest
import requests

url = 'http://127.0.0.1:5000' # The root url of the flask app

   
class TestTransactions():


    def test_index_page(self):
        r = requests.get(url+'/') # Assumses that it has a path of "/"
        assert r.status_code == 200 # Assumes that it will return a 200 response

    def test_conversion(self):
        r=requests.post(url+'/convertir', json={'list': ["a","e","z","x","H","h","x"]})
        data=r.json()
        assert r.status_code == 200 # Assumes that it will return a 200 response
        assert len(data)!=0,"json empty"