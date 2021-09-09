##
# maui.py
# MR-Spagetty

import os
import random
from sys import argv
try:
    import keyboard
except ImportError:
    print("Please install the keyboard python module")


class controls:
    def __init__(self, up, down, left, right):
        """Base control setup

        Args:
            up (str): button to be associated with moving upwards.
            down (str): button to be associated with moving downwards.
            left (str): button to be associated with moving left.
            right (str): button to be associated with moving right.
        """
        self.up_control = up
        self.down_control = down
        self.left_control = left
        self.right_control = right

    def edit_up_control(self, up):
        """changes the button to be associated with moving upwards.

        Args:
            up (str): new button to be associated with moving upwards.
        """
        self.up_control = up

    def edit_down_control(self, down):
        """changes the button to be associated with moving downwards.

        Args:
            down (str): new button to be associated with moving downwards.
        """
        self.down_control = down

    def edit_left_control(self, left):
        """changes the button to be associated with moving left.

        Args:
            left (str): new button to be associated with moving left.
        """
        self.left_control = left

    def edit_right_control(self, right):
        """changes the button to be associated with moving right.

        Args:
            right (str): new button to be associated with moving right.
        """
        self.right_control = right


class map:
    def __init__(self, seed, dificulty):
        """initalizing the map.

        Args:
            seed (any): the seed for the world
            dificulty (int): 1, 2, or 3  defines the dificulty that will be
            used in the map
        """
        self.random = random
        self.random.seed(seed)
        self.dificulty = dificulty
        self.tiles = {}

    def generate_tile(self, turn_num, coordinates={'x': 0, 'y': 0}):
        """logic for generating a new tile

        Args:
            turn_num (int): the current turn number
            coordinates (dict, optional): the coordinates of the tile to be
            generated. Defaults to {'x': 0, 'y': 0}.
        """
        if coordinates['y'] not in self.tiles.keys():
            self.tiles[coordinates['y']] = {}
        self.tiles[coordinates['y']][coordinates['x']] = self.tile(self,
                                                                   turn_num)

    def print(self, current_seen, view_distance, x, y, turn_num, food,
              message):
        """prints the currently visable tile of the map with the player's
        current coordinates and food

        Args:
            current_seen (dict{lists}): the tiles that can currently be seen
            by the player
            view_distance (int): the view distance of the player
            x (int): the current x coordinate of the player
            y (int): the current y coordinate of the player
            turn_num (int): the current turn number
            food (float): the amount of food the player has
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        if view_distance == 2:
            r0 = current_seen[-2]
            r1 = current_seen[-1]
            r2 = current_seen[0]
            r3 = current_seen[1]
            r4 = current_seen[2]
            print(
                f"""
