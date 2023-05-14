# coding: UTF-8

import flet as ft
from Application.character import *


class App:
    """ Fletを使ってGUIアプリケーション全体を管理するclass """
    def __init__(self) :
        self.character = DX3Character()
        
        self.__initUiParts()

    def __del__(self) :
        pass

    def __initUiParts(self) :
        self.worksStr = ft.Text( value="Works: " )
        self.worksSelBox = ft.Dropdown()

        self.worksSelBox.width = 500

        for id in eWorks :
            self.worksSelBox.options.append( ft.dropdown.Option( Works.getDispName(id) ) )
        

    def home(self, page: ft.Page) :
        page.title = "DX3 Character Maker"

        # parts
        page.controls.append( self.worksStr )
        page.controls.append( self.worksSelBox )

        # function

        # update
        page.update()

    def run(self) :
        ft.app( target = self.home )
        # ft.app( target = home, view=ft.WEB_BROWSER ) # WEB BORWSER で起動
    
    # @classmethod
    # def run(cls) :
    #     pass



def run():
    app = App()
    app.run()

if __name__ == "__main__":
    run()