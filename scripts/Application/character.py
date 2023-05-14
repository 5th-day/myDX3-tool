# coding: UTF-8

from .character_attributes import *

# class DX3Character(Personality, LifePath) 継承で持つか変数として持つか。。。
class DX3Character(object):
    """ Double Cross v3 character class """
    def __init__(self) :
        # instance vars
        personality = Personality()
        lifepath    = LifePath()
        lois        = Lois()

    def __del__(self) :
        pass

class Personality(object):
    """ Personal data class """
    def __init__(self) :
        # instance vars
        self.name            = ""
        self.code_name       = ""
        self.works : eWorks  = 0
        self.cover           = 0
        self.age             = 0
        self.gender          = 0
        self.zodiac_sign     = "" # 星座
        self.height          = 0
        self.weight          = 0
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