({x}x, {-y}y) turn:{turn_num} food:{food}
╔═════════╦═════════╦═════════╦═════════╦═════════╗
║{r0[-2][0]}║{r0[-1][0]}║{r0[0][0]}║{r0[1][0]}║{r0[2][0]}║
║{r0[-2][1]}║{r0[-1][1]}║{r0[0][1]}║{r0[1][1]}║{r0[2][1]}║
║{r0[-2][2]}║{r0[-1][2]}║{r0[0][2]}║{r0[1][2]}║{r0[2][2]}║
║{r0[-2][3]}║{r0[-1][3]}║{r0[0][3]}║{r0[1][3]}║{r0[2][3]}║
║{r0[-2][4]}║{r0[-1][4]}║{r0[0][4]}║{r0[1][4]}║{r0[2][4]}║
╠═════════╬═════════╬═════════╬═════════╬═════════╣
║{r1[-2][0]}║{r1[-1][0]}║{r1[0][0]}║{r1[1][0]}║{r1[2][0]}║
║{r1[-2][1]}║{r1[-1][1]}║{r1[0][1]}║{r1[1][1]}║{r1[2][1]}║
║{r1[-2][2]}║{r1[-1][2]}║{r1[0][2]}║{r1[1][2]}║{r1[2][2]}║
║{r1[-2][3]}║{r1[-1][3]}║{r1[0][3]}║{r1[1][3]}║{r1[2][3]}║
║{r1[-2][4]}║{r1[-1][4]}║{r1[0][4]}║{r1[1][4]}║{r1[2][4]}║
╠═════════╬═════════╬═════════╬═════════╬═════════╣
║{r2[-2][0]}║{r2[-1][0]}║≈≈≈≈≈≈≈≈≈║{r2[1][0]}║{r2[2][0]}║
║{r2[-2][1]}║{r2[-1][1]}║≈≈≈≈≈≈≈≈≈║{r2[1][1]}║{r2[2][1]}║
║{r2[-2][2]}║{r2[-1][2]}║≈≈≈≈≈☻≈≈≈║{r2[1][2]}║{r2[2][2]}║
║{r2[-2][3]}║{r2[-1][3]}║≈≈\\__█/≈≈║{r2[1][3]}║{r2[2][3]}║
║{r2[-2][4]}║{r2[-1][4]}║≈≈≈≈≈≈≈≈≈║{r2[1][4]}║{r2[2][4]}║
╠═════════╬═════════╬═════════╬═════════╬═════════╣
║{r3[-2][0]}║{r3[-1][0]}║{r3[0][0]}║{r3[1][0]}║{r3[2][0]}║
║{r3[-2][1]}║{r3[-1][1]}║{r3[0][1]}║{r3[1][1]}║{r3[2][1]}║
║{r3[-2][2]}║{r3[-1][2]}║{r3[0][2]}║{r3[1][2]}║{r3[2][2]}║
║{r3[-2][3]}║{r3[-1][3]}║{r3[0][3]}║{r3[1][3]}║{r3[2][3]}║
║{r3[-2][4]}║{r3[-1][4]}║{r3[0][4]}║{r3[1][4]}║{r3[2][4]}║
╠═════════╬═════════╬═════════╬═════════╬═════════╣
║{r4[-2][0]}║{r4[-1][0]}║{r4[0][0]}║{r4[1][0]}║{r4[2][0]}║
║{r4[-2][1]}║{r4[-1][1]}║{r4[0][1]}║{r4[1][1]}║{r4[2][1]}║
║{r4[-2][2]}║{r4[-1][2]}║{r4[0][2]}║{r4[1][2]}║{r4[2][2]}║
║{r4[-2][3]}║{r4[-1][3]}║{r4[0][3]}║{r4[1][3]}║{r4[2][3]}║
║{r4[-2][4]}║{r4[-1][4]}║{r4[0][4]}║{r4[1][4]}║{r4[2][4]}║
╚═════════╩═════════╩═════════╩═════════╩═════════╝
{message}
                    Center Tile
                    ╔═════════╗
                    ║{r2[0][0]}║
                    ║{r2[0][1]}║
                    ║{r2[0][2]}║
                    ║{r2[0][3]}║
                    ║{r2[0][4]}║
                    ╚═════════╝
""")
        if view_distance == 1:
            r0 = current_seen[-1]
            r1 = current_seen[0]
            r2 = current_seen[1]
            print(
                f"""
({x}x, {-y}y) turn:{turn_num} food:{food}
╔═════════╦═════════╦═════════╗
║{r0[-1][0]}║{r0[0][0]}║{r0[1][0]}║
║{r0[-1][1]}║{r0[0][1]}║{r0[1][1]}║
║{r0[-1][2]}║{r0[0][2]}║{r0[1][2]}║
║{r0[-1][3]}║{r0[0][3]}║{r0[1][3]}║
║{r0[-1][4]}║{r0[0][4]}║{r0[1][4]}║
╠═════════╬═════════╬═════════╣
║{r1[-1][0]}║≈≈≈≈≈≈≈≈≈║{r1[1][0]}║
║{r1[-1][1]}║≈≈≈≈≈≈≈≈≈║{r1[1][1]}║
║{r1[-1][2]}║≈≈≈≈≈☻≈≈≈║{r1[1][2]}║
║{r1[-1][3]}║≈≈\\__█/≈≈║{r1[1][3]}║
║{r1[-1][4]}║≈≈≈≈≈≈≈≈≈║{r1[1][4]}║
╠═════════╬═════════╬═════════╣
║{r2[-1][0]}║{r2[0][0]}║{r2[1][0]}║
║{r2[-1][1]}║{r2[0][1]}║{r2[1][1]}║
║{r2[-1][2]}║{r2[0][2]}║{r2[1][2]}║
║{r2[-1][3]}║{r2[0][3]}║{r2[1][3]}║
║{r2[-1][4]}║{r2[0][4]}║{r2[1][4]}║
╚═════════╩═════════╩═════════╝
{message}
          Center Tile
          ╔═════════╗
          ║{r1[0][0]}║
          ║{r1[0][1]}║
          ║{r1[0][2]}║
          ║{r1[0][3]}║
          ║{r1[0][4]}║
          ╚═════════╝
