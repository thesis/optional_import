test:
	python setup.py nosetests \
	  --with-doctest          \
	  --doctest-extension=rst \
	  --ignore-files "bad\.py"
