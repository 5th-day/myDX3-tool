# coding: UTF-8

from typing import Callable, Union, Literal

from .state import State, Observer
from .img_lib import ImgLib
from .character_attributes import *

class DX3Character(object):
    """ Double Cross v3 character class
        パラメータが変更されたとき影響を受ける他のパラメータを更新できるようにAPI経由でアクセスする
        setXxxx()  : パラメータの変更
        getXxxx()  : パラメータの取得
        bind()     : パラメータが変更されたときに通知を受けるコールバックの登録
    """
    def __init__(self) :
        # instance vars
        self.__prm    = DX3CharacterData()
        # 辞書型でObserverを管理する
        self.__observers: dict[ePrmId, Observer] = {}
        
        for id in ePrmId :
            self.__observers[id] = Observer()

    def __del__(self) :
        pass
    
    # ################################################################
    # API
    # ################################################################
    def bind(self, id : ePrmId, callback : Callable[ [], None ]) -> None :
        """ パラメータが変更されたとき、bindに登録したコールバックが呼び出される """
        self.__observers[id].bind(callback)
        
    # ################　Personality　#########################
    # Character Name
    def setCharacterName(self, name: str) -> None:
        # set prm
        self.__prm.personality.name = name
        # notify prm change
        self.__observers[ePrmId.charName].notify()
        
    def getCharacterName(self) -> str :
        return self.__prm.personality.name

      # Code Name
    def setCodeName(self, codeName: str) -> None:
        # set prm
        self.__prm.personality.codeName = codeName
        # notify prm change
        self.__observers[ePrmId.codeName].notify()
        
    def getCodeName(self) -> str :
        return self.__prm.personality.codeName

    # Works
    def setWorkws(self, works: eWorks) -> None:
        # set prm
        self.__prm.personality.works = works
        # notify prm change
        self.__observers[ePrmId.works].notify()
        
        # update 能力値
        self._updateAbilityValue()
        
    def getWorks(self) -> eWorks :
        return self.__prm.personality.works

    # Cover
    def setCover(self, cover: str) -> None:
        # set prm
        self.__prm.personality.cover = cover
        # notify prm change
        self.__observers[ePrmId.cover].notify()
        
    def getCover(self) -> str :
        return self.__prm.personality.cover

    # 年齢
    def setAge(self, age: int) -> None:
        # set prm
        self.__prm.personality.age = age
        # notify prm change
        self.__observers[ePrmId.age].notify()
        
    def getAge(self) -> str :
        return self.__prm.personality.age

    # 性別
    def setGender(self, gender: str) -> None:
        # set prm
        self.__prm.personality.gender = gender
        # notify prm change
        self.__observers[ePrmId.gender].notify()
        
    def getGender(self) -> str :
        return self.__prm.personality.gender

    # 星座
    def setZodiacSign(self, zodiacSign: str) -> None:
        # set prm
        self.__prm.personality.zodiacSign = zodiacSign
        # notify prm change
        self.__observers[ePrmId.zodiacSign].notify()
        
    def getZodiacSign(self) -> str :
        return self.__prm.personality.zodiacSign

    # 身長
    def setBodyHeight(self, height: float) -> None:
        # set prm
        self.__prm.personality.height = height
        # notify prm change
        self.__observers[ePrmId.bodyHeight].notify()
        
    def getBodyHeight(self) -> float :
        return self.__prm.personality.height

    # 体重
    def setBodyWeight(self, weight: float) -> None:
        # set prm
        self.__prm.personality.weight = weight
        # notify prm change
        self.__observers[ePrmId.bodyWeight].notify()
        
    def getBodyWeight(self) -> float :
        return self.__prm.personality.weight

    # 血液型
    def setBloodType(self, bloodType: str) -> None:
        # set prm
        self.__prm.personality.bloodType = bloodType
        # notify prm change
        self.__observers[ePrmId.bloodType].notify()
        
    def getBloodType(self) -> str :
        return self.__prm.personality.bloodType

    # Memo
    def setMemo(self, str: str) -> None:
        # set prm
        self.__prm.personality.memo = str
        # notify prm change
        self.__observers[ePrmId.memo].notify()
        
    def getMemo(self) -> str :
        return self.__prm.personality.memo

    # Player Name
    def setPlayerName(self, name: str) -> None:
        # set prm
        self.__prm.personality.playerName = name
        # notify prm change
        self.__observers[ePrmId.playerName].notify()
        
    def getPlayerName(self) -> str :
        return self.__prm.personality.playerName

    # 外見
    def setAppearance(self, path : str = "", base64 = "" ) :
        # set prm
        if ( path != "" ) :     # pathが与えられた場合
            base64 = ImgLib.getBase64fromPath(path)
        elif ( base64 != "" ) :  # 画像データが与えられた場合
            pass
        else : 
            print("Error")
            return
        
        self.__prm.personality.appearance = base64
        # notify prm change
        self.__observers[ePrmId.appearance].notify()
    
    def getAppearance(self) -> str:
        """ Return base64 image data """
        return self.__prm.personality.appearance
    
    # 使用経験点
    def setResumeExp(self, exp: int) -> None:
        # set prm
        self.__prm.personality.resumeExp = exp
        # notify prm change
        self.__observers[ePrmId.resumeExp].notify()
        
    def getResumeExp(self) -> int :
        return self.__prm.personality.resumeExp

    # ################　LifePath　#########################
    # 出自
    def setBirthPlace(self, birthPlace: eBirthPlace) -> None:
        # set prm
        self.__prm.lifepath.birthPlace = birthPlace
        # notify prm change
        self.__observers[ePrmId.birthPlace].notify()
        
    def getBirthPlace(self) -> eBirthPlace :
        return self.__prm.lifepath.birthPlace

    # 経験
    # どの経験表か区別が必要
    def setExperience(self, experience : Union[eStudentExperience, eSocietyExperience, eUgnExperience] ) -> None:
        # set prm
        self.__prm.lifepath.experience = experience
        # notify prm change
        self.__observers[ePrmId.experience].notify()
        
    def getExperience(self) -> eBirthPlace :
        return self.__prm.lifepath.experience

    # 邂逅
    def setEncount(self, encount: str) -> None:
        # set prm
        self.__prm.lifepath.encount = encount
        # notify prm change
        self.__observers[ePrmId.encount].notify()
        
    def getEncount(self) -> str :
        return self.__prm.lifepath.encount

    # 覚醒
    def setArousal(self, arousal: eArousal) -> None:
        # set prm
        self.__prm.lifepath.arousal = arousal
        
        self.__prm.lifepath.arousalErodedVal = Arousal.getErodedValue( arousal )
        #　覚醒は侵食率基礎値に影響を与える
        self._updateErodedValue()
        # notify prm change
        self.__observers[ePrmId.arousal].notify()
        
    def getArousal(self) -> eArousal :
        return self.__prm.lifepath.arousal

    # 衝動
    def setImpulse(self, impulse: eImpulse) -> None:
        # set prm
        self.__prm.lifepath.impulse = impulse
        
        self.__prm.lifepath.impulseErodedVal = Impulse.getErodedValue( impulse )
        
        self._updateErodedValue()
        # notify prm change
        self.__observers[ePrmId.impulse].notify()
        
    def getImpulse(self) -> eImpulse :
        return self.__prm.lifepath.impulse

    # 侵食率基礎値
    def _updateErodedValue(self) -> None:
        # set prm
        erodedVal = self.__prm.lifepath.arousalErodedVal + self.__prm.lifepath.impulseErodedVal
        self.__prm.lifepath.baseErodedVal = erodedVal
        # notify prm change
        self.__observers[ePrmId.erodedVal].notify()
        
    def getErodedValue(self) -> int :
        return self.__prm.lifepath.baseErodedVal
    
    # ################　能力値　#########################
    # 能力値
    def _updateAbilityValue(self) -> None:
        # set prm
        body        = 0
        sense       = 0
        mental      = 0
        sociality   = 0
        
        # ref syndrome
        syndromePrm1 = Syndrome.getPrm( self.__prm.syndrome1 )
        syndromePrm2 = Syndrome.getPrm( self.__prm.syndrome2 )
        
        bleed = self.getBleed()
        if ( bleed == eBleed.pureBleed ) :
            body        += syndromePrm1.bodyVal      * 2
            sense       += syndromePrm1.senseVal     * 2
            mental      += syndromePrm1.mentalVal    * 2
            sociality   += syndromePrm1.socialityVal * 2
        else :
            body        += syndromePrm1.bodyVal      + syndromePrm2.bodyVal      
            sense       += syndromePrm1.senseVal     + syndromePrm2.senseVal     
            mental      += syndromePrm1.mentalVal    + syndromePrm2.mentalVal    
            sociality   += syndromePrm1.socialityVal + syndromePrm2.socialityVal 
            
        # ref works
        worksId  = self.getWorks()
        worksPrm = Works.getFactor(worksId)
        
        match worksPrm :
            case "肉体":
                body        += 1
            case "感覚":
                sense       += 1
            case "精神":
                mental      += 1
            case "社会":
                sociality   += 1
            case _:
                print("Invalid Works")
                return
        
        # ref 成長P
        body        += self.__prm.ability.body.growth
        sense       += self.__prm.ability.sense.growth
        mental      += self.__prm.ability.mental.growth
        sociality   += self.__prm.ability.sociality.growth
        
        # 反映
        self.__prm.ability.body.val         = body
        self.__prm.ability.sense.val        = sense
        self.__prm.ability.mental.val       = mental
        self.__prm.ability.sociality.val    = sociality
        
        # notify prm change
        self.__observers[ePrmId.bodyPoint     ].notify()
        self.__observers[ePrmId.sensePoint    ].notify()
        self.__observers[ePrmId.mentalPoint   ].notify()
        self.__observers[ePrmId.socialityPoint].notify()
        
        # update 副能力値（能力値が関わるもの）
        # HP最大値
        self._updateMaxHp()
        # 常備化P
        self._updateRegularStockPoint()
        # 行動値
        self._updateMovePoint()
        
    # 肉体値
    def getBodyValue(self) -> int :
        return self.__prm.ability.body.val

    def setBodyGrowthPoint(self, point : int ) :
        # set prm
        self.__prm.ability.body.growth = point
        # notify prm change
        self.__observers[ePrmId.bodyGrowthPoint].notify()
        # update prm
        self._updateAbilityValue()
       
    def getBodyGrowthPoint(self) -> int :
        return self.__prm.ability.body.growth
    
    # 感覚値
    def getSenseValue(self) -> int :
        return self.__prm.ability.sense.val

    def setSenseGrowthPoint(self, point : int ) :
        # set prm
        self.__prm.ability.sense.growth = point
        # notify prm change
        self.__observers[ePrmId.senseGrowthPoint].notify()
        # update prm
        self._updateAbilityValue()
       
    def getSenseGrowthPoint(self) -> int :
        return self.__prm.ability.sense.growth
    
    # 精神値
    def getMentalValue(self) -> int :
        return self.__prm.ability.mental.val

    def setMentalGrowthPoint(self, point : int ) :
        # set prm
        self.__prm.ability.mental.growth = point
        # notify prm change
        self.__observers[ePrmId.mentalGrowthPoint].notify()
        # update prm
        self._updateAbilityValue()
       
    def getMentalGrowthPoint(self) -> int :
        return self.__prm.ability.mental.growth
    
    # 社会値
    def getSocialityValue(self) -> int :
        return self.__prm.ability.sociality.val
    
    def setSocialityGrowthPoint(self, point : int ) :
        # set prm
        self.__prm.ability.sociality.growth = point
        # notify prm change
        self.__observers[ePrmId.socialityGrowthPoint].notify()
        # update prm
        self._updateAbilityValue()
       
    def getSocialityGrowthPoint(self) -> int :
        return self.__prm.ability.sociality.growth
    
    # ################　副能力値　#########################
    # HP最大値
    def _updateMaxHp(self) -> None :
        # set prm
        maxHp = self.getBodyValue() * 2 + self.getMentalValue() + 20
        self.__prm.subAbility.maxHp = maxHp
        
        # notify prm change
        self.__observers[ePrmId.maxHp].notify()
    
    def getMaxHp(self) -> int :
        return self.__prm.subAbility.maxHp

    # 常備化P
    def _updateRegularStockPoint(self) -> None :
        # set prm
        # Todo：調達Pを加算
        regulaStock = (self.getSocialityValue() + 0) * 2
        
        # notify prm change
        self.__observers[ePrmId.regularStock].notify()
        
        # 財産Pを更新
        self._updateWalletPoint()
    
    def getRegularStockPoint(self) -> int :
        return self.__prm.subAbility.regularStockPoint

    # 行動値
    def _updateMovePoint(self) -> None :
        # set prm
        movePoint = self.getSenseValue() * 2 + self.getMentalValue()
        self.__prm.subAbility.movePoint = movePoint
        # notify prm change
        self.__observers[ePrmId.movePoint].notify()
        
        # 戦闘移動を更新
        self._updateBattleMove()
    
    def getMovePoint(self) -> int :
        return self.__prm.subAbility.movePoint

    # 財産P
    def _updateWalletPoint(self) -> None :
        # set prm
        # Todo : 使用Pを減算
        self.__prm.subAbility.walletPoint = self.getRegularStockPoint() - 0
        # notify prm change
        self.__observers[ePrmId.walletPoint].notify()
    
    def getWalletPoint(self) -> int :
        return self.__prm.subAbility.walletPoint

    # 戦闘移動
    def _updateBattleMove(self) -> None :
        # set prm
        self.__prm.subAbility.battleMove = self.getMovePoint() + 5
        # notify prm change
        self.__observers[ePrmId.battleMove].notify()
        
        # 全力移動を更新
        self._updateFullPowerMove()
    
    def getBattleMove(self) -> int :
        return self.__prm.subAbility.battleMove

    # 全力移動
    def _updateFullPowerMove(self) -> None :
        # set prm
        self.__prm.subAbility.fullPowerMove = self.getMovePoint() * 2
        # notify prm change
        self.__observers[ePrmId.fullPowerMove].notify()
    
    def getFullPowerMove(self) -> int :
        return self.__prm.subAbility.fullPowerMove

    # ################　ブリード、シンドローム　#########################
    # ブリード
    def setBleed(self, bleed: eBleed) -> None:
        # set prm
        self.__prm.bleed = bleed
        
        # notify prm change
        self.__observers[ePrmId.bleed].notify()
        
        # update 能力値
        self._updateAbilityValue()
        
    def getBleed(self) -> eBleed :
        return self.__prm.bleed

    # シンドローム
    def setSyndrome(self, target : Literal[1,2,"optional"], syndrome : eSyndrome) -> None :
        match target :
            case 1 :
                # set prm
                self.__prm.syndrome1 = syndrome
                # notify prm change
                self.__observers[ePrmId.syndrome1].notify()
            case 2 :
                # set prm
                self.__prm.syndrome2 = syndrome
                # notify prm change
                self.__observers[ePrmId.syndrome2].notify()
            case "optional" :
                # set prm
                self.__prm.optionalSyndrome = syndrome
                # notify prm change
                self.__observers[ePrmId.optionalSyndrome].notify()
            case _ :
                print("Error")
                return
        
        # update 能力値
        self._updateAbilityValue()
    
    def getSyndrome(self, target : Literal[1,2,"optional"] ) -> eSyndrome:
        match target :
            case 1 :
                return self.__prm.syndrome1
            case 2 :
                return self.__prm.syndrome2
            case "optional" :
                return self.__prm.optionalSyndrome
            case _ :
                print("Error")
                return
    
    # ################　エフェクト、コンボ　#########################
    # エフェクト
    def appendEffect(self):
        self.__prm.effectList.append()
        
        # notify prm change
        self.__observers[ePrmId.effect].notify()
    
    def deleteEffect(self, index : int ):
        deletedEffect = self.__prm.effectList[index]
        del self.__prm.effectList[index]
        
        # notify prm change
        self.__observers[ePrmId.effect].notify()
        
        # combo check
        
    
    def setEffect(self, index : int, syndrome : eSyndrome, effect ) -> None:
        # set prm
        # self.__prm.effectList[index] = Effect.
        
        # notify prm change
        self.__observers[ePrmId.effect].notify()
        
    def getEffectList(self) -> list[EffectPrm] :
        return self.__prm.effectList

    def getEffect(self, index : int) -> EffectPrm :
        return self.__prm.effectList[index]

    def getEffectNum(self) -> int :
        return len(self.__prm.effectList)

    # コンボ
    def appendCombo(self):
        self.__prm.comboList.append()
        
        # notify prm change
        self.__observers[ePrmId.combo].notify()
    
    def deleteCombo(self, index : int ):
        del self.__prm.comboList[index]
        
        # notify prm change
        self.__observers[ePrmId.combo].notify()
    
    def setEffectToCombo(self, index : int, syndrome : eSyndrome, effect ) -> None:
        # set prm
        # self.__prm.comboList[index] = Effect.
        
        # notify prm change
        self.__observers[ePrmId.combo].notify()
        
    def getCobmoList(self) -> list[ComboPrm] :
        return self.__prm.comboList

    def getCombo(self, index : int) -> ComboPrm :
        pass
        # return  ,self.__prm.effectList[index]

    def getComboNum(self) -> int :
        return len(self.__prm.comboList)

      
