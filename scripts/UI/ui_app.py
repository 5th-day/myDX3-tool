# coding: UTF-8

# from PIL import Image
import flet as ft

from Application.character import *

# ##############################################################################################3#
class App:
    """ Fletを使ってGUIアプリケーション全体を管理するclass """
    page = None
    
    character : DX3Character = None
    
    def __init__(self) :
        self.assetsDir = "assets"
        
        App.character = DX3Character()
        
    def __del__(self) :
        pass

    def home(self, page: ft.Page) :
        App.page = page # クラス変数として管理
        
        # page の初期設定
        page.title = "DX3 Character Maker"
        page.theme_mode = ft.ThemeMode.LIGHT
        # page.bgcolor = ft.colors.WHITE
        page.scroll = ft.ScrollMode.AUTO
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
        ft.app( target = self.home, assets_dir=self.assetsDir )
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
        self.playerInfoUi  = PlayerInfoUi()
        self.lifepathUi    = LifepathUi()
        self.appearanceUi  = AppearanceUi()
        self.basicPointsUi = BasicPointsUi()
        self.abilityUi     = AbilityUi()
        self.bleedUi       = BleedUi()
        self.syndromeUi    = SyndromeUi()
        
        
    def build(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Column
                    (
                        [
                            ft.Row(
                                [
                                    self.personalityUi,
                                    ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                    ft.Column( [ self.playerInfoUi, self.lifepathUi ] ),
                                                    self.appearanceUi,
                                                ],
                                                vertical_alignment=ft.CrossAxisAlignment.START
                                            ),
                                            self.basicPointsUi
                                        ],
                                    ),
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.START,
                                wrap=True,
                            ),
                            self.abilityUi,
                        ],
                        wrap = True,
                        # expand=1
                    ),
                    ft.Column
                    (
                        [
                            ft.Row(
                                [
                                    self.bleedUi,
                                    self.syndromeUi,
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.START,
                            )
                        ],
                        # expand=1
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
                # 暫定的に画面全体を小さく表示して実装するために scale セット
                scale=0.60
            ),
            # width=self.containerWidth,
            bgcolor=ft.colors.GREY_200,
            border_radius=10,
        )
    
        
    
# ##############################################################################################3#
class PersonalityUi (ft.UserControl):
    """ キャラクターの個人情報・人格に関する情報 """
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
            self.worksSelBox.options.append( ft.dropdown.Option( key=id, text=Works.getDispName(id) ) )
        
        # callback
        
    def __initCover(self):
        # カヴァー
        self.coverStr = ft.Text( value="カヴァー", width=self.itemNameWidth )
        self.coverSelBox = ft.Dropdown()
        
        self.coverSelBox.witdh = self.fieldWidth
        
        # list itemの登録
        self.coverSelBox.options.append( ft.dropdown.Option( " " ) )
        for id in eWorks :
            self.coverSelBox.options.append( ft.dropdown.Option( key=id, text=Works.getDispName(id) ) )
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
        self.bodyHeightField.on_blur = self.heightOnEdit
        
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
    
    def heightOnEdit(self, e):
        pass
    
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
        self.expField.on_blur = self.expFiledOnEdited
        

    def expFiledOnEdited(self, e):
        pass
        
# ###############################################################################################
class LifepathUi(ft.UserControl):
    """ ライフパス情報 """
    def __init__(self):
        super().__init__()
        # define
        self.containerWidth = 500
        self.itemNameWidth = 100
        self.itemNameWidthSmall = 75
        self.fieldWidth = 300
        
        # init
        self.__initLifePathStr()
        self.__initBirthPlace()
        self.__initExperience()
        self.__initEncount()
        self.__initArousal()
        self.__initImpulse()
        self.__initErodedVal()
        
    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Row( [self.lifepathStr]  ),
                ft.Row( self.birthPlace.row ),
                ft.Row( self.experience.row ),
                ft.Row( self.encount.row    ),
                ft.Row( self.arousal.row    ),
                ft.Row( self.impulse.row    ),
                ft.Row( self.erodedValRow   ),
            ],),
            width=self.containerWidth,
            bgcolor=ft.colors.YELLOW,
        )
    
    class LifePathItem:
        def __init__(self, dispStr : str, itemList : list = [], callbackOnChange =  None):
            self.dispStr = ft.Text( value = dispStr)
            self.itemSelBox = ft.Dropdown()

            self.itemSelBox.width = 400
            
            self.row = [ self.dispStr, self.itemSelBox ]

            # list itemの登録
            self.itemSelBox.options.append( ft.dropdown.Option( " " ) )
            self.setItemList( itemList )
            
            # callback
            self.itemSelBox.on_change = callbackOnChange
        
        def __del__(self):
            pass
        
        def setItemList( self, itemList : list ) :
            for item in itemList :
                self.itemSelBox.options.append( ft.dropdown.Option( item ) )
                
        def clearItemList( self ):
            self.itemSelBox.options.clear()
            self.itemSelBox.options.append( ft.dropdown.Option( " ") )

    def __initLifePathStr(self):
        # 出自
        self.lifepathStr = ft.Text("ライフパス")
        # callback
        
    def __initBirthPlace(self):
        # 出自
        self.birthPlace = self.LifePathItem("出自", callbackOnChange=self.birthPaceOnChanged)
        # callback
        
    def __initExperience(self):
        # 経験
        self.experience = self.LifePathItem("経験", callbackOnChange=self.experienceOnChanged)
        # callback
        
    def __initEncount(self):
        # 邂逅
        self.encount = self.LifePathItem("邂逅", callbackOnChange=self.encountOnChanged)
        # callback
        
    def __initArousal(self):
        # 覚醒
        self.arousal = self.LifePathItem("覚醒", callbackOnChange=self.arousalOnChanged)
        # callback
        
    def __initImpulse(self):
        # 衝動
        self.impulse = self.LifePathItem("衝動", callbackOnChange=self.impulseOnChanged)
        # callback
        
    def __initErodedVal(self):
        # 侵食率基礎値
        self.erodedValSpace = ft.Text( "" )
        self.erodedValStr = ft.Text( "侵食率基礎値" )
        self.erodedValField = ft.TextField( value=0, disabled=True)
        
        self.erodedValRow = [ self.erodedValSpace, self.erodedValStr, self.erodedValField ]
        
    def birthPaceOnChanged(self, e):
        pass
        
    def experienceOnChanged(self, e):
        pass
        
    def encountOnChanged(self, e):
        pass
        
    def arousalOnChanged(self, e):
        pass
        
    def impulseOnChanged(self, e):
        pass
        
