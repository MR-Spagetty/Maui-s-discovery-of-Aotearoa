##
# maui.py
# MR-Spagetty

import keyboard
import random


class controls:
    def __init__(self, up, down, left, right, map, menu):
        """Base control setup

        Args:
            up (str): button to be associated with moving upwards.
            down (str): button to be associated with moving downwards.
            left (str): button to be associated with moving left.
            right (str): button to be associated with moving right.
            map (str): button to be associated with opening/closing the map.
            menu (str): button to be associated with opening/closing the menu.
        """
        self.up_control = up
        self.down_control = down
        self.left_control = left
        self.right_control = right
        self.map_button = map
        self.menu_button = menu

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

    def edit_map_button(self, map):
        """changes the button to be associated with the map.

        Args:
            map (str): new button to be associated with the map.
        """
        self.map_button = map


class map:
    def __init__(self, seed, dificulty):
        self.random = random
        self.random.seed(seed)
        self.dificulty = dificulty
        self.tiles = {}

    def generate_tile(self, turn_num, coordinates={'x': 0, 'y': 0}):
        if coordinates['y'] not in self.tiles.keys():
            self.tiles[coordinates['y']] = {}
        self.tiles[coordinates['y']][coordinates['x']] = self.tile(self,
                                                                   turn_num)

    def print(self, current_seen, view_distance, x, y):
        if view_distance == 2:
            r0 = current_seen[-2]
            r1 = current_seen[-1]
            r2 = current_seen[0]
            r3 = current_seen[1]
            r4 = current_seen[2]
            print(
                f"""
({x}, {y})
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
║{r2[-2][0]}║{r2[-1][0]}║{r2[0][0]}║{r2[1][0]}║{r2[2][0]}║
║{r2[-2][1]}║{r2[-1][1]}║{r2[0][1]}║{r2[1][1]}║{r2[2][1]}║
║{r2[-2][2]}║{r2[-1][2]}║{r2[0][2]}║{r2[1][2]}║{r2[2][2]}║
║{r2[-2][3]}║{r2[-1][3]}║{r2[0][3]}║{r2[1][3]}║{r2[2][3]}║
║{r2[-2][4]}║{r2[-1][4]}║{r2[0][4]}║{r2[1][4]}║{r2[2][4]}║
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
""")
        if view_distance == 1:
            r0 = current_seen[-1]
            r1 = current_seen[0]
            r2 = current_seen[1]
            print(
                f"""
({x}, {y})
╔═════════╦═════════╦═════════╗
║{r0[-1][0]}║{r0[0][0]}║{r0[1][0]}║
║{r0[-1][1]}║{r0[0][1]}║{r0[1][1]}║
║{r0[-1][2]}║{r0[0][2]}║{r0[1][2]}║
║{r0[-1][3]}║{r0[0][3]}║{r0[1][3]}║
║{r0[-1][4]}║{r0[0][4]}║{r0[1][4]}║
╠═════════╬═════════╬═════════╣
║{r1[-1][0]}║{r1[0][0]}║{r1[1][0]}║
║{r1[-1][1]}║{r1[0][1]}║{r1[1][1]}║
║{r1[-1][2]}║{r1[0][2]}║{r1[1][2]}║
║{r1[-1][3]}║{r1[0][3]}║{r1[1][3]}║
║{r1[-1][4]}║{r1[0][4]}║{r1[1][4]}║
╠═════════╬═════════╬═════════╣
║{r2[-1][0]}║{r2[0][0]}║{r2[1][0]}║
║{r2[-1][1]}║{r2[0][1]}║{r2[1][1]}║
║{r2[-1][2]}║{r2[0][2]}║{r2[1][2]}║
║{r2[-1][3]}║{r2[0][3]}║{r2[1][3]}║
║{r2[-1][4]}║{r2[0][4]}║{r2[1][4]}║
╚═════════╩═════════╩═════════╝
""")

    class tile:
        tile_types = ['sea', 'rock', 'island', 'whirlpool']

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
                map_obj (map_object): the parent map to be associated with
                this tile.

                turn_number (int): the current turn number to be used to
                determin the life of the tile.

                generated (bool, optional): weather or not the tile will be
                randomly generated. Defaults to True.

                tile_type (str, optional): used to determin what the type of
                this tile will be if not randomly generated. Defaults to None.
            """
            self.turn_created = turn_number

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
                    self.fish_delay = random.randint(2, 20)
                    self.remaining_delay = self.fish_delay
            if not self.generates_fish:
                self.fish_delay = 0

            self.has_fish = False

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
            if self.has_fish:
                player.fish_collected += 1
                self.has_fish = False
                self.remaining_delay = self.fish_delay

        def create_display(self):
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
        self.food_collected, self.view_distance = self.dificulty_starts[
            map_obj.dificulty]
        self.map = map_obj
        self.control_scheme = control_scheme
        self.coordinates = {'x': 0, 'y': 0}
        self.last_seen_chart = {}
        self.current_turn = 0

    def update_map_and_chart(self):
        current_seen = {}
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
                       *self.coordinates.values())


control_scheme = controls('w', 's', 'a', 'd', 'm', 'esc')
test_map = map(random.getrandbits(200), 2)
test_player = player(test_map, control_scheme)
test_player.update_map_and_chart()
