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
	function __init__::self (
		var self.txt=""
		.self.uno::
		.self.dos::
		.self.tres::
	);
	function uno::self (
		var self.txt=self.txt+"Hello,"
	);
	function dos::self (
		var self.txt=self.txt+" world!"
	);
	function tres::self (
		display self.txt
	);
);
```
*^ An overly complicated Hello, World! program ^*
# What do I need to code in Oddsie++?
The same as Oddsie.
