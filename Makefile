.PHONY: default build install clean

default: build

build:
	echo "Hello World" > helloworld
	echo "0.1" >> helloworld

install:
	mkdir -p $(DESTDIR)/usr/share/helloworld
	cp helloworld $(DESTDIR)/usr/share/helloworld

clean:
	rm helloworld
