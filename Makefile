# Makefile
# quickly create a new bot

.PHONY: new-bot dumb-bot intermediate-bot master-bot clean cleanall

new-bot:
	chmod +x train3t.py versus3t.py
	touch 3tmind.dat

dumb-bot: clean new-bot
	./train3t.py 100

intermediate-bot: clean new-bot
	./train3t.py 100000

master-bot: clean new-bot
	./train3t.py 700000

clean:
	rm -f 3tmind.dat

cleanall: clean
	rm -rf __pycache__/*
