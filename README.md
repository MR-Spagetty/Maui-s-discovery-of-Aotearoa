# Maui-s-discovery-of-Aotearoa

## Setup:

To run this program you must have python 3.6 or greater and install the python keyboard module

if python is in your PATH use the following command to install the module:

`py -m pip install keyboard`

if python is not on your PATH use the following command to install the keyboard module:

`<python path> -m pip install keyboard`

replace \<python path> with the path tp you python installation

## playing:

do NOT run this program in idle if you do it will not display it correctly

to run this program correctly you must navigate to the directory containing the game using:

`cd <path to file's directory>`

then run the program using:

`py maui.py`

or like before if python is not in your path:

`<python path> maui.py`

## gameplay:

in the game you play as Maui the mythical character from pacific islander legends who discovered Aotearoa. the aim of this game is to find Aotearoa without dying.

along your path you will encounter different types of tiles that can do different things, here is the key for these tiles which can be seen at any point in the game py pressing `h`

```Tile type and function key:

Sea:
tile without fish:
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈
≈≈≈≈≈≈≈≈≈

tile with fish:
≈≈≈≈≈ α ≈
≈ α ≈≈≈≈≈
≈≈≈ α ≈≈≈
≈ α ≈ α ≈
≈≈≈≈≈≈≈≈≈

    The sea tile has a 50/50 chance of generating fish and
    if the tile generates fish the delay between a fish
    generating will be between 2 and 5 turns (inclusive).

Island:
≈≈≈≈≈≈≈≈≈
≈≈▄█▄██▌≈
≈███████`
≈▐█████`≈
≈≈`≈≈≈`≈≈

    The island tile is basically just a sea tile that cannot
    generate fish.

Rock:
≈≈≈≈≈≈≈≈≈
≈≈&██&%/≈
≈≈\&@██&≈
≈≈≈\%&&#≈
≈≈≈≈≈≈≈≈≈

    The rock tile is a barrier that cannot be passed and in
    the hardest difficulty if you hit one you lose 3 food.

Whirlpool:
≈≈≈/≈_≈≈≈
≈≈|≈/≈\≈≈
≈|≈\@\≈|≈
≈≈\_/≈|≈≈
≈≈≈≈≈≈/≈≈

    The whirlpool tile is a tile that can do many things
    these things include:
    - Random teleportation (within 255 tiles in both directions)
    - Losing a random amount of food between 1 and how much you have
    - Killing the player (by removing all of your fish)```
