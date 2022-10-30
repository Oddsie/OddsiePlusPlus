# Oddsie++
 Oddsie is an "improved" version of Oddsie.
# Examples
```lua
use random
class main (
  function __init__::self (
    display "NUMBER GUESS"
    var guess=int(input(":"))
    var actual=random.randint(1,10)
    if guess==actual (
      display "Good Guess!"
    );
    otherwise (
      display "Incorrect! Number was "+str(actual)+"!"
    );
);
```
*^ Simple number-guessing game ^*
```lua
;; Really Complicated Hello World
class main (
	var txt=""
	function uno::self (
		var txt=txt+"Hello,"
	);
	function dos::self (
		var txt=txt+" world!"
	);
	function tres::self (
		display txt
	);
	function __init__::self (
	    .self.uno
	    .self.dos
	    .self.tres
	);
);
```
*^ An overly complicated Hello, World! program ^*
# What do I need to code in Oddsie?
- Linux (Won't work on Windows)
- Python 3.7 and up
- Oddsie
