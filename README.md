## Installation

Checkout the repository: https://github.com/matija-knezevic/python-app-dockerhub-gke-deployment

Go to root directory and execute:

```bash
make
```

In this case "make" runs a Flask server which is accessible on localhost, port 8080.
If you want to override this you can either edit Makefile or use the following command:

```bash
flask --app endo-app.py run -h <your_ip> -p <your_port>
```

## Usage

```bash
# Returns "Hello World"
curl http://localhost:8080/helloworld

# Returns "Joey Ramone Rules" but (of course) you can use your own CamelCase string
curl http://localhost:8080/helloworld?name=JoeyRamoneRules

OR

curl http://localhost:8080/helloworld?name=DonauDampfSchifFahrtsElektrizitaetenHauptBetriebsWerkbauUnterBeamtenGesellschaft

# Returns git hash of all commits in the repository
curl http://localhost:8080/versionz
```

### Testing

```bash
# Starts unit testing
python test_endo-app.py
```

```bash
# Example for passed tests
...
----------------------------------------------------------------------
Ran 3 tests in 0.312s

OK

```

```bash
# Example for failed tests
...
F..
======================================================================
FAIL: test_helloworld (__main__.TestRESTRequests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_endo-app.py", line 29, in test_helloworld
    self.assertEqual(404,RESTRequests.rest_requests("http://localhost:8080/helloworld"))
AssertionError: 404 != 200

----------------------------------------------------------------------
Ran 3 tests in 0.120s

FAILED (failures=1)

```

## License
[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0)
