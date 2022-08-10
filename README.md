# endocode-challenge

endocode-challenge is "homework" assingment from a cool company called Endocode GmbH.

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

```python
# Returns "Hello World"
curl http://localhost:8080/helloworld

# Returns "Joey Ramone Rules" but (of course) you can use your own CamelCase string
curl http://localhost:8080/helloworld?name=JoeyRamoneRules

# Returns git hash of all commits in the repository
curl http://localhost:8080/versionz
```

## License
[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0)