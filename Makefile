compile:
	g++ -fPIC -shared ctypes_playground/c_array.cpp -o /usr/local/lib/c_array.so

cleanall:
	rm /usr/local/lib/c_array.so

test:
	make compile
	python ctypes_playground/c_array_wrapper.py
	make cleanall