""")

    class tile:
        # probabilities of each tile type is determened by frequency in this
        # list
        tile_types = ['sea', 'sea', 'sea', 'island', 'whirlpool', 'rock']

        tiles = {'island': [
                    '≈≈≈≈≈≈≈≈≈',
                    '≈≈▄█▄██▌≈',
                    '≈███████`',
                    '≈▐█████`≈',
                    '≈≈`≈≈≈`≈≈'
                ],
            'sea': {
                'fish': [
                    '≈≈≈≈≈≈≈α≈',
                    '≈α≈≈≈≈≈≈≈',
                    '≈≈≈≈α≈≈≈≈',
                    '≈α≈≈≈≈≈α≈',
                    '≈≈≈≈≈≈≈≈≈'
                ],
                'no fish': [
                    '≈≈≈≈≈≈≈≈≈',
                    '≈≈≈≈≈≈≈≈≈',
                    '≈≈≈≈≈≈≈≈≈',
                    '≈≈≈≈≈≈≈≈≈',
                    '≈≈≈≈≈≈≈≈≈'
                ]
                },
            'whirlpool': [
                '≈≈≈≈≈≈≈≈≈',
                '≈≈whirl≈≈',
                '≈≈≈≈≈≈≈≈≈',
                '≈≈≈pool≈≈',
                '≈≈≈≈≈≈≈≈≈'
                ],
            'rock': [
                '≈≈≈≈≈≈≈≈≈',
                '≈≈≈≈≈≈≈≈≈',
                '≈≈≈ROCK≈≈',
                '≈≈≈≈≈≈≈≈≈',
                '≈≈≈≈≈≈≈≈≈'
            ]
            }

        def __init__(self, map_obj, turn_number,
                     generated=True, tile_type=None):
            """setup for a map tile

            Args:
                map_obj (map_type_object): the parent map to be associated with
                this tile.

                turn_number (int): the current turn number to be used to
                determin the life of the tile.

                generated (bool, optional): weather or not the tile will be
                randomly generated. Defaults to True.

                tile_type (str, optional): used to determin what the type of
                this tile will be if not randomly generated. Defaults to None.
            """
            self.turn_created = turn_number

            self.parent = map_obj
            # determing what kind of tile will be generated
            if generated:
                self.type = map_obj.random.choice(self.tile_types)
            else:
                self.type = tile_type

            # Determining wheather or not a sea tile will generate fish and
            # the delay between each fish generated
            if self.type != 'sea':
                self.generates_fish = False
            else:
                self.generates_fish = bool(random.getrandbits(1))
                if self.generates_fish:
                    self.fish_delay = map_obj.random.randint(2, 5)
                    self.remaining_delay = int(self.fish_delay)
            if not self.generates_fish:
                self.fish_delay = 0

            self.has_fish = False
            if self.type == 'whirlpool':
                self.cooldown = 2
                self.cooldown_at = 0

        def check_if_fish(self, last_seen, current_turn):
            """logic to check if a tile has generated a fish

            Args:
                last_seen (int): the turn number that this tile was last seen
                current_turn (int): the current turn number
            """
            # only checks if the tile can generate fish and does not already
            # have a fish
            if self.generates_fish and not self.has_fish:
                turns_since_seen = current_turn - last_seen
                if self.remaining_delay - turns_since_seen <= 0:
                    self.remaining_delay = 0
                    self.has_fish = True
                else:
                    self.remaining_delay -= turns_since_seen

        def collect_fish(self, player):
            """logic for collection a fish

            Args:
                player (player_type_object): the player that will be affected
                by the whirlpool
            """
            if self.has_fish:
                player.food += 1
                self.has_fish = False
                self.remaining_delay = int(self.fish_delay)

        # things that can happen in a whirl pool

        def teleport_random(self, player):
            """Logic for teleporting the player to a random location

            Args:
                player (player_type_object): the player that will be affected
                by the whirlpool
            """
            x_offset = random.choice([-1, 1]) * random.getrandbits(8)
            y_offset = random.choice([-1, 1]) * random.getrandbits(8)
            player.current_message = "you got teleported "\
                f"by {x_offset}x and {y_offset}y"
            player.coordinates['x'] += x_offset
            player.coordinates['y'] += y_offset

        def lose_fish(self, player):
            """function that causes the player to lose between 1 food and
            however much the player currently has

            Args:
                player (player_type_object): the player that will be affected
                by the whirlpool
            """
            amount_to_lose = random.randint(2, (player.food*2)) / 2
            player.food -= amount_to_lose
            player.current_message = f'You lost {amount_to_lose} food'

        def die(self, player):
            """function to kill the player

            Args:
                player (player_type_object): the player that will be affected
                by the whirlpool
            """
            player.food = 0
            player.current_message = "you got sucked down to Davey Jones' "\
                "locker"

        def whirlpool_execute(self, player):
            """function for executing a whirlpool function

            Args:
                player (player_type_object): the player that will be affected
                by the whirlpool
            """
            if self.type == 'whirlpool':
                x = player.coordinates['x']
                y = player.coordinates['y']
                turns_since_seen = (player.current_turn -
                                    player.last_seen_chart[y][x])
                if self.cooldown_at - turns_since_seen <= 0:
                    possible_actions = [
                        self.teleport_random, self.lose_fish,
                        self.die
                    ]
                    random.choice(possible_actions)(player)
                    self.cooldown_at = self.cooldown
                else:
                    self.cooldown_at -= turns_since_seen

        def create_display(self):
            """creat the display for the tile display

            Returns:
                list: the display for the tile
            """
            if self.type == "sea":
                if self.has_fish:
                    tile = self.tiles['sea']['fish']
                else:
                    tile = self.tiles['sea']['no fish']
            else:
                tile = self.tiles[self.type]
            return tile


class player:
    dificulty_starts = {
        #   F  V
        1: (5, 2),
        2: (5, 1),
        3: (2, 1)
    }
    # F = starting food
    # V = view distance

    def __init__(self, map_obj, control_scheme):
        """generating the player object

        Args:
            map_obj (map_type_object): the map object that this player object
            will use
            control_scheme (controls_type_object): the controls that this
            player will use
        """
        self.in_menu = True
        self.playing = True
        self.quiting = False
        self.in_help = False
        self.food, self.view_distance = self.dificulty_starts[
            map_obj.dificulty]
        self.map = map_obj
        self.control_scheme = control_scheme
        self.coordinates = {'x': 0, 'y': 0}
        self.last_seen_chart = {}
        self.current_turn = 1
        self.button_listener = keyboard.on_press(self.button_logic)
        self.current_message = ''

    def hit_a_rock(self):
        """logic for when you hit a rock
        """
        self.current_message = 'You have hit a rock you cannot pass this'
        if self.map.dificulty == 3:
            self.current_message = f'{self.current_message}\nas '\
                'punnnnnnishment you have lost 2 fish'
            self.food -= 2
        self.update_map_and_chart(True)

    def update_map_and_chart(self, hit_rock=False):
        """function for updating the displayed map

        Args:
            hit_rock (bool, optional): wheather or not the functions was
            called by hitting a rock. Defaults to False.
        """
        current_seen = {}

        if self.coordinates['y'] in self.map.tiles and not hit_rock:
            if self.coordinates['x'] in self.map.tiles[self.coordinates['y']]:
                self.map.tiles[
                    self.coordinates['y']][
                        self.coordinates['x']].collect_fish(self)
                self.map.tiles[
                    self.coordinates['y']][
                        self.coordinates['x']].whirlpool_execute(self)

        # iterating through the currently visable x coordinates
        for x in range(self.coordinates['x'] - self.view_distance,
                       self.coordinates['x'] + 1 + self.view_distance):
            # iterating through the currently visable y coordinates
            for y in range(self.coordinates['y'] - self.view_distance,
                           self.coordinates['y'] + 1 + self.view_distance):
                # checking if the tile at these coordinates currently exists
                # and if it doesnt it creates the tile
                if y not in self.map.tiles:
                    self.map.tiles[y] = {}
                if x not in self.map.tiles[y]:
                    self.map.generate_tile(
                        self.current_turn, {'x': x, 'y': y})

                # checking if the tile is in the last seen chart and if it is
                # not adding it to the chart with the current turn as the value
                if y not in self.last_seen_chart:
                    self.last_seen_chart[y] = {}
                if x not in self.last_seen_chart[y]:
                    self.last_seen_chart[y][x] = self.current_turn
                else:
                    # checking if the tile has fish then updating it's last
                    # seen turn number
                    self.map.tiles[y][x].check_if_fish(
                        self.last_seen_chart[y][x], self.current_turn)
                    self.last_seen_chart[y][x] = self.current_turn
                # creating the display grid
                rx = x - self.coordinates['x']
                ry = y - self.coordinates['y']
                if ry not in current_seen:
                    current_seen[ry] = {}
                current_seen[ry][rx] = self.map.tiles[y][x].create_display()
        self.map.print(current_seen, self.view_distance,
                       *self.coordinates.values(), self.current_turn,
                       self.food, self.current_message)
        self.current_message = ''

    def help(self):
        """displays help information
        """
        sea_tile = map.tile.tiles['sea']
        sea_tile_fish = "\n".join(sea_tile['fish'])
        sea_tile_no_fish = "\n".join(sea_tile['no fish'])
        island_tile = "\n".join(map.tile.tiles['island'])
        rock_tile = "\n".join(map.tile.tiles['rock'])
        whirlpool_tile = "\n".join(map.tile.tiles['whirlpool'])
        print(f"""
