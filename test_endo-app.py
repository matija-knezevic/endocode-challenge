import unittest
import requests

class RESTRequests():

    def rest_requests(x):
        url = x
        try:
            r = requests.get(url,timeout=1)
            r.raise_for_status()
            return r.status_code
        except requests.exceptions.Timeout as errt:
            print (errt)
            raise
        except requests.exceptions.HTTPError as errh:
            print (errh)
            raise
        except requests.exceptions.ConnectionError as errc:
            print (errc)
            raise
        except requests.exceptions.RequestException as err:
            print (err)
            raise

# Test endpoints
class TestRESTRequests(unittest.TestCase):

    def test_helloworld(self):
        self.assertEqual(200,RESTRequests.rest_requests("http://localhost:8080/helloworld"))

    def test_helloworld_name(self):
        self.assertEqual(200,RESTRequests.rest_requests("http://localhost:8080/helloworld?name=JoeyRamoneRules"))

    def test_versionz(self):
        self.assertEqual(200,RESTRequests.rest_requests("http://localhost:8080/versionz"))

if __name__ == '__main__':
    unittest.main()