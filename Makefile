build: 
	python3 setup.py build_ext -if
	python3 setup.py install
clean: 
	rm -rf __pycache__
	rm -f *.so
	rm -rf build
