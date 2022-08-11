# endocode-challenge

endocode-challenge is "homework" assignment from a cool company called Endocode GmbH.

## Installation

Checkout the repository: https://github.com/matija-knezevic/endocode-challenge

Go to root directory and execute:

```bash
make
```

In this case "make" runs a Flask server which is accessible on localhost, port 8080.
If you want to override this you can either edit Makefile or use the following command:

```bash
flask --app http-service.py run -h <your_ip> -p <your_port>
```

## Usage

```bash
# Returns "Hello World"
curl http://localhost:8080/helloworld

# Returns "Joey Ramone Rules" but (of course) you can use your own CamelCase string
curl http://localhost:8080/helloworld?name=JoeyRamoneRules

# Returns git hash of all commits in the repository
curl http://localhost:8080/versionz
```

### Testing

```bash
# Starts unit testing
python test_http-service.py
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
  File "test_http-service.py", line 29, in test_helloworld
    self.assertEqual(404,RESTRequests.rest_requests("http://localhost:8080/helloworld"))
AssertionError: 404 != 200

----------------------------------------------------------------------
Ran 3 tests in 0.120s

FAILED (failures=1)

```

## License
[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0)