# coding: UTF-8

from typing import Literal, Callable
import flet as ft

from Application.character_attributes import *
from Application.character import DX3Character, SkillPrm


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
        # ft.app( target = self.home, assets_dir=self.assetsDir, view=ft.WEB_BROWSER ) # WEB BORWSER で起動
        

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
        self.basicPointsUi = SubAbilityUi()
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
                scroll = ft.ScrollMode.AUTO,
                # 暫定的に画面全体を小さく表示して実装するために scale セット
                # scale=0.60,
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
            self.coverField,
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
                ft.Row( [ self.coverStr      , self.coverField      ], alignment=ft.MainAxisAlignment.CENTER ),
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
        self.charaNameField = ft.TextField( value=App.character.getCharacterName() )
        self.charaNameField.width = self.fieldWidth
        
        # observerに登録
        App.character.bind( id = ePrmId.charName, callback=self.updateCharaName )
        # callback
        self.charaNameField.on_blur = lambda e : App.character.setCharacterName(e.control.value)
        
    def __initCodeName(self):
        # コードネーム
        self.codeNameStr = ft.Text( value="コードネーム", width=self.itemNameWidth )
        self.codeNameField = ft.TextField()
        self.codeNameField.width = self.fieldWidth
        
        # observerに登録
        App.character.bind( id = ePrmId.codeName, callback=self.updateCodeName )
        # callback
        self.charaNameField.on_blur = lambda e : App.character.setCodeName(e.control.value)
        
    def __initWorks(self):
        # ワークス選択リスト
        self.worksStr = ft.Text( value="ワークス", width=self.itemNameWidth )
        self.worksSelBox = ft.Dropdown()

        self.worksSelBox.width = self.fieldWidth

        # list itemの登録
        # self.worksSelBox.options.append( ft.dropdown.Option( " " ) )
        for id in eWorks :
            self.worksSelBox.options.append( ft.dropdown.Option( key=id, text=Works.getDispName(id) ) )
        
        # observerに登録
        App.character.bind( id = ePrmId.works, callback=self.updateCharaName )
        # callback
        self.worksSelBox.on_change = lambda e : App.character.setWorkws( int(e.control.value) )
        
    def __initCover(self):
        # カヴァー
        self.coverStr = ft.Text( value="カヴァー", width=self.itemNameWidth )
        self.coverField = ft.TextField()
        
        self.coverField.witdh = self.fieldWidth
        
        # observerに登録
        App.character.bind( id = ePrmId.cover, callback=self.updateCover )
        # callback
        self.coverField.on_blur = lambda e : App.character.setCover(e.control.value)
        
    def __initAge(self) :
        # 年齢
        self.ageStr = ft.Text( value="年齢", width=self.itemNameWidthSmall )
        self.ageField = ft.TextField( keyboard_type=ft.KeyboardType.NUMBER, suffix_text="歳" )
        self.ageField.width = self.itemNameWidthSmall
        
        # observerに登録
        App.character.bind( id = ePrmId.cover, callback=self.updateAge )
        # callback
        self.ageField.on_blur = lambda e : App.character.setAge( int(e.control.value) )
        
    def __initGender(self) :
        # 性別
        self.genderStr = ft.Text( value="性別", width=self.itemNameWidthSmall )
        self.genderField = ft.TextField()
        self.genderField.width = self.itemNameWidthSmall
        
        # observerに登録
        App.character.bind( id = ePrmId.gender, callback=self.updateGender )
        # callback
        self.ageField.on_blur = lambda e : App.character.setGender( e.control.value )
        
    def __initZodiacSign(self) :
        # 星座
        self.zodiacSignStr = ft.Text( value="星座", width=self.itemNameWidthSmall )
        self.zodiacSignField = ft.TextField()
        self.zodiacSignField.width = self.itemNameWidthSmall
        
        # observerに登録
        App.character.bind( id = ePrmId.zodiacSign, callback=self.updateZodiacSign )
        # callback
        self.ageField.on_blur = lambda e : App.character.setZodiacSign( e.control.value )
        
    def __initBodyHeight(self) :
        # 身長
        self.bodyHeightStr = ft.Text( value="身長", width=self.itemNameWidthSmall )
        self.bodyHeightField = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, suffix_text="cm")
        self.bodyHeightField.width = self.itemNameWidthSmall
        
        # observerに登録
        App.character.bind( id = ePrmId.bodyHeight, callback=self.updateBodyHeight )
        # callback
        self.bodyHeightField.on_blur = lambda e : App.character.setBodyHeight( int( e.control.value ) )
        
    def __initBodyWeight(self) :
        # 体重
        self.bodyWeightStr = ft.Text( value="体重", width=self.itemNameWidthSmall )
        self.bodyWeightField = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, suffix_text="kg")
        self.bodyWeightField.width = self.itemNameWidthSmall
        
        # observerに登録
        App.character.bind( id = ePrmId.bodyWeight, callback=self.updateBodyWeight )
        # callback
        self.bodyWeightField.on_blur = lambda e : App.character.setBodyWeight( int( e.control.value ) )
        
    def __initBloodType(self) :
        # 血液型
        self.bloodTypeStr = ft.Text( value="血液型", width=self.itemNameWidthSmall )
        self.bloodTypeField = ft.TextField()
        self.bloodTypeField.width = self.itemNameWidthSmall
        
        # observerに登録
        App.character.bind( id = ePrmId.bloodType, callback=self.updateBloodType )
        # callback
        self.bloodTypeField.on_blur = lambda e : App.character.setBloodType( e.control.value )
        
    def __initMemo(self):
         # メモ
        self.memoStr = ft.Text( value="メモ", width=self.itemNameWidthSmall )
        self.memoField = ft.TextField(multiline=True)
        
        self.memoField.witdh  = self.fieldWidth + ( self.itemNameWidth - self.itemNameWidthSmall )
        # self.memoField.height = 500
        self.memoField.text_align = ft.TextAlign.START
        self.memoField.min_lines = 3
        self.memoField.max_lines = 3

        # observerに登録
        App.character.bind( id = ePrmId.memo, callback=self.updateMemoField )
        # callback
        self.memoField.on_blur = lambda e : App.character.setMemo( e.control.value )
        
    def updateCharaName(self):
        self.charaNameField.value = App.character.getCharacterName()
        self.charaNameField.update()
    
    def updateCodeName(self):
        self.codeNameField.value = App.character.getCodeName()
        self.codeNameField.update()
    
    def updateWorks(self):
        self.worksSelBox.value = App.character.getWorks()
        self.worksSelBox.update()
    
    def updateCover(self):
        self.coverField.value = App.character.getCover()
        self.coverField.update()
    
    def updateAge(self):
        self.ageField.value = App.character.getAge()
        self.ageField.update()
    
    def updateGender(self):
        self.genderField.value = App.character.getGender()
        self.genderField.update()
        
    def updateZodiacSign(self):
        self.zodiacSignField.value = App.character.getZodiacSign()
        self.zodiacSignField.update()
        
    def updateBodyHeight(self):
        self.bodyHeightField.value = App.character.getBodyHeight()
        self.bodyHeightField.update()
        
    def updateBodyWeight(self):
        self.bodyWeightField.value = App.character.getBodyWeight()
        self.bodyWeightField.update()
    
    def updateBloodType(self):
        self.bloodTypeField.value = App.character.getBloodType()
        self.bloodTypeField.update()
    
    def updateMemoField(self):
        self.memoField.value = App.character.getMemo()
        self.memoField.update()

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
        
        # observerに登録
        App.character.bind( id = ePrmId.playerName, callback=self.updatePlayerName )
        # callback
        self.plNameField.on_blur = lambda e : App.character.setPlayerName( e.control.value )
        
    def updatePlayerName(self):
        self.plNameField.value = App.character.getPlayerName()
        self.plNameField.update()
        
    def __initExp(self):
        # 使用経験点
        self.expSpace = ft.Text( value="", width=self.itemNameWidth )
        self.expStr = ft.Text( value="使用経験点", width=self.itemNameWidth )
        self.expField = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER)

        self.expField.width = self.fieldWidth - self.itemNameWidth
        
        # observerに登録
        App.character.bind( id = ePrmId.memo, callback=self.updateExp )
        # callback
        self.expField.on_blur = lambda e : App.character.setResumeExp( int(e.control.value) )
        
    def updateExp(self):
        self.expField.value = App.character.getResumeExp()
        self.expField.update()
        
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
        self.__initExperienceList()
        self.__initExperience()
        self.__initEncount()
        self.__initArousal()
        self.__initImpulse()
        self.__initErodedVal()
        
    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Row( [self.lifepathStr]      ),
                ft.Row( self.birthPlace.row     ),
                ft.Row( self.experienceList.row ),
                ft.Row( self.experience.row     ),
                ft.Row( self.encount.row        ),
                ft.Row( self.arousal.row        ),
                ft.Row( self.impulse.row        ),
                ft.Row( self.erodedValRow       ),
            ],),
            width=self.containerWidth,
            bgcolor=ft.colors.YELLOW,
        )
    
    class LifePathItem:
        def __init__(self, dispStr : str, dropdownItem : dict[int,str] = {}, callbackOnChange =  None):
            self.dispStr = ft.Text( value = dispStr)
            self.itemSelBox = ft.Dropdown()

            self.itemSelBox.width = 400
            
            self.row = [ self.dispStr, self.itemSelBox ]

            # list itemの登録
            # self.itemSelBox.options.append( ft.dropdown.Option( " " ) )
            self.setItemList( dropdownItem )
            
            # callback
            self.itemSelBox.on_change = callbackOnChange
        
        def __del__(self):
            pass
        
        def setItemList( self, items : dict[int,str] ) :
            """ Dropdownにアイテムを追加する関数
                item : keyとvalueを持つ辞書型のリスト
            """
            for id, value in items.items() :
                self.itemSelBox.options.append( ft.dropdown.Option( key=id, text=value ) )
                
        def clearItemList( self ):
            self.itemSelBox.options.clear()
            
        def setValue(self, value):
            self.itemSelBox.value = value
            
        def getValue(self) -> str:
            return self.itemSelBox.value
        
        def update(self) :
            self.itemSelBox.update()

    def __initLifePathStr(self):
        # 出自
        self.lifepathStr = ft.Text("ライフパス")
        
    def __initBirthPlace(self):
        dict = self.generateListForDropDown( eBirthPlace, BirthPlace )
        # 出自
        self.birthPlace = self.LifePathItem("出自", dropdownItem=dict, callbackOnChange=self.birthPlaceOnChanged)
        # observerに登録
        App.character.bind( id = ePrmId.erodedVal, callback=self.updateBirthPlace )
    
    def updateBirthPlace(self):
        self.birthPlace.setValue = App.character.getBirthPlace()
        self.birthPlace.update()
        
    def __initExperienceList(self):
        dict = self.generateListForDropDown( eExperienceList, ExperienceList )
        # 経験表
        self.experienceList = self.LifePathItem("経験表", dropdownItem=dict, callbackOnChange=self.experienceListOnChange)
    
    def __initExperience(self):
        # 経験
        self.experience = self.LifePathItem("経験", callbackOnChange=self.experienceOnChanged)
        # observerに登録
        App.character.bind( id = ePrmId.experience, callback=self.updateExperience )
    
    def updateExperienceItems(self, listType : eExperienceList ) :
        """ 経験のドロップダウンボックスに表示するアイテムを変更する """
        match listType :
            case eExperienceList.student :
                enum      = eStudentExperience
                classType = StudentExperience
            case eExperienceList.sociality :
                enum      = eSocietyExperience
                classType = SocietyExperience
            case eExperienceList.underground :
                enum      = eUndergroundExperience
                classType = UndergroundExperience
            case eExperienceList.ugn :
                enum      = eUgnExperience
                classType = UgnExperience
            case _ :
                print("Invalid 経験表")
                return
        # 辞書型でリストを取得
        dict = self.generateListForDropDown( enum=enum, classType=classType )
        
        self.experience.clearItemList()
        self.experience.setItemList( items=dict )
        self.experience.update()
        
    def updateExperience(self):
        experienceListId, experienceId = App.character.getExperience()
        
        if ( experienceListId != int(self.experienceList.getValue()) ) :
            # 経験表 Dropdownの更新
            self.experienceList.setValue( experienceListId )
            self.experienceList.update()
            # 経験 Dropdownの更新
            self.updateExperienceItems( int(self.experienceList.getValue()) )
        else :
            self.experience.setValue( int(experienceId) )
        self.experience.update()
        
    def __initEncount(self):
        # 邂逅
        # 邂逅はIntEnum型で管理していない（英訳の手間）
        dict = {}
        for relation in Encount.dict.keys() :
            itemStr = relation + ": " + Encount.dict[relation]
            dict[itemStr] = itemStr
        
        self.encount = self.LifePathItem("邂逅", dropdownItem=dict, callbackOnChange=self.encountOnChanged)
        # observerに登録
        App.character.bind( id = ePrmId.encount, callback=self.updateEncount )
        
    def updateEncount(self):
        self.encount.setValue( App.character.getEncount() )
        self.encount.update()
        
    def __initArousal(self):
        dict = self.generateListForDropDown( eArousal, Arousal )
        # 覚醒
        self.arousal = self.LifePathItem("覚醒", dropdownItem=dict, callbackOnChange=self.arousalOnChanged)
        # observerに登録
        App.character.bind( id = ePrmId.arousal, callback=self.updateArousal )
        
    def updateArousal(self):
        self.arousal.setValue( App.character.getArousal() )
        self.arousal.update()
        
    def __initImpulse(self):
        dict = self.generateListForDropDown( eImpulse, Impulse )
        # 衝動
        self.impulse = self.LifePathItem("衝動", dropdownItem=dict, callbackOnChange=self.impulseOnChanged)
        # observerに登録
        App.character.bind( id = ePrmId.impulse, callback=self.updateImpulse )
        
    def updateImpulse(self):
        self.impulse.setValue( App.character.getImpulse() )
        self.impulse.update()
        
    def __initErodedVal(self):
        # 侵食率基礎値
        self.erodedValSpace = ft.Text( "" )
        self.erodedValStr = ft.Text( "侵食率基礎値" )
        self.erodedValField = ft.TextField( value=0, disabled=True)
        
        self.erodedValRow = [ self.erodedValSpace, self.erodedValStr, self.erodedValField ]
        
        # observerに登録
        App.character.bind( id = ePrmId.erodedVal, callback=self.updateErodedVal )
    
    def updateErodedVal(self):
        self.erodedValField.value = App.character.getErodedValue()
        self.erodedValField.update()
        
    def birthPlaceOnChanged(self, e):
        App.character.setBirthPlace( int(e.control.value) )
        
    def experienceListOnChange(self,e):
        # 経験 Dropdownの更新
        self.updateExperienceItems( int(e.control.value) )
        
    def experienceOnChanged(self, e):
        experienceList = self.experienceList.getValue()
        App.character.setExperience( int(experienceList), int(e.control.value) )
        
    def encountOnChanged(self, e):
        App.character.setEncount( e.control.value )
        
    def arousalOnChanged(self, e):
        App.character.setArousal( int(e.control.value) )
        
    def impulseOnChanged(self, e):
        App.character.setImpulse( int(e.control.value) )
    
    def generateListForDropDown(self, enum : IntEnum, classType) -> dict[int, str] :
        """ keyとvalueを持つ辞書型のリストを生成する """
        dict = {}
        for id in enum :
            dict[id] = classType.getDispName(id)
        return dict
        
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
        
        # observerに登録
        App.character.bind( id = ePrmId.appearance, callback=self.updateAppearance )
        
        # callback
        self.imgFrame.on_click = self.appearanceOnClicked
        
        # 画像ファイルPicker　Instance
        # openFilePicker()の度にインスタンスを生成すると都度appendすることになるのでここで生成しておく
        self.pickFileDialog = ft.FilePicker(on_result=self.filePickerOnResult)
        App.page.overlay.append( self.pickFileDialog )

    def updateAppearance(self) :
        img = App.character.getAppearance()
        self.setImage(data = img)
    
    def appearanceOnClicked(self,e):
        self.openFilePicker()
    
    def openFilePicker(self):
        self.pickFileDialog.pick_files(file_type=ft.FilePickerFileType.IMAGE)
        
    def filePickerOnResult(self, e : ft.FilePickerResultEvent):
        if e.files is None:
            print("canceled")
            return
        
        # setAppearance を実行した結果Observerからの通知によって自動的に表示画像が更新されるのでここで画像更新する必要はない
        # self.setImage(e.files[0].path)
        App.character.setAppearance(e.files[0].path)
    
    def setImage(self, path: str = None, data = None):
        if path is not None:
            self.img.src = path
        elif data is not None:
            self.img.src_base64 = data
        else :
            return
        
        self.img.color = None
        self.img.update()
        
