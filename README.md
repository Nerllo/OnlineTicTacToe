
TIC TAC TOE (runs in python3)

Basic Functionality
On the main menu you will find 4 options: PvE, PvP, Replay, and Exit

PvE:
You will be able to select whether you want to play as "X" or "O".
You will also be able to determine if you want to play first, or if you want the computer to play first.
At the end of the game you will receive a replay number, which you can use to see the game from the beginning.

PvP:
You will wait until another player joins the session. After that you will play against another person.
The mark that you will use will be assigned by the server, so will the order of who plays first (determined by who logs in first).
Several players can play at the same time on different sessions.
At the end of the game you will receive a replay number, which you can use to see the game from the beginning.

Replay:
You select the unique ID given to you at the end of a match to see your replay of a game (the replay shows only the perspective 
of the player in the game). 
The replay will let you know if you are looking at a PvP or PvE game. (Printed at the very beginning of the replay)

Exit:
Simply exits the game.

Implementation details:
I used Python's raw socket (stdlib) to program the connection. I also had to use multithreaded programming in order to allow
several games to happen at once. In the PvP version the exchange of messages and the board are handled by the server. Finally,
the replays are saved locally in the client's machine, not in the server side (making every replay unique to the client).
