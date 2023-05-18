# coding: UTF-8

import flet as ft
from Application.character import *

# ##############################################################################################3#
class App:
    """ Fletを使ってGUIアプリケーション全体を管理するclass """
    page = None
    
    def __init__(self) :
        self.character = DX3Character()
        
    def __del__(self) :
        pass

    def __initUiParts(self) :
        # キャラクター基本情報入力枠
        self.personalityUi = PersonalityUi()
        self.playerInfoUi = PlayerInfoUi()
        
    def home(self, page: ft.Page) :
        App.page = page # クラス変数として管理
        
        # page の初期設定
        page.title = "DX3 Character Maker"
        page.theme_mode = ft.ThemeMode.LIGHT
        # page.bgcolor = ft.colors.WHITE
        page.scroll = auto
        # page.window_width = 
        # page.window_height = 
        # page.theme = ft.Theme(color_scheme_seed="green")
        # page.window_full_screen = True
        # page.window_maximized = True
        page.window_center()

        # ページ全体のレイアウトを管理するクラスインスタンス
        self.layout = PageLayout()

        # widgets
        page.controls.append( self.layout )
        
        # function

        # update
        page.update()

    def run(self) :
        ft.app( target = self.home )
        # ft.app( target = self.home, port=8550, view=ft.WEB_BROWSER ) # WEB BORWSER で起動
        

# ##############################################################################################3#
class PageLayout(ft.UserControl):
    """ ページ全体のレイアウトを決めるクラス """
    def __init__(self):
        super().__init__()
        # define
        self.containerWidth = App.page.window_width
        
        # init
        self.__initUiParts()

    def __initUiParts(self) :
        # キャラクター基本情報入力枠
        self.personalityUi = PersonalityUi()
        self.playerInfoUi = PlayerInfoUi()
        
        
    def build(self):
        return ft.Container(
            content=ft.Column
            (
                [ ft.Row([self.personalityUi, self.playerInfoUi], vertical_alignment=ft.CrossAxisAlignment.START, wrap=True), ],
            ),
            # width=self.containerWidth,
            bgcolor=ft.colors.GREY_200,
            border_radius=10,
        )
    
        
    