Button:   | Function:
h         | opens this dialogue
{self.control_scheme.up_control}         | Moves you upwards
{self.control_scheme.down_control}         | Moves you downwards
{self.control_scheme.left_control}         | Moves you left
{self.control_scheme.right_control}         | Moves you right
q         | activates the quit prompt

Tile type and function key:

Sea:
tile without fish:
{sea_tile_no_fish}
tile with fish:
{sea_tile_fish}

    The sea tile has a 50/50 chance of generating fish and
    if the tile generates fish the delay between a fish
    generating will be between 2 and 5 turns (inclusive).

Island:
{island_tile}

    The island tile is basically just a sea tile that cannot
    gerate fish.

Rock:
{rock_tile}

    The rock tile is a barrier that cannot be passed and in
    the hardest difficulty if you hit one you lose 3 food.
    your difficuty is {"not hard mode" if self.map.dificulty < 3 else
    "hard mode"}
Whirlpool:
{whirlpool_tile}

    The whirlpool tile is a tile that can do mny things
    these things include:
    - Random telportation (within 255 tiles in both directions)
    - Losing a random amount of food between 1 and how much you have
    - Killing the player (by removing all of your fish)

Press a key to continue
""")

    def button_logic(self, button):
        """the logic for buttons

        Args:
            button (str): the value of the button to process
        """
        moved = False
        if not self.in_menu:
            # getting the usefull information out of the button variable
            button = str(button)[14:-6]
            hit_a_rock = False
            if self.in_help:
                self.in_help = False
                self.update_map_and_chart()
            elif self.quiting:
                if button == 'y':
                    self.playing = False
                elif button == 'n':
                    self.quiting = False
                    self.update_map_and_chart()
            else:
                if button == self.control_scheme.up_control:
                    if self.map.tiles[
                            self.coordinates['y'] - 1][
                                self.coordinates['x']].type != 'rock':

                        self.coordinates['y'] -= 1
                        self.food -= 0.5
                        moved = True
                    else:
                        hit_a_rock = True
                elif button == self.control_scheme.down_control:
                    if self.map.tiles[
                            self.coordinates['y'] + 1][
                                self.coordinates['x']].type != 'rock':

                        self.coordinates['y'] += 1
                        self.food -= 0.5
                        moved = True
                    else:
                        hit_a_rock = True
                elif button == self.control_scheme.right_control:
                    if self.map.tiles[
                            self.coordinates['y']][
                                self.coordinates['x'] + 1].type != 'rock':

                        self.coordinates['x'] += 1
                        self.food -= 0.5
                        moved = True
                    else:
                        hit_a_rock = True
                elif button == self.control_scheme.left_control:
                    if self.map.tiles[
                            self.coordinates['y']][
                                self.coordinates['x'] - 1].type != 'rock':

                        self.coordinates['x'] -= 1
                        self.food -= 0.5
                        moved = True
                    else:
                        hit_a_rock = True
                if moved:
                    self.update_map_and_chart()
                    self.current_turn += 1
                elif hit_a_rock:
                    self.hit_a_rock()
                if button == 'q':
                    print('Are you sure (Y|N)')
                    self.quiting = True
                if button == 'h':
                    self.in_help = True
                    self.help()


class menu:
    menu_options = {
        'start': """