# ###############################################################################################
class AppearanceUi(ft.UserControl):
    """ キャラクターアイコン """
    def __init__(self):
        super().__init__()
        # define
        self.containerWidth = 200
        self.imgWidth = self.containerWidth
        self.imgHeight = self.imgWidth
        
        # init
        self.__initAppearanceStr()
        self.__initAppearanceImage()
        
    def build(self):
        return ft.Container(
            content=ft.Column([
                self.str,
                self.imgFrame
            ],),
            width=self.containerWidth,
            bgcolor=ft.colors.YELLOW,
        )
    
    def __initAppearanceStr(self):
        self.str = ft.Text("外見")

    def __initAppearanceImage(self):
        self.img = ft.Image(
            src=f"/images/person.svg",
            width=self.imgWidth, height=self.imgHeight,
            color=ft.colors.GREY_600,
            fit=ft.ImageFit.FIT_WIDTH,
            border_radius=10,
        )
        
        self.imgFrame = ft.Container(
            self.img,
            bgcolor=ft.colors.AMBER_100,
        )
        self.imgFrame.on_click = self.appearanceOnClicked
        
        # 画像ファイルPicker　Instance
        # openFilePicker()の度にインスタンスを生成すると都度appendすることになるのでここで生成しておく
        self.pickFileDialog = ft.FilePicker(on_result=self.filePickerOnResult)
        App.page.overlay.append( self.pickFileDialog )
        
    def appearanceOnClicked(self,e):
        self.openFilePicker()
    
    def openFilePicker(self):
        self.pickFileDialog.pick_files(file_type=ft.FilePickerFileType.IMAGE)
        
    def filePickerOnResult(self, e : ft.FilePickerResultEvent):
        if e.files is None:
            print("canceled")
            return
        self.setImage(e.files[0].path)
    
    def setImage(self, path: str = None, data = None):
        if path is not None:
            self.img.src = path
        elif data is not None:
            # Image Object ->　ft.Image
            pass
        else :
            return
        
        self.img.color = None
        self.img.update()
        
# ###############################################################################################
class BasicPointsUi(ft.UserControl):
    """ 副能力値 HP最大値など """
    def __init__(self):
        super().__init__()
        # define
        self.containerWidth = 500
        
        # init
        self.__initMaxHpUi()
        self.__initRegularStockUi()
        self.__initBattleMoveUi()
        self.__initMovePointUi()
        self.__initWalletPointUi()
        self.__initFullPowerMoveUi()
        
    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Row(
                    [
                        self.maxHpUi,
                        self.regularStockUi,
                        self.BattleMoveUi,
                    ],
                ),
                ft.Row(
                    [
                        self.movePointUi,
                        self.walletPointUi,
                        self.fullPowerUi,
                    ],
                ),
            ],),
            width=self.containerWidth,
            bgcolor=ft.colors.YELLOW,
        )
    
    def __initMaxHpUi(self):
        self.maxHpUi = BasicPointsItem("外見","肉体","精神" )

    def __initRegularStockUi(self):
        self.regularStockUi = BasicPointsItem("常備化P","社会","調達" )
    
    def __initBattleMoveUi(self):
        self.BattleMoveUi = BasicPointsItem("戦闘移動","行動値",None )
    
    def __initMovePointUi(self):
        self.movePointUi = BasicPointsItem("行動値","感覚","精神" )
    
    def __initWalletPointUi(self):
        self.walletPointUi = BasicPointsItem("財産P","常備化P","使用P" )
    
    def __initFullPowerMoveUi(self):
        self.fullPowerUi = BasicPointsItem("全力移動","戦闘移動",None )
    