# ###############################################################################################
class SubAbilityUi(ft.UserControl):
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
        self.maxHpUi = SubAbilityItem("HP最大値","肉体","精神" )
        # observerに登録
        App.character.bind( id = ePrmId.maxHp, callback=self.updateMaxHp )
        
    def updateMaxHp(self):
        self.maxHpUi.setPrm1 ( App.character.getBodyValue() )
        self.maxHpUi.setPrm2 ( App.character.getMentalValue() )
        self.maxHpUi.setTotal( App.character.getMaxHp() )
    
    def __initRegularStockUi(self):
        self.regularStockUi = SubAbilityItem("常備化P","社会","調達" )
        # observerに登録
        App.character.bind( id = ePrmId.regularStock, callback=self.updateRegularStockPoint )
        
    def updateRegularStockPoint(self):
        self.regularStockUi.setPrm1 ( App.character.getSocialityValue() )
        # self.regularStockUi.setPrm2 ( 調達 )
        self.regularStockUi.setTotal( App.character.getRegularStockPoint() )
    
    def __initBattleMoveUi(self):
        self.BattleMoveUi = SubAbilityItem("戦闘移動","行動値",None )
        # observerに登録
        App.character.bind( id = ePrmId.battleMove, callback=self.updateBattleMovePoint )
        
    def updateBattleMovePoint(self):
        self.BattleMoveUi.setPrm1 ( App.character.getMovePoint() )
        self.BattleMoveUi.setTotal( App.character.getBattleMove() )
    
    def __initMovePointUi(self):
        self.movePointUi = SubAbilityItem("行動値","感覚","精神" )
        # observerに登録
        App.character.bind( id = ePrmId.movePoint, callback=self.updateMovePoint )
        
    def updateMovePoint(self):
        self.movePointUi.setPrm1 ( App.character.getSenseValue() )
        self.movePointUi.setPrm2 ( App.character.getMentalValue() )
        self.movePointUi.setTotal( App.character.getMovePoint() )
    
    def __initWalletPointUi(self):
        self.walletPointUi = SubAbilityItem("財産P","常備化P","使用P" )
        # observerに登録
        App.character.bind( id = ePrmId.walletPoint, callback=self.updateWalletPoint )
        
    def updateWalletPoint(self):
        self.walletPointUi.setPrm1 ( App.character.getRegularStockPoint() )
        # self.walletPointUi.setPrm2 ( 使用P )
        self.walletPointUi.setTotal( App.character.getWalletPoint() )
    
    def __initFullPowerMoveUi(self):
        self.fullPowerUi = SubAbilityItem("全力移動","戦闘移動",None )
        # observerに登録
        App.character.bind( id = ePrmId.fullPowerMove, callback=self.updateFullPowerMove )
        
    def updateFullPowerMove(self):
        self.fullPowerUi.setPrm1 ( App.character.getBattleMove() )
        self.fullPowerUi.setTotal( App.character.getFullPowerMove() )
    
