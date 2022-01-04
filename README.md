# Knights Battle

There	are	four	knights	who	are	about	to	do	battle.

    RED (R)
    BLUE (B)
    GREEN (G)
    YELLOW (Y)

Their	world	consists	of	an	8x8	square	`Arena`	which	looks	suspiciously	like	a	chess-board.	The	Arena	is	surrounded	by	water	on	all	sides. The	64	tiles	on	the	board	are	identified with	(row,	col)	co-ordinates	with	(0,0)	being	the	top	left tile	and	(7,0)	being	the	bottom	left	tile	(row	7	col	0).
<br/>

**Each	knight	starts	in	one	corner	of	the	board.**
    
    R (0,0) (top left)
    B (7,0) (bottom left)
    G (7,7) (bottom right)
    Y (0,7) (top right)

### Items

<br/>Around the board are the following four Items and Positons:

`Axe         (A) (2,2):  +2 Attack`  
`Dagger      (D) (2,5):  +1 Attack`  
`Helmet      (H) (5,2):  +1 Defence`  
`MagicStaff  (M) (5,5):  +1 Attack, +1 Defence`  


### Movement

<br/>Each Knight moves one tile at a time in one of four directions.<br/>

`North (N)  (UP)`  
`East  (E)  (RIGHT)`  
`South (S)  (DOWN)`  
`West  (W)  (LEFT)`  


### Fighting

<br/>Each Knight has a base attack and defence score of 1:

`Attack  (1)`  
`Defence (1)`  


# Usage

To run the app:

    python app.py

To run the test:

    python test.py

Instructions are read in from `movements.txt`.

Final result of arena is written to `result.json`.
# battling-knight-python-challenge
# battling-knight-python-challenge