╔════════════════════════════════════════════════════╗
║ ______   _________  ________   ______   _________  ║
║/_____/\\ /________/\\/_______/\\ /_____/\\ /________/\\ ║
║\\::::_\\/_\\__.::.__\\/\\::: _  \\ \\\\:::_ \\ \\\\__.::.__\\/ ║
║ \\:\\/___/\\  \\::\\ \\   \\::(_)  \\ \\\\:(_) ) )_ \\::\\ \\   ║
║  \\_::._\\:\\  \\::\\ \\   \\:: __  \\ \\\\: __ `\\ \\ \\::\\ \\  ║
║    /____\\:\\  \\::\\ \\   \\:.\\ \\  \\ \\\\ \\ `\\ \\ \\ \\::\\ \\ ║
║    \\_____\\/   \\__\\/    \\__\\/\\__\\/ \\_\\/ \\_\\/  \\__\\/ ║
╚════════════════════════════════════════════════════╝



  ______    __  __    ________  _________
 /_____/\\  /_/\\/_/\\  /_______/\\/________/\\
 \\:::_ \\ \\ \\:\\ \\:\\ \\ \\__.::._\\/\\__.::.__\\/
  \\:\\ \\ \\ \\_\\:\\ \\:\\ \\   \\::\\ \\    \\::\\ \\
   \\:\\ \\ /_ \\\\:\\ \\:\\ \\  _\\::\\ \\__  \\::\\ \\
    \\:\\_-  \\ \\\\:\\_\\:\\ \\/__\\::\\__/\\  \\::\\ \\
     \\___|\\_\\_/\\_____\\/\\________\\/   \\__\\/