class SubAbilityItem(ft.UserControl):
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
    
    def setPrm1(self, value : int):
        self.prm1Field.value = value
        self.prm1Field.update()

    def setPrm2(self, value : int):
        self.prm2Field.value = value
        self.prm2Field.update()

    def setTotal(self, value : int):
        self.total.value = value
        self.total.update()

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
                        self.bodyUi,
                        self.senseUi,
                        self.mentalUi,
                        self.socialityUi
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            ],),
            # width=self.containerWidth,
            bgcolor=ft.colors.YELLOW,
        )
    
    def __initAbilityStr(self):
        self.abilityStr = ft.Text("能力値", bgcolor=ft.colors.GREY_100)

    def __initBodyUi(self):
        self.bodyUi = AbilityBodyUi()

    def __initSenseUi(self):
        self.senseUi = AbilitySenseUi()
    
    def __initMentalUi(self):
        self.mentalUi = AbilityMentalUi()
    
    def __initSocialityUi(self):
        self.socialityUi = AbilitySocialityUi()
    
class AbilityItemUi(ft.UserControl):
    """ 技能パラメータ """
    def __init__(self, abilityStr: str):
        super().__init__()
        # define
        self.containerWidth = 300
        self.pointWidth = 60
        # vars
        self.abilityStr     = abilityStr
        self.abilityPoint   = 0
        self.freePointSpace = ""
        self.freePoint      = 0
        self.skillList      = []
        
        # スキルリストをDX3characterから取得
        self.updateSkillList()
        
        self.skillAppendIcon = ft.IconButton(icon=ft.icons.ADD, tooltip="技能追加")
        
        self.abilityStrText    = ft.Text( self.abilityStr )
        self.abilityPointField = ft.TextField( value=self.abilityPoint, width=self.pointWidth ,read_only=True )
        self.freePointSpace    = ft.Text( self.freePointSpace,)
        self.freePointField    = ft.TextField( value=self.freePoint, width=self.pointWidth, label="成長P")
        
        self.skillRows         = ft.Column(self.skillList)
        
        # callback
        self.setSkillAppendIconOnClick( self.appendSkill )
        
        # observerに登録
        observerId : ePrmId = App.character.getSkillObserverId(self.abilityStr)
        App.character.bind(observerId, self.updateSkills)
        
    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row
                    (
                        [
                            self.abilityStrText,
                            self.abilityPointField,
                            ft.Column(
                                [
                                    self.freePointSpace,
                                    self.freePointField,
                                ]
                            ),
                        ],
                    ),
                    self.skillRows,
                    self.skillAppendIcon,
                ],
            ),
            width=self.containerWidth,
        )
    
    def updateAbilityPoint(self, point : int ) :
        """ 能力値の更新 """
        self.abilityPointField.value = point
        self.abilityPointField.update()
        
    def updateAbilityFreePoint(self, point : int)  :
        """ 能力値の成長ポイントの更新 """
        self.freePointField.value = point
        self.freePointField.update()
    
    def setAbilityFreePointOnChange(self, callback : Callable[[], None] ) -> None :
        self.freePointField.on_blur = callback
    
    def setSkillAppendIconOnClick(self, callback : Callable[[], None] ) -> None :
        self.skillAppendIcon.on_click = callback
    
    def appendSkill(self, e) :
        """ スキルの追加 """
        App.character.appendSkill(self.abilityStr)
        
        self.updateSkills()
        
    def updateSkillList(self) :
        """ スキルリストの更新 """
        # 既存のリストのクリア
        self.skillList.clear()
        # スキルリストの取得
        skillList : list[SkillPrm]= App.character.getSkillList(ability=self.abilityStr)
        
        index = 0
        # リストにスキル追加
        for skill in skillList :
            self.skillList.append( 
                SkillItemUi(
                    abilityStr   = self.abilityStr,
                    skillStr     = skill.type,
                    index        = index,
                    hasTextField = skill.existSpecific,
                    specificStr  = skill.specific,
                    freePoint    = skill.growth,
                    level        = skill.level,
                    deletable    = skill.deletable,
                )
            )
            index += 1
        
    def updateSkills(self) :
        """ スキルの更新（observerに登録するコールバック）"""
        self.updateSkillList()
        self.skillRows.update()
        

    
