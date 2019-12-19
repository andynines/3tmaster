
.PHONY: train clean

train:
	chmod +x train3t.py versus3t.py
	touch 3tmind.dat
	./train3t.py 10

clean:
	rm -rf __pychache__/
	rm -f 3tmind.dat