class BasicPointsItem(ft.UserControl):
    """ HP最大値など """
    def __init__(self, dispStr : str, prm1str : str, prm2str : str = None, ):
        super().__init__()
        # define
        self.prmWidth = 50
        
        # vars
        self.dispStr = ft.Text( value = dispStr )
        self.prm1Str = ft.Text( value = prm1str )
        self.prm1Field  = ft.TextField( value=0, read_only=True )
        
        self.existPrm2 = False if prm2str is None else True
        
        self.prm2Str = ft.Text( value = prm2str )
        self.prm2Field  = ft.TextField( value=0, read_only=True )
        
        self.total = ft.TextField( value=0, read_only=True )
        self.total.width = self.prmWidth

        # callback
    
    def build(self):
        prm1Frame = ft.Column([ self.prm1Str, self.prm1Field ], width=self.prmWidth )
        prm2Frame = ft.Column([ self.prm2Str, self.prm2Field ], width=self.prmWidth )
        
        prmList = [ prm1Frame ]
        
        if self.existPrm2 :
            prmList.append( prm2Frame )
        
        return ft.Container(
            ft.Column([
                ft.Row( [
                    ft.Column( [
                        self.dispStr,
                        ft.Row(prmList),
                    ], ),
                    self.total,
                ], )
            ], ),
            bgcolor=ft.colors.BLUE_50,
        )

# ###############################################################################################
class AbilityUi(ft.UserControl):
    """ 能力値 """
    def __init__(self):
        super().__init__()
        # define
        self.containerWidth = 1000
        
        # init
        self.__initAbilityStr()
        self.__initBodyUi()
        self.__initSenseUi()
        self.__initMentalUi()
        self.__initSocialityUi()
        
    def build(self):
        return ft.Container(
            content=ft.Column([
                self.abilityStr,
                ft.Row(
                    [
                        # self.bodyUi,
                        # self.senseUi,
                        # self.mentalUi,
                        # self.socialityUi
                    ],
                ),
            ],),
            width=self.containerWidth,
            bgcolor=ft.colors.YELLOW,
        )
    
    def __initAbilityStr(self):
        self.abilityStr = ft.Text("能力値", bgcolor=ft.colors.GREY_100)

    def __initBodyUi(self):
        self.bodyUi = abilityItemUi()

    def __initSenseUi(self):
        self.senseUi = abilityItemUi()
    
    def __initMentalUi(self):
        self.mentalUi = abilityItemUi()
    
    def __initSocialityUi(self):
        self.socialityUi = abilityItemUi()
    
class abilityItemUi(ft.UserControl):
    """ 技能パラメータ """
    def __init__(self, ):
        super().__init__()
        # define
        
        # vars

        # callback
    
    def build(self):
        pass
    

# ###############################################################################################
class BleedUi(ft.UserControl):
    """ ブリード """
    def __init__(self):
        super().__init__()
        # define
        self.containerWidth = 250
        
        # init
        self.__initBleedStr()
        self.__initBleedSelBox()
        
    def build(self):
        return ft.Container(
            content=ft.Column([
                        self.bleedStr,
                        self.bleedSelBox,
            ],),
            width=self.containerWidth,
            bgcolor=ft.colors.ORANGE,
        )
    
    def __initBleedStr(self):
        self.bleedStr = ft.Text("ブリード")

    def __initBleedSelBox(self):
        self.bleedSelBox = ft.Dropdown()
        
        self.bleedSelBox.options.append( ft.dropdown.Option(" "))
    
class SyndromeUi(ft.UserControl):
    """ シンドローム """
    def __init__(self, ):
        super().__init__()
        # define
        
        # init
        self.__initSyndromeStr()
        self.__initSyndromItems()

        # callback
    
    def build(self):
        return ft.Container( 
            content=ft.Column(
                [
                    self.syndromeStr,
                    ft.Row(
                        self.syndromeItems,
                    ),
                ],
            ),
            # width=self.containerWidth,
            bgcolor=ft.colors.YELLOW,
        )
    
    def __initSyndromeStr(self):
        self.syndromeStr = ft.Text("シンドローム")
        
    def __initSyndromItems(self):
        self.syndromeItem1 = SyndromeItem()
        self.syndromeItem2 = SyndromeItem()
        self.syndromeItem3 = SyndromeItem()
        
        self.syndromeItem3.selBox.label = "optional"
        
        self.syndromeItems = [
                self.syndromeItem1,
                self.syndromeItem2,
                self.syndromeItem3,
            ]
        
class SyndromeItem(ft.UserControl):
    """ シンドローム """
    def __init__(self):
        super().__init__()
        # define
        
        # init
        self.__initSyndromeItem()

        # callback
    
    def build(self):
        return self.selBox
    
    def __initSyndromeItem(self):
        self.selBox = ft.Dropdown()
        
        self.selBox.options.append(ft.dropdown.Option(" ") )
        
    

# ###############################################################################################

def run():
    app = App()
    app.run()

if __name__ == "__main__":
    run()