class AbilityBodyUi(AbilityItemUi):
    """ 肉体UI """
    def __init__(self):
        super().__init__(abilityStr = "肉体" )
        # define
        
        # vars
        
        # callback
        self.setAbilityFreePointOnChange( callback=lambda e: App.character.setBodyGrowthPoint( int(e.control.value) ) )
        
        # observerに登録
        App.character.bind(id = ePrmId.bodyPoint      , callback= self.updateBodyPoint     )
        App.character.bind(id = ePrmId.bodyGrowthPoint, callback= self.updateBodyFreePoint )
        # App.character.bind(id = ePrmId.bodySkillPoint , callback= None )
    
    def updateBodyPoint(self):
        self.updateAbilityPoint( App.character.getBodyValue() )
    
    def updateBodyFreePoint(self):
        self.updateAbilityFreePoint( App.character.getBodyGrowthPoint() )
    
    
class AbilitySenseUi(AbilityItemUi):
    """ 感覚UI """
    def __init__(self):
        super().__init__(abilityStr = "感覚")
        # define
        
        # vars
        
        # callback
        self.setAbilityFreePointOnChange( callback=lambda e: App.character.setSenseGrowthPoint( int(e.control.value) ) )
        
        # observerに登録
        App.character.bind(id = ePrmId.sensePoint      , callback= self.updateSensePoint     )
        App.character.bind(id = ePrmId.senseGrowthPoint, callback= self.updateSenseFreePoint )
    
    def updateSensePoint(self):
        self.updateAbilityPoint( App.character.getSenseValue() )
    
    def updateSenseFreePoint(self):
        self.updateAbilityFreePoint( App.character.getSenseGrowthPoint() )    
    
    
