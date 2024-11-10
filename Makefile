.venv:
	@python3 -m venv .venv
	@(. .venv/bin/activate; \
	pip install -q -r requirements.txt;)


run: 
	@(. .venv/bin/activate; \
	python3 main.py;)

test:
	@(. .venv/bin/activate; \
	python3 test.py;)