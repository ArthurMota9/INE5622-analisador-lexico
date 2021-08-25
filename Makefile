.PHONY: run clean
setup:
	pip3 install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf venv

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip3 install wheel
	./venv/bin/pip3 install -r requirements.txt

run-st: venv/bin/activate
	./venv/bin/python3 __main__.py ./code-examples/codeWithoutError.lcc

run-nd: venv/bin/activate
	./venv/bin/python3 __main__.py ./code-examples/codeWithoutError2.lcc

run-err: venv/bin/activate
	./venv/bin/python3 __main__.py ./code-examples/codeWithError.lcc