class AbilityMentalUi(AbilityItemUi):
    """ 精神UI """
    def __init__(self):
        super().__init__(abilityStr = "精神")
        # define
        
        # vars

        # callback
        self.setAbilityFreePointOnChange( callback=lambda e: App.character.setMentalGrowthPoint( int(e.control.value) ) )
        
        # observerに登録
        App.character.bind(id = ePrmId.mentalPoint      , callback= self.updateMentalPoint     )
        App.character.bind(id = ePrmId.mentalGrowthPoint, callback= self.updateMentalFreePoint )
    
    def updateMentalPoint(self):
        self.updateAbilityPoint( App.character.getMentalValue() )
    
    def updateMentalFreePoint(self):
        self.updateAbilityFreePoint( App.character.getMentalGrowthPoint() )    
    
   
class AbilitySocialityUi(AbilityItemUi):
    """ 社会UI """
    def __init__(self):
        super().__init__(abilityStr = "社会")
        # define
        
        # vars

        # callback
        self.setAbilityFreePointOnChange( callback=lambda e: App.character.setSocialityGrowthPoint( int(e.control.value) ) )
        
        # observerに登録
        App.character.bind(id = ePrmId.socialityPoint      , callback= self.updateSocialityPoint     )
        App.character.bind(id = ePrmId.socialityGrowthPoint, callback= self.updateSocialityFreePoint )
    
    def updateSocialityPoint(self):
        self.updateAbilityPoint( App.character.getSocialityValue() )
    
    def updateSocialityFreePoint(self):
        self.updateAbilityFreePoint( App.character.getSocialityGrowthPoint() )    
    
   
