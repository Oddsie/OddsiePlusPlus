# Oddsie++
 Oddsie++ is an "improved" version of Oddsie.
# Examples
```lua
use random
class main (
	function __init__::self (
		display "NUMBER GUESS"
		var act=random.randint()
		var gue=input(": ")
		if gue==act (
			display "Good Guess!"
		);
		otherwise (
			display "Incorrect! Number was "+str(act)+"!"
		);
	);
);
```
*^ Simple number-guessing game ^*
```lua
;; Really Complicated Hello World
class main (
	var self.txt=""
	function uno::self (
		var self.txt=txt+"Hello,"
	);
	function dos::self (
		var self.txt=txt+" world!"
	);
	function tres::self (
		display self.txt
	);
	function __init__::self (
	    .self.uno
	    .self.dos
	    .self.tres
	);
);
```
*^ An overly complicated Hello, World! program ^*
# What do I need to code in Oddsie++?
The same as Oddsie.