# ################################################################################################
class DX3CharacterData(object):
    """ Double Cross v3 character data class """
    def __init__(self) :
        # instance vars
        self.personality = Personality()
        self.lifepath    = LifePath()
        self.ability     = Ability()
        self.subAbility  = SubAbility()
        self.loisList    = []
        
        self.bleed : eBleed         = eBleed.pureBleed
        self.syndrome1 : eSyndrome  = eSyndrome.empty
        self.syndrome2 : eSyndrome  = eSyndrome.empty
        self.optionalSyndrome : eSyndrome = eSyndrome.empty
        
        self.effectList : list[EffectPrm] = []   
        self.comboList  : list[ComboPrm]  = []

    def __del__(self) :
        pass

    
class Personality(object):
    """ Personal data class """
    def __init__(self) :
        # instance vars
        self.name : str      = ""
        self.codeName        = ""
        self.works : eWorks  = 0
        self.cover           = ""
        self.age             = 0
        self.gender          = ""
        self.zodiacSign      = "" # 星座
        self.height          = 0
        self.weight          = 0
        self.bloodType       = 0
        self.memo            = ""
        self.playerName      = ""
        self.resumeExp       = 0

        self.appearance = ""

    def __del__(self) :
        pass

class LifePath(object):
    """ キャラクターの人生の経歴に関するクラス """
    def __init__(self) :
        # instance vars
        self.birthPlace       = "" # 出自
        self.experience       = "" # 経験
        self.encount          = "" # 邂逅
        self.arousal          = "" # 覚醒
        self.arousalErodedVal = 0  # 侵食値
        self.impulse          = "" # 衝動
        self.impulseErodedVal = 0  # 侵食値
        self.baseErodedVal    = 0  # 侵食地基礎値

    def __del__(self) :
        pass