class SkillItemUi(ft.UserControl):
    """ 技能パラメータ """
    def __init__(self, abilityStr : str, skillStr : str, index : int, hasTextField : bool = False, specificStr : str = "", freePoint : float = 0, level : int = 0, deletable : bool = False ):
        super().__init__()
        # define
        
        # vars
        self.abilityStr   = abilityStr
        self.skillStr     = skillStr
        self.index        = index   # スキルリストのインデックス
        self.level        = level
        self.freePoint    = freePoint
        self.hasTextField = hasTextField
        self.specificStr  = specificStr
        self.deletable    = deletable
        
        self.strText        = ft.Text(self.skillStr)
        self.levelField     = ft.TextField(value=self.level    , keyboard_type=ft.KeyboardType.NUMBER, read_only=True, suffix_text="Lv")
        self.freePointField = ft.TextField(value=self.freePoint, keyboard_type=ft.KeyboardType.NUMBER, suffix_text="P", label="成長P")
        
        self.specificField   = ft.TextField(value=self.specificStr)
        
        self.skillDeleteIcon = ft.IconButton(icon=ft.icons.DELETE, tooltip="削除")
        
        # callback
        self.specificField.on_blur    = self.specificFieldOnChange
        self.freePointField.on_blur   = self.freePointFieldOnChange
        self.skillDeleteIcon.on_click = self.skillDeleteIconOnClick
    
    def build(self):
        if self.hasTextField :
            row = [self.strText, self.specificField, self.freePointField, self.levelField ]
            # 一旦適当な幅で調整しておく
            self.strText.width = self.specificField.width= 50
        else :
            row = [self.strText, self.freePointField, self.levelField ]
            # 一旦適当な幅で調整しておく
            self.strText.width = 100
        
        if self.deletable :
            row.append( self.skillDeleteIcon )
            
        # 一旦適当な幅で調整しておく
        self.levelField.width = self.freePointField.width = 60
        return ft.Row( row )
    
    def specificFieldOnChange(self, e) :
        App.character.setSpecificSkillStr( ability=self.abilityStr, index=self.index, str=e.control.value )
         
    def freePointFieldOnChange(self, e) :
        App.character.setSkillGrowthPoint( ability=self.abilityStr, index=self.index, point=float(e.control.value) )

    def skillDeleteIconOnClick(self, e) :
        App.character.deleteSkill(ability=self.abilityStr, index=self.index)

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
        
        # dropdown itemの登録
        for id in eBleed :
            self.bleedSelBox.options.append( ft.dropdown.Option(key=id, text=Bleed.getDispName(id) ) )

        # callback
        self.bleedSelBox.on_change = lambda e: App.character.setBleed( int(e.control.value) )
        
        # observer に登録
        App.character.bind( id=ePrmId.bleed, callback=self.update )
        
    def update(self):
        self.bleedSelBox.value = App.character.getBleed()
        self.bleedSelBox.update()
        
    
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
        self.syndromeItem1 = SyndromeItem(syndromeId=1)
        self.syndromeItem2 = SyndromeItem(syndromeId=2)
        self.syndromeItem3 = SyndromeItem(syndromeId=3)
        
        self.syndromeItem3.selBox.label = "optional"
        
        self.syndromeItems = [
                self.syndromeItem1,
                self.syndromeItem2,
                self.syndromeItem3,
            ]
        
