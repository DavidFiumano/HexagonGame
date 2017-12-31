from enum import Enum, unique

from glooey import *

from gameData import GlobalGameState, Game, gameObj
from menubutton import MenuButton

@unique
class MenuSubstate(Enum):
    MainMenu = 1 # for the main Menu Screen. Set to this by default in __init__
    GameCreation = 2 # for creating the game. Set to this when you click the "Play" button
    Options = 3 # for when the menu is in the main options menu
    VideoSettings = 4 # for when the menu is in the Video Settings menu
    GameSettings = 5 # for when the menu is in Game Settings
    TextureSettings = 6 # for when the game is in the texture settings
    Controls = 7 # for when the game is in the controls menu
    Quit = 8 # for when the menu is no longer on the screen. Only cleans memory associated with the menu.


class Menu:

    def __init__(self): # displays menu buttons which manage other things
        self.menuSubstate = MenuSubstate.MainMenu
        self.stateSwitched = True # used to determine if I have to clear the window.
        # Generally, it's better not to clear the window (I think) to avoid penalities associated with redrawing the frame. In these instances just pass so the cursor can be drawn

        self.menuGUI = Gui(gameObj.game_window, gameObj.drawBatch, gameObj.gui_layer) # gui is in the main game window, attached to the game drawBatch and on the uppermost user interaction layer that is appropriate
        # see gameData.py for additional documentation

        ## Button Definitions ##
        # button definitions are created witht he object and stored in memory during the Starting phase until the program exits
        # this is because the memory use is negligible and it should make the menu more responsive on most pcs

        self.PlayButton = MenuButton("Play!")

    def manage_main(self):
        if self.stateSwitched:
            # if the state has switched since the last time, drawn a new batch
            print("State switch observed")
            self.menuGUI.add(self.PlayButton)
            print("Added menu item")
            gameObj.drawBatch.add(self.menuGUI)
            print("Added to batch")
            self.stateSwitched = False
            gameObj.drawBatch.draw()
        else:
            pass

    def manage_GameCreation(self):
        pass # draw gui

    def manage_Options(self):
        pass # draw gui

    def manage_VideoSettings(self):
        pass # draw gui

    def manage_GameSettings(self):
        pass # draw gui

    def manage_TextureSettings(self):
        pass # draw gui

    def manage_Controls(self):
        pass # draw gui

    def manage_Quit(self):
        pass # clear screen, reset menuSubstate to MenuSubstate.MainMenu

    def handle_click(self):
        pass # different behavior depending on what substate the menu is in

    def handle_keystroke(self):
        pass # different behavior depending on what substate the menu is in

    def manage_menu(self): # manages the menu, handles substates, calls appropriate functions for each substate
        if self.menuSubstate == MenuSubstate.MainMenu:
            print(self.menuSubstate)
            try:
                self.manage_main()
            except Exception as e:
                print(e)
                exit()
            # self.menuSubstate = MenuSubstate.GameCreation # do things
        elif self.menuSubstate == MenuSubstate.GameCreation:
            print(self.menuSubstate)
            self.menuSubstate = MenuSubstate.Options # do things
        elif self.menuSubstate == MenuSubstate.Options:
            print(self.menuSubstate)
            self.menuSubstate = MenuSubstate.GameSettings # do things
        elif self.menuSubstate == MenuSubstate.GameSettings:
            print(self.menuSubstate)
            self.menuSubstate = MenuSubstate.TextureSettings # do things
        elif self.menuSubstate == MenuSubstate.TextureSettings:
            print(self.menuSubstate)
            self.menuSubstate = MenuSubstate.Controls # do things
        elif self.menuSubstate == MenuSubstate.Controls:
            print(self.menuSubstate)
            self.menuSubstate = MenuSubstate.Quit # do things
        elif self.menuSubstate == MenuSubstate.Quit:
            print(self.menuSubstate)
            self.menuSubstate = MenuSubstate.MainMenu
            gameObj.globalGameState = GlobalGameState.In_Game # do things
