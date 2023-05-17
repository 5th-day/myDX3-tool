# coding: UTF-8

import flet as ft
from Application.character import *


class App:
    """ Fletを使ってGUIアプリケーション全体を管理するclass """
    page = None
    
    def __init__(self) :
        self.character = DX3Character()
        
        self.__initUiParts()

    def __del__(self) :
        pass

    def __initUiParts(self) :
        # キャラクター基本情報入力枠
        self.personalityUi = PersonalityUi()
        
    def home(self, page: ft.Page) :
        App.page = page # クラス変数として管理
        
        page.title = "DX3 Character Maker"
        # page.bgcolor = ft.colors.WHITE

        # parts
        page.controls.append( self.personalityUi )
        # function

        # update
        page.update()

    def run(self) :
        ft.app( target = self.home )
        # ft.app( target = self.home, port=8550, view=ft.WEB_BROWSER ) # WEB BORWSER で起動
        
        
    

class PersonalityUi (ft.UserControl):
    """ sample """
    def __init__(self):
        super().__init__()
        self.containerWidth = 500
        self.itemNameWidth = 100
        self.fieldWidth = 300
        
        
        self.__initCharaName()
        self.__initCodeName()
        self.__initWorks()
        self.__initCover()
        
    def build(self):
        # return ft.Container(
        #     ft.DataTable(
        #         columns=[
        #             ft.DataColumn(ft.Text("")),
        #             ft.DataColumn(ft.Text("")),
        #         ],
        #         rows=[
        #             ft.DataRow( cells = [ ft.DataCell( self.charaNameStr ), ft.DataCell( self.charaNameField ) ]),
        #             ft.DataRow( cells = [ ft.DataCell( self.charaNameStr ), ft.DataCell( self.charaNameField ) ]),
        #             ft.DataRow( cells = [ ft.DataCell( self.worksStr )    , ft.DataCell(self.worksSelBox)      ]),
        #             ft.DataRow( cells = [ ft.DataCell( self.worksStr )    , ft.DataCell(self.worksSelBox)      ]),
        #         ],
        #     ),
        #     width=self.containerWidth,
        #     padding=30,
        # )
        return ft.Container(
            content=ft.Column([
                ft.Row( [ self.charaNameStr, self.charaNameField ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.codeNameStr , self.codeNameField  ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.worksStr    , self.worksSelBox    ], alignment=ft.MainAxisAlignment.CENTER ),
                # ft.Row( [ self.coverStr    , self.coverSelBox    ], alignment=ft.MainAxisAlignment.CENTER ),
                self.coverRow,
            ],),
            width=self.containerWidth,
        )
    
    def __initCharaName(self):
        # キャラクター名
        self.charaNameStr = ft.Text( value="氏名", width=self.itemNameWidth)
        self.charaNameField = ft.TextField()
        self.charaNameField.width = self.fieldWidth
        
    def __initCodeName(self):
        # コードネーム
        self.codeNameStr = ft.Text( value="コードネーム", width=self.itemNameWidth, tooltip="任意")
        self.codeNameField = ft.TextField()
        self.codeNameField.width = self.fieldWidth
        
        
    def __initWorks(self):
        # ワークス選択リスト
        self.worksStr = ft.Text( value="ワークス", width=self.itemNameWidth )
        self.worksSelBox = ft.Dropdown()

        self.worksSelBox.width = self.fieldWidth

        # list itemの登録
        self.worksSelBox.options.append( ft.dropdown.Option( " " ) )
        for id in eWorks :
            self.worksSelBox.options.append( ft.dropdown.Option( Works.getDispName(id) ) )
        
    def __initCover(self):
        # カヴァー
        self.coverStr = ft.Text( value="カヴァー", width=self.itemNameWidth, tooltip="任意")
        self.coverSelBox = ft.Dropdown()
        
        self.coverSelBox.witdh = self.fieldWidth
        
        # list itemの登録
        self.coverSelBox.options.append( ft.dropdown.Option( " " ) )
        for id in eWorks :
            self.coverSelBox.options.append( ft.dropdown.Option( Works.getDispName(id) ) )
        self.coverSelBox.options.append( ft.dropdown.Option( "その他" ) )
        
        self.coverSelBox.on_change = self.coverOnChange
        
    def coverOnChange(self, e):
        if ( self.coverSelBox.value == "その他" ):
            pass
        else:
            pass
        App.page.update()
        

def run():
    app = App()
    app.run()

if __name__ == "__main__":
    run()