class SyndromeItem(ft.UserControl):
    """ シンドローム """
    def __init__(self, syndromeId : Literal[1,2,3] ):
        super().__init__()
        # vars
        self.syndromeId = syndromeId
        
        # init
        self.__initSyndromeItem()

        # observerに登録
        match self.syndromeId :
            case 1 :
                bindId = ePrmId.syndrome1
            case 2 :
                bindId = ePrmId.syndrome2
            case 3 :
                bindId = ePrmId.optionalSyndrome
            case _ :
                print( "syndromeNum Error" )
        App.character.bind(id=bindId, callback=self.update)
        # Bleedが更新されたときにも通知を受ける
        App.character.bind(id=ePrmId.bleed, callback=self.update)
    
        self.target = "optional" if self.syndromeId == 3 else self.syndromeId
        
    def build(self):
        return self.selBox
    
    def __initSyndromeItem(self):
        self.selBox = ft.Dropdown()
        
        for id in eSyndrome :
            self.selBox.options.append(ft.dropdown.Option( key=id, text=Syndrome.getDispName(id) ) )
        
        # callback
        self.selBox.on_change = self.onChange
        
        flg = self.isToBeDisable( App.character.getBleed() )
        self.selBox.disabled = flg
        
    def update(self) :
        self.selBox.value = App.character.getSyndrome(target=self.target)
        
        # ブリードが変わった場合
        flg = self.isToBeDisable( App.character.getBleed() )
        self.selBox.disabled = flg
        
        self.selBox.update()
    
    def isToBeDisable(self, bleedId : eBleed) -> bool :
        flg = False
        
        match self.syndromeId :
            case 1 :
                pass
            case 2 :
                # synderom 2 は ピュアブリードのとき Disable
                if bleedId == eBleed.pureBleed :
                    flg = True
            case 3 :
                # optional syndrome は トライブリードでないとき Disable
                if not bleedId == eBleed.triBleed  :
                    flg = True
            case _ :
                pass
        return flg
    
    def onChange(self, e):
        App.character.setSyndrome(target = self.target, syndrome = int(e.control.value) )
        

# ###############################################################################################

def run():
    app = App()
    app.run()

if __name__ == "__main__":
    run()