""",
        'quit': """

  ______   _________  ________   ______   _________
 /_____/\\ /________/\\/_______/\\ /_____/\\ /________/\\
 \\::::_\\/_\\__.::.__\\/\\::: _  \\ \\\\:::_ \\ \\\\__.::.__\\/
  \\:\\/___/\\  \\::\\ \\   \\::(_)  \\ \\\\:(_) ) )_ \\::\\ \\
   \\_::._\\:\\  \\::\\ \\   \\:: __  \\ \\\\: __ `\\ \\ \\::\\ \\
     /____\\:\\  \\::\\ \\   \\:.\\ \\  \\ \\\\ \\ `\\ \\ \\ \\::\\ \\
     \\_____\\/   \\__\\/    \\__\\/\\__\\/ \\_\\/ \\_\\/  \\__\\/



╔════════════════════════════════════════════════════╗
║ ______    __  __    ________  _________            ║
║/_____/\\  /_/\\/_/\\  /_______/\\/________/\\           ║
║\\:::_ \\ \\ \\:\\ \\:\\ \\ \\__.::._\\/\\__.::.__\\/           ║
║ \\:\\ \\ \\ \\_\\:\\ \\:\\ \\   \\::\\ \\    \\::\\ \\             ║
║  \\:\\ \\ /_ \\\\:\\ \\:\\ \\  _\\::\\ \\__  \\::\\ \\            ║
║   \\:\\_-  \\ \\\\:\\_\\:\\ \\/__\\::\\__/\\  \\::\\ \\           ║
║    \\___|\\_\\_/\\_____\\/\\________\\/   \\__\\/           ║
╚════════════════════════════════════════════════════╝
"""
    }

    def __init__(self):
        """initalizes the game and starts the menu
        """
        # basic game setup
        if len(argv) >= 6:
            control_scheme = controls(*argv[1:5])
            try:
                dificulty = int(argv[5])
            except ValueError:
                dificulty = 1
            seed = random.getrandbits(200)
            if len(argv) >= 7:
                seed = argv[6]
        else:
            control_scheme = controls('w', 's', 'a', 'd')
            seed = random.getrandbits(200)
            dificulty = 1
        game_map = map(seed, dificulty)

        # basic variables used in the menu
        self.selected = 'start'
        self.in_menu = True
        self.quiting = False

        # initalizing the player
        self.game_player = player(game_map, control_scheme)

        # creating the key handler for use in the menu

        def key_handler(key, menu):
            """key handler for the menu

            Args:
                key (str): the key that was pressed
                menu (menu_type_object): the menu object
            """
            if menu.in_menu:
                if key == 'enter':
                    menu.execute_selection()
                elif key == menu.game_player.control_scheme.up_control\
                        or key == menu.game_player.control_scheme.down_control:
                    if menu.selected == 'start':
                        menu.selected = 'quit'
                    else:
                        menu.selected = 'start'
                    menu.print()

        # creating the event listener that will be used in the menu
        keyboard.on_press(
            lambda key, menu=self: key_handler(str(key)[14:-6], menu))

        # actually starting the menu
        self.print()
        while self.in_menu:
            continue

        # starting the game if the user did not choose to quit
        if not self.quiting:
            self.game_player.in_menu = False
            self.game_player.in_help = True
            self.game_player.help()
            while self.game_player.playing and self.game_player.food > 0:
                continue
            if self.game_player.food == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.game_player.update_map_and_chart()
                # belive it or not this says "YOU DIED"
                print(" __  __   ______   __  __       ______    ________  "
                      "______   ______\n/_/\\/_/\\ /_____/\\ /_/\\/_/\\     /"
                      "_____/\\  /_______/\\/_____/\\ /_____/\\\n\\ \\ \\ \\ "
                      "\\\\:::_ \\ \\\\:\\ \\:\\ \\    \\:::_ \\ \\ \\__.::._"
                      "\\/\\::::_\\/_\\:::_ \\ \\\n \\:\\_\\ \\ \\\\:\\ \\ \\ "
                      "\\\\:\\ \\:\\ \\    \\:\\ \\ \\ \\   \\::\\ \\  \\:\\/"
                      "___/\\\\:\\ \\ \\ \\\n  \\::::_\\/ \\:\\ \\ \\ \\\\:\\ "
                      "\\:\\ \\    \\:\\ \\ \\ \\  _\\::\\ \\__\\::___\\/_\\:"
                      "\\ \\ \\ \\\n    \\::\\ \\  \\:\\_\\ \\ \\\\:\\_\\:\\ "
                      "\\    \\:\\/.:| |/__\\::\\__/\\\\:\\____/\\\\:\\/.:| |"
                      "\n     \\__\\/   \\_____\\/ \\_____\\/     \\____/_/\\"
                      "________\\/ \\_____\\/ \\____/_/")

    def print(self):
        """prints the menu with an outline around the currently selected option
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.menu_options[self.selected])

    def execute_selection(self):
        """clears the terminal then executes the currently selected task
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.selected == 'quit':
            self.quiting = True
        self.in_menu = False


if __name__ == '__main__':
    game = menu()