class Lois(object):
    """ ロイス（人との絆）に関するクラス """
    def __init__(self) :
        # instance vars
        self.relationship     = "" # 
        self.name             = "" # 
        self.feel             = "" # 好意・悪意
        self.memo             = "" # 
        self.titas            = "" # タイタス


    def __del__(self) :
        pass

class Ability(object):
    """ 能力値に関するクラス """
    def __init__(self) -> None:
        self.body       = AbilityBodyPrm()
        self.sense      = AbilitySensePrm()
        self.mental     = AbilityMentalPrm()
        self.sociality  = AbilitySocialityPrm()
        
   
    def __del__(self) :
        pass

class AbilityPrm(object):
    """ 能力値に関するクラス """
    def __init__(self) -> None:
        self.val    = 0
        self.growth = 0
        
        self.skillList = []
    
    def __del__(self) :
        pass

class AbilityBodyPrm(AbilityPrm):
    def __init__(self) -> None:
        super().__init__()
        
        self.skillList.append( SkillPrm("白兵"))
        self.skillList.append( SkillPrm("回避"))
        self.skillList.append( SkillPrm("運転"))

class AbilitySensePrm(AbilityPrm):
    def __init__(self) -> None:
        super().__init__()
        
        self.skillList.append( SkillPrm("射撃"))
        self.skillList.append( SkillPrm("知覚"))
        self.skillList.append( SkillPrm("芸術"))

class AbilityMentalPrm(AbilityPrm):
    def __init__(self) -> None:
        super().__init__()
        
        self.skillList.append( SkillPrm("RC"))
        self.skillList.append( SkillPrm("意志"))
        self.skillList.append( SkillPrm("知識"))

class AbilitySocialityPrm(AbilityPrm):
    def __init__(self) -> None:
        super().__init__()
        
        self.skillList.append( SkillPrm("交渉"))
        self.skillList.append( SkillPrm("調達"))
        self.skillList.append( SkillPrm("情報"))

class SubAbility(object):
    def __init__(self) -> None:
        self.maxHp = 0 
        self.regularStockPoint = 0
        self.movePoint         = 0
        self.walletPoint       = 0
        self.battleMove        = 0
        self.fullPowerMove     = 0

class SkillPrm(object):
    """ スキルに関するクラス """
    def __init__(self, type : str, specific : str = "") -> None:
        self.type   = type
        self.specific = specific
        self.growth = 0
        self.level  = 0
        
    
    def __del__(self) :
        pass