# ##############################################################################################3#
class PersonalityUi (ft.UserControl):
    """ sample """
    def __init__(self):
        super().__init__()
        # define
        self.containerWidth = 500
        self.itemNameWidth = 100
        self.itemNameWidthSmall = 75
        self.fieldWidth = 300
        
        # init
        self.__initCharaName()
        self.__initCodeName()
        self.__initWorks()
        self.__initCover()
        self.__initAge()
        self.__initGender()
        self.__initZodiacSign()
        self.__initBodyHeight()
        self.__initBodyWeight()
        self.__initBloodType()
        self.__initMemo()
        
        # list
        self.fieldList = [
            self.charaNameField,
            self.codeNameField,
            self.worksSelBox,
            self.coverSelBox,
            self.ageField,
            self.genderField,
            self.zodiacSignField,
            self.bodyHeightField,
            self.bodyWeightField,
            self.bloodTypeField,
            self.memoField
        ]
        
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
                ft.Row( [ self.charaNameStr  , self.charaNameField  ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.codeNameStr   , self.codeNameField   ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.worksStr      , self.worksSelBox     ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.coverStr      , self.coverSelBox     ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.ageStr        , self.ageField        , self.genderStr    ,self.genderField     , self.zodiacSignStr,self.zodiacSignField ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.bodyHeightStr , self.bodyHeightField , self.bodyWeightStr,self.bodyWeightField, self.bloodTypeStr  ,self.bloodTypeField  ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.memoStr       , self.memoField       ], alignment=ft.MainAxisAlignment.CENTER ),
            ],),
            width=self.containerWidth,
            bgcolor=ft.colors.AMBER,
        )
    
    def __initCharaName(self):
        # キャラクター名
        self.charaNameStr = ft.Text( value="氏名", width=self.itemNameWidth, )
        self.charaNameField = ft.TextField()
        self.charaNameField.width = self.fieldWidth
        
        # callback
        self.charaNameField.on_blur = ""
        
    def __initCodeName(self):
        # コードネーム
        self.codeNameStr = ft.Text( value="コードネーム", width=self.itemNameWidth )
        self.codeNameField = ft.TextField()
        self.codeNameField.width = self.fieldWidth
        
        # callback
        
    def __initWorks(self):
        # ワークス選択リスト
        self.worksStr = ft.Text( value="ワークス", width=self.itemNameWidth )
        self.worksSelBox = ft.Dropdown()

        self.worksSelBox.width = self.fieldWidth

        # list itemの登録
        self.worksSelBox.options.append( ft.dropdown.Option( " " ) )
        for id in eWorks :
            self.worksSelBox.options.append( ft.dropdown.Option( Works.getDispName(id) ) )
        
        # callback
        
    def __initCover(self):
        # カヴァー
        self.coverStr = ft.Text( value="カヴァー", width=self.itemNameWidth )
        self.coverSelBox = ft.Dropdown()
        
        self.coverSelBox.witdh = self.fieldWidth
        
        # list itemの登録
        self.coverSelBox.options.append( ft.dropdown.Option( " " ) )
        for id in eWorks :
            self.coverSelBox.options.append( ft.dropdown.Option( Works.getDispName(id) ) )
        self.coverSelBox.options.append( ft.dropdown.Option( "その他" ) )
        
        # callback
        self.coverSelBox.on_change = self.coverOnChange
        
    def __initAge(self) :
        # 年齢
        self.ageStr = ft.Text( value="年齢", width=self.itemNameWidthSmall )
        self.ageField = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER)
        self.ageField.width = self.itemNameWidthSmall
        
        # callback
        
    def __initGender(self) :
        # 性別
        self.genderStr = ft.Text( value="性別", width=self.itemNameWidthSmall )
        self.genderField = ft.TextField()
        self.genderField.width = self.itemNameWidthSmall
        
        # callback
        
    def __initZodiacSign(self) :
        # 星座
        self.zodiacSignStr = ft.Text( value="星座", width=self.itemNameWidthSmall )
        self.zodiacSignField = ft.TextField()
        self.zodiacSignField.width = self.itemNameWidthSmall
        
        # callback
        
    def __initBodyHeight(self) :
        # 身長
        self.bodyHeightStr = ft.Text( value="身長", width=self.itemNameWidthSmall )
        self.bodyHeightField = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, suffix_text="cm")
        self.bodyHeightField.width = self.itemNameWidthSmall
        
        # callback
        
    def __initBodyWeight(self) :
        # 体重
        self.bodyWeightStr = ft.Text( value="体重", width=self.itemNameWidthSmall )
        self.bodyWeightField = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, suffix_text="kg")
        self.bodyWeightField.width = self.itemNameWidthSmall
        
        # callback
        
    def __initBloodType(self) :
        # 血液型
        self.bloodTypeStr = ft.Text( value="血液型", width=self.itemNameWidthSmall )
        self.bloodTypeField = ft.TextField()
        self.bloodTypeField.width = self.itemNameWidthSmall
        
        # callback
        
    def __initMemo(self):
         # メモ
        self.memoStr = ft.Text( value="メモ", width=self.itemNameWidthSmall )
        self.memoField = ft.TextField(multiline=True)
        
        self.memoField.witdh  = self.fieldWidth + ( self.itemNameWidth - self.itemNameWidthSmall )
        # self.memoField.height = 500
        self.memoField.text_align = ft.TextAlign.START
        self.memoField.min_lines = 3
        self.memoField.max_lines = 3

        
        # callback
        self.memoField.on_blur   = self.memoFieldOnEdited
        # self.memoField.on_submit = self.memoFieldEdited
        
       
    def coverOnChange(self, e):
        if ( self.coverSelBox.value == "その他" ):
            pass
        else:
            pass
        App.page.update()
    
    def memoFieldOnEdited(self, e):
        pass

# ##############################################################################################3#
class PlayerInfoUi(ft.UserControl):
    """ プレイヤー情報 """
    def __init__(self):
        super().__init__()
        # define
        self.containerWidth = 500
        self.itemNameWidth = 100
        self.itemNameWidthSmall = 75
        self.fieldWidth = 300
        
        # init
        self.__initPlayerName()
        self.__initExp()
        
    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Row( [ self.plNameStr , self.plNameField ], alignment=ft.MainAxisAlignment.CENTER ),
                ft.Row( [ self.expSpace  , self.expStr    , self.expField    ], alignment=ft.MainAxisAlignment.CENTER ),
            ],),
            width=self.containerWidth,
            bgcolor=ft.colors.YELLOW,
        )
    
    def __initPlayerName(self):
        # プレイヤー名
        self.plNameStr = ft.Text( value="PL", width=self.itemNameWidth )
        self.plNameField = ft.TextField()
        self.plNameField.width = self.fieldWidth
        
        # callback
        self.plNameField.on_blur = ""
        
    def __initExp(self):
        # 使用経験点
        self.expSpace = ft.Text( value="", width=self.itemNameWidth )
        self.expStr = ft.Text( value="使用経験点", width=self.itemNameWidth )
        self.expField = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER)

        self.expField.width = self.fieldWidth - self.itemNameWidth
        
        # callback
        

    def memoFieldOnEdited(self, e):
        pass
        

def run():
    app = App()
    app.run()

if __name__ == "__main__":
    run()