from pyglet import *

from os import path
from enum import Enum, unique

@unique
class GlobalGameState(Enum):
    Starting = 1 # handled by starting.py
    Loading_Screen = 2 # When loading in the beginning, possibly not needed on faster pcs
    Menu = 3 # all substates of menu are handled by the menu_state class
    In_Game = 4 # all substates of _In_Game are handled by the GameState class
    Closing = 5 # if the window is closing

    # Misc States
    Hard_Paused = 6 # if the game is paused/not supposed to load: Potentially when the game is alt+tabbed

class Game:

    def __init__(self):

        ## GAME DEFINITIONS ##

        self.gameSettings = None # gameSettings are uninited until set_settings is called
        self.settings_initialized = False # makes sure settings are only set once
        self.game_settings_path = path.join('settings', 'game.settings') # where game.settings is stored
        self.mod_settings_path = path.join('settings', 'mod.settings') # where mod.settings is stored

        ## GRAPHICS DEFINITIONS ##

        self.drawBatch = graphics.Batch() # everything to be drawn is drawn into this

        self.background_layer = graphics.OrderedGroup(0) # layer on which the background is drawn (usually ocean)
        self.land_layer = graphics.OrderedGroup(1) # layer on which the land is drawn
        self.terrain_feature_layer = graphics.OrderedGroup(2) # layer on which terrain/cities features are drawn
        self.city_status_layer = graphics.OrderedGroup(3) # layer on which city statuses are drawn (units garrisoned in cities are listed here to enable us to click the city when they are garrisoned)
        self.highlight_layer = graphics.OrderedGroup(4) # layer on which terrain highlights to denote player territory are drawn
        self.action_layer = graphics.OrderedGroup(5) # layer on which actions are drawn (below unit layer to enable planes and icons to move across them)
        self.bottom_unit_layer = graphics.OrderedGroup(6) # layer on which land and sea units are drawn
        self.top_unit_layer = graphics.OrderedGroup(7) # layer on which air units are drawn
        self.unit_highlight_layer = graphics.OrderedGroup(8) # layer on which unit highlights (AOE indicators) are drawn.
        self.gui_layer = graphics.OrderedGroup(9) # for gui
        self.err_layer = graphics.OrderedGroup(10) # for errors I may wish to display (may be unimplemented)
        self.pause_layer = graphics.OrderedGroup(11) # for pausing the game. Allows the player to safely exit in the event of non-fatal errors

        ## WINDOW INITIALIZATION ##

        self.game_window = window.Window(visible = False) # the window that is drawn on

        ## SET GAMESTATE ##

        self.globalGameState = GlobalGameState.Starting # gamestate of the game as a whole, used to ensure that the proper code is run in each loop

    def set_settings(self, settings):
        # recieves [settings], which is a dictionary according to the following format:
        # [key] : (Value, Value1, Value2, ...)
        if not(self.settings_initialized):
            self.settings_initialized = True
            self.gameSettings = settings
        else:
            return None

    def get_setting(self, setting):
        # setting is the key of the setting in {settings}
        # run in a try a catch block unless 100% sure this will succeed
        # returns a string, regardless of the setting
        return self.gameSettings[setting]

    def get_setting_dict(self, setting):
        # returns all the settings at once
        # useful for me
        # returns a reference. The ingegrity of this is not managed
        return self.gameSettings

    def set_setting(self, setting, value):
        # sets the value of an individual setting
        # returns -1 and prints if a setting is invalid and the change was not made
        if setting in self.gameSettings.keys():
            self.gameSettings[setting] = value
        else:
            print("Failed: setting ", setting, " to ", value)
            return -1



gameObj = Game()
