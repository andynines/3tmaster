# 3tmaster
An heuristic AI for playing tic-tac-toe
## Playing
Use the makefile to create a new bot; its knowledge is preserved in the file `3tmind.dat`.
```bash
make dumb-bot
make intermediate-bot
make master-bot # may take a moment
```
To play against the current bot, use the `versus3t.py` script. To train the bot for an additional `n` number of rounds, use `./train3t.py n`.

To clean up, use `make cleanall`.
## Example
```bash
$ make master-bot 
rm -f 3tmind.dat
chmod +x train3t.py versus3t.py
touch 3tmind.dat
./train3t.py 700000
Victory rate: 72.01%
Draw rate: 27.32%
$ ./versus3t.py 
Go second
---
--X
---
1,1 1,2 1,3 2,1 2,2 3,1 3,2 3,3: 2,2
---
-OX
--X
1,1 1,2 1,3 2,1 3,1 3,2: 1,3
--O
-OX
X-X
1,1 1,2 2,1 3,2: 3,2
-XO
-OX
XOX
1,1 2,1: 1,1
OXO
XOX
XOX
Draw
```
## Copying
MIT License; see `license.txt`.
