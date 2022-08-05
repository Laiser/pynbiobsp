build: 
	python3 setup.py build_ext -if
clean: 
	rm -rf __pycache__
	rm -f *.so
	rm -rf build
