hello:
	echo "this is my first make command"
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
test:
	# python -m pytest -vv test_hello.py
	echo test
lint:
	pylint --disable=R,C,W0311 app.py