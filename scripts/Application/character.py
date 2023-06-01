# coding: UTF-8

from typing import Callable
from .state import State, Observer
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
    
    def bind(self, id : ePrmId, callback : Callable[ [], None ]) -> None :
        """ パラメータが変更されたとき、bindに登録したコールバックが呼び出される """
        self.__observers[id].bind(callback)
        
    # Character Name
    def setCharacterName(self, str: str) -> None:
        # set prm
        self.__prm.personality.name = str
        # notify prm change
        self.__observers[ePrmId.charName].notify()
        
    def getCharacterName(self) -> str :
        return self.__prm.personality.name

        
# ################################################################################################
class DX3CharacterData(object):
    """ Double Cross v3 character data class """
    def __init__(self) :
        # instance vars
        self.personality = Personality()
        self.lifepath    = LifePath()
        self.lois        = Lois()

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
        self.gender          = 0
        self.zodiacSign      = "" # 星座
        self.height          = 0
        self.weight          = 0
        self.bloodType       = 0
        self.memo            = ""
        self.playerName      = ""
        self.playerExp       = 0

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

class Bleed(object):
    """ ブリード（血族）に関するクラス """
    def __init__(self) :
        # instance vars
        self.type             = "" # ブリード によって選べるシンドロームの数が変わる
        self.syndrome         = [] # どうやらシンドロームによってエフェクトが決まる
        self.optionalSyndrome = 0  # オプショナルは扱いが異なる


    def __del__(self) :
        pass

class Syndrome(object):
    """ シンドロームに関するクラス """
    def __init__(self, type, syndrome) :
        # instance vars
        self.type             = "" # ブリード によって選べるシンドロームの数が変わる
        self.syndrome         = [] # どうやらシンドロームによってエフェクトが決まる
        self.optionalSyndrome = 0  # オプショナルは扱いが異なる


    def __del__(self) :
        pass
      
class Effect(object):
    """ エフェクト（能力）に関するクラス """
    def __init__(self) :
        # instance vars
        self.name           = "" # 
        self.level          = 0  # 
        self.timing         = "" #
        self.skill          = 0  #
        self.difficulty     = 0  #
        self.object         = "" # 対象
        self.reach          = 0  # 射程
        self.ErodingVal     = 0  # 侵食値
        self.limit          = "" # 制限
        self.detail         = "" # 詳細
        self.ruleBookPage   = 0 # 参照ページ
    def __del__(self) :
        pass

class ComboData(object):
    """ コンボデータに関するクラス """
    def __init__(self) :
        # instance vars
        self.name           = "" # 
        self.level          = 0  # 
        self.timing         = "" #
        self.skill          = 0  #
        self.difficulty     = 0  #
        self.object         = "" # 対象
        self.reach          = 0  # 射程
        self.ErodingVal     = 0  # 侵食値
        self.limit          = "" # 制限
        self.detail         = "" # 詳細
    def __del__(self) :
        pass

class Buff(object):
    """ バフに関するクラス """
    def __init__(self) :
        # instance vars
        self.diceIncrease = 0 # ダイス増加（侵食値）
        self.diceNum      = 0 # ダイス補正
        self.critical     = 0 # C値補正
        self.accuracy     = 0 # 命中（達成値）補正
        self.attack       = 0 # 攻撃力補正
    def __del__(self) :
        pass
