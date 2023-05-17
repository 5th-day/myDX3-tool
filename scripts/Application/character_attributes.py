# coding: UTF-8

import weakref
from enum import IntEnum, auto, unique

@unique
class eWorks(IntEnum):
    ElementarySchoolStudent   = auto() # 小学生
    MiddleSchoolStudent       = auto() # 中学生
    HighSchoolStudent         = auto() # 高校生
    BadStudent                = auto() # 不良学生
    UniversityStudent         = auto() # 大学生
    PartTimeWorker            = auto() # フリーター
    Teacher                   = auto() # 教師
    HousewifeOrHusband        = auto() # 主婦・主夫
    UgnChildrenA              = auto() # UGNチルドレンA
    UgnChildrenB              = auto() # UGNチルドレンB
    UgnChildrenC              = auto() # UGNチルドレンC
    UgnAgentA                 = auto() # UGNエージェントA
    UgnAgentB                 = auto() # UGNエージェントB
    UgnAgentC                 = auto() # UGNエージェントC
    UgnAgentD                 = auto() # UGNエージェントD
    UgnBranchManagerA         = auto() # UGN支部長A
    UgnBranchManagerB         = auto() # UGN支部長B
    UgnBranchManagerC         = auto() # UGN支部長C
    UgnBranchDirectorD        = auto() # UGN支部長D
    Criminal                  = auto() # 刑事
    Discipline                = auto() # 鑑識
    Lawyer                    = auto() # 弁護士
    DefensiveMember           = auto() # 防衛隊員
    Mercenary                 = auto() # 傭兵
    Researcher                = auto() # 研究者
    Professor                 = auto() # 教授
    Nurse                     = auto() # 看護師
    Doctor                    = auto() # 医者
    Politician                = auto() # 政治家
    Businessman               = auto() # ビジネスマン
    Executive                 = auto() # エグゼクティブ
    BarBusiness               = auto() # 水商売
    Shopkeeper                = auto() # 商店主
    ReligiousPerson           = auto() # 宗教家
    Detective                 = auto() # 探偵
    Bodyguard                 = auto() # ボディーガード
    Driver                    = auto() # ドライバー
    Yakuza                    = auto() # ヤクザ
    Mafia                     = auto() # マフィア
    Thief                     = auto() # 泥棒
    EgoWetter                 = auto() # エゴシエーター
    Assassin                  = auto() # 暗殺者
    FortuneTeller             = auto() # 占い師
    Artist                    = auto() # アーティスト
    Singer                    = auto() # 歌手
    Actor                     = auto() # 俳優
    Magician                  = auto() # 奇術師
    Athlete                   = auto() # アスリート
    Fighter                   = auto() # 格闘家
    Reporter                  = auto() # 記者
    Announcer                 = auto() # アナウンサー
    Programmer                = auto() # プログラマー
    Hacker                    = auto() # ハッカー
    JackOfAllTrades           = auto() # 何でも屋
    Informer                  = auto() # 情報屋
    Operative                 = auto() # 工作員


class WorksPrm :
    """ 職業パラメータ class """

    def __init__(self, dispName : str, factor, skills ) :
        # instance vars
        self.dispName  = dispName
        self.factor    = factor
        self.skills    = skills
        
    def __del__(self) :
        pass
    

class Works :
    """ 職業 class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eWorks.ElementarySchoolStudent   : WorksPrm( dispName="小学生"          , factor="感覚", skills=["知覚（２）", "意志", "RC", "情報：噂話", "-", ] ),
        eWorks.MiddleSchoolStudent       : WorksPrm( dispName="中学生"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.HighSchoolStudent         : WorksPrm( dispName="高校生"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.BadStudent                : WorksPrm( dispName="不良学生"        , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UniversityStudent         : WorksPrm( dispName="大学生"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.PartTimeWorker            : WorksPrm( dispName="フリーター"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Teacher                   : WorksPrm( dispName="教師"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.HousewifeOrHusband        : WorksPrm( dispName="主婦・主夫"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnChildrenA              : WorksPrm( dispName="UGNチルドレンA"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnChildrenB              : WorksPrm( dispName="UGNチルドレンB"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnChildrenC              : WorksPrm( dispName="UGNチルドレンC"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnAgentA                 : WorksPrm( dispName="UGNエージェントA" , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnAgentB                 : WorksPrm( dispName="UGNエージェントB" , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnAgentC                 : WorksPrm( dispName="UGNエージェントC" , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnAgentD                 : WorksPrm( dispName="UGNエージェントD" , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnBranchManagerA         : WorksPrm( dispName="UGN支部長A"      , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnBranchManagerB         : WorksPrm( dispName="UGN支部長B"      , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnBranchManagerC         : WorksPrm( dispName="UGN支部長C"      , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnBranchDirectorD        : WorksPrm( dispName="UGN支部長D"      , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Criminal                  : WorksPrm( dispName="刑事"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Discipline                : WorksPrm( dispName="鑑識"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Lawyer                    : WorksPrm( dispName="弁護士"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.DefensiveMember           : WorksPrm( dispName="防衛隊員"        , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Mercenary                 : WorksPrm( dispName="傭兵"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Researcher                : WorksPrm( dispName="研究者"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Professor                 : WorksPrm( dispName="教授"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Nurse                     : WorksPrm( dispName="看護師"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Doctor                    : WorksPrm( dispName="医者"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Politician                : WorksPrm( dispName="政治家"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Businessman               : WorksPrm( dispName="ビジネスマン"     , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Executive                 : WorksPrm( dispName="エグゼクティブ"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.BarBusiness               : WorksPrm( dispName="水商売"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Shopkeeper                : WorksPrm( dispName="商店主"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.ReligiousPerson           : WorksPrm( dispName="宗教家"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Detective                 : WorksPrm( dispName="探偵"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Bodyguard                 : WorksPrm( dispName="ボディーガード"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Driver                    : WorksPrm( dispName="ドライバー"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Yakuza                    : WorksPrm( dispName="ヤクザ"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Mafia                     : WorksPrm( dispName="マフィア"         , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Thief                     : WorksPrm( dispName="泥棒"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.EgoWetter                 : WorksPrm( dispName="エゴシエーター"    , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Assassin                  : WorksPrm( dispName="暗殺者"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.FortuneTeller             : WorksPrm( dispName="占い師"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Artist                    : WorksPrm( dispName="アーティスト"     , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Singer                    : WorksPrm( dispName="歌手"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Actor                     : WorksPrm( dispName="俳優"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Magician                  : WorksPrm( dispName="奇術師"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Athlete                   : WorksPrm( dispName="アスリート"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Fighter                   : WorksPrm( dispName="格闘家"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Reporter                  : WorksPrm( dispName="記者"            , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Announcer                 : WorksPrm( dispName="アナウンサー"     , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Programmer                : WorksPrm( dispName="プログラマー"     , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Hacker                    : WorksPrm( dispName="ハッカー"        , factor="", skills=["", "", "", "", "", ] ),
        eWorks.JackOfAllTrades           : WorksPrm( dispName="何でも屋"        , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Informer                  : WorksPrm( dispName="情報屋"          , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Operative                 : WorksPrm( dispName="工作員"          , factor="", skills=["", "", "", "", "", ] ),
    }

    @classmethod
    def getWorksPrm( cls, id : eWorks ) :
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eWorks ) :
        return cls.prm[id].dispName
    @classmethod
    def getFactor( cls, id : eWorks ) :
        return cls.prm[id].factor
    @classmethod
    def getSkills( cls, id : eWorks ) :
        return cls.prm[id].skills

