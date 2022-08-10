run:
	flask --app http-service.py run -h localhost -p 8080
setup: requirements.txt
	pip install -r requirements.txt
clean:
	rm -rf __pycache__