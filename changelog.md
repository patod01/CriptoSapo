# Standalone is here!!

`build date: 2022-09-30 17:10:57`
`build version: 0.m4p4`

- trying to remove glitch from changelog. Let's see next push...
- working with branches from now on.
- ignored build zip files.
- fixed changelog markdown breakline.
- `init.bat` updated to evaluate env vars which add the current python dist to the path.
	- added `p` parameter to launch python interpreter.
- activated git LFS for the `.xlsx` files.
- updated readme to indicate the ETL process in the `view.xlsx` file (done at the very beginning of the project).
	- updated queryem to be independent of file path.
- cleaned up the `.xlsx` file.
- fixed typo in previous commit for future changelogs.
- modified everything to embed python.
	- added python distribution folder to app folder.
	- updated `.gitignore` to ignore every python distribution.
	- updated bat files (buy, sell, ship, spy) to work with embedded python.
- updated json indentation inside chauchera.
- updated copy function in `build.py` to:
	 - ignore comments.
	 - ignore empty lines.
- added pydist to build folder.
- added python distribution path to `src.txt`. 
- readme updated to celebrate new release.

---

# Build tools out of the box, 2/2! Keep moving from now on and go in peace.

`build date: 2022-09-12 00:48:01`
`build version: 0.m473`

- added app info file
- added `src.txt` file to read source files to be copied
- make build tools
	- erase last build content
	- check if build folder set up
	- copy new project content
	- versioning system
		- number base convertor
	- added beta versions, which does't update changelog on build
	- update changelog
		- changelog renamed from 'txt' to 'md'
	- make zip distribution
	- reordered build instructions
- make changelog file
- updated format issue in readme
- pydist ignored
- new project folders structure (files moved to src folder)
- removed trash from `del_build_content()` and added comments
- removed commented import lines in `build.py`
- readme updated
- changed `b.bat` to `build.bat`
- I screw it up. It'll not be 11 but 2 weeks instead v:
- __first public release with a tag!!__ _When I find out how to upload it..._

---

# Build tools out of the box, 1/2! New doggo's toy.

date: 2022-08-30 00:07:52

- added app info file \
.- make build tools
    - erase last build content
    - check if build folder set up \
    .- copy new project content \
    .- versioning system
        - number base convertor \
    .- update changelog \
    .- make zip distribution \
.- make changelog file
- updated format issue in readme
- pydist and bman ignored

---

# Everyone stand up in the Going Merry!!

date: 2022-08-21 14:48:42

- The general mini on board refactor
    - everyone moved to going_merry
    - nami kissed sapo and it converted into... usopp?
    - sapo
        - renamed to usopp
            - say hello to usopp!!
        - old schema function, pAPP(), renamed to spy()
    - nami dependencies updated from sapo to usopp
    - luffy dependencies updated from sapo to usopp
    - dev tools updated to fit in going_merry
    - action buttons updated to fit in going_merry
- now nami says when no wallet was created
- franky
    - updated format time function to optionally give seconds
    - franky's franky renamed to build_blueprint()
- blazingly new readme to meet the actual purpose of the project
- updated dev tools to inject ingored files into app's folder
- added comment to every button indicating python's path
- nami now checks if the deposited amount is valid (int > 0)
- now nami saves the seconds of trades in wallet's history
- removed some dumb spaces

---

# Say hello to Luffitaro

date: 2022-08-20 19:46:55

- body of main function
    - logic flow and modules imported
    - orders to buy
    - orders to sell
    - orders to spy
    - orders to ship
    - bat file buttons for every order
- luffy has a whip

Other mini goals:
- nami now verifies if coin index exists in wallet when selling
- nami's chat is now capitalized
- sapo's chat is now capitalized and pprint removed
- franky's chat is now capitalized and pprint removed
- changed wallet database url in nami
- added del new_trade statemant in nami
- changed databases url in franky and sapo
- changed 'select' button
- added 'init.bat' to add dev tools to path in command line
- changed 't.bat' to fit new path
- added database verification function to franky
- added description to make_format_time() in franky
- added a dot to the end of every function description

---

# say hello to Onami

date: 2022-08-17 23:00:09

- wallet functions added
    - json structure
    - write to
    - read from
    - update pocket
    - first balance option
- wallet gitignored
- sapo has redefined itself because of being afraid of nami
    - separate functions for
        - watch the price
        - write down the price

Mini changes:
- unignored some dev tools
- added tools folder for building utilities
- new doc strings style defined
- new hierarchy jokes defined
- franosuke refactored
        - franky now has a function to convert time
        - moved coins index to sapo
        - does not need to convert coins names anymore
- sapo refactored to adapt to nami structure
        - added function to create link to binance API
        - coins index list updated
                - moved from franky to sapo
        - infoBTC() changed to coin_info()
        - now writes to csv the index instead of coin's name
        - erased thrash from main function, pAPP(), to create these functions in nami
        - changed var 'symbol' to 'indice'

---

# Say hello to franosuke and other mini goals

date: 2022-08-01 13:52:04

Stuff added to franky:
- avoid empty lines
- register moved to its own function inside franky
    - open, high, low, close values
- comments pulled out
- added principal cryptocoins to track

Franosuke arrives with a new viewer in a spreadsheet:
- added power query rutines to read from csv
- graph visualization with candles

Other minor adjustments:
- added read from the command line capabilities to sapo
- sapo now writes to csv, just like franky does
- sapo can now deliver only the price from the command line
- gitignore updated
    - all csv ignored
    - txt blown from watch dog
    - temp and build folders ignored

---

# steps from becoming an actual app

date: 2022-06-29 00:20:11

- line jump added in 'readme'
- deleted old comments. RIP requests
- http request encapsulated
- added csv transformer to format date. Hi, Franky!
- updated gitignore to ignore more

---

# bye bye requests

date: 2022-06-12 23:28:47

- urllib is now alive
- requests still exists as comments
- ignored 'status' file and deleted from repository

---

# moved to urllib

date: 2022-05-15 23:18:10

added the code to drop requests lib to go with the minimum dependancies
possible. Now remains to make it work.

---

# add ed gitignore

date: 2022-05-15 17:59:54

---

# new pc

date: 2022-05-10 07:50:40

testing new environment while adding status file and select button

---

# folder buttons

date: 2022-05-08 18:05:08

added BAT files to manipulate actions:
- buy
- sell
- choose

---

# YEAH

date: 2022-04-24 21:31:14

It's time to conquer the whole world

---

# Initial commit

date: 2022-04-24 20:15:43

