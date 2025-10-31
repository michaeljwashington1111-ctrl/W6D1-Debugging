run:
	python calculator.py

test:
	python -m unittest -v

test-calculator:
	python -m unittest -v test_calculator.py

test-reverser:
	python -m unittest -v test_reverser.py

menu:
	python run_menu.py
