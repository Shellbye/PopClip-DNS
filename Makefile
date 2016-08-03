build: extensions/DNS.popclipextz
.PHONY: build

clean:
	rm -f extensions/DNS.popclipextz
.PHONY: clean

extensions/DNS.popclipextz: source/DNS/dig-wrapper.py source/DNS/Config.plist
	mkdir -p extensions/DNS.popclipext
	cp $? extensions/DNS.popclipext
	cd extensions && zip -r DNS.popclipextz DNS.popclipext
	rm -rf extensions/DNS.popclipext
