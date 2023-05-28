# coding: UTF-8

import weakref
from enum import IntEnum, auto, unique

# ################################################################################################
# ワークス
# ################################################################################################
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
        eWorks.ElementarySchoolStudent   : WorksPrm( dispName="小学生"           , factor="感覚", skills=["知覚（２）", "意志", "RC", "情報：噂話", "-", ] ),
        eWorks.MiddleSchoolStudent       : WorksPrm( dispName="中学生"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.HighSchoolStudent         : WorksPrm( dispName="高校生"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.BadStudent                : WorksPrm( dispName="不良学生"         , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UniversityStudent         : WorksPrm( dispName="大学生"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.PartTimeWorker            : WorksPrm( dispName="フリーター"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Teacher                   : WorksPrm( dispName="教師"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.HousewifeOrHusband        : WorksPrm( dispName="主婦・主夫"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnChildrenA              : WorksPrm( dispName="UGNチルドレンA"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnChildrenB              : WorksPrm( dispName="UGNチルドレンB"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnChildrenC              : WorksPrm( dispName="UGNチルドレンC"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnAgentA                 : WorksPrm( dispName="UGNエージェントA" , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnAgentB                 : WorksPrm( dispName="UGNエージェントB" , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnAgentC                 : WorksPrm( dispName="UGNエージェントC" , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnAgentD                 : WorksPrm( dispName="UGNエージェントD" , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnBranchManagerA         : WorksPrm( dispName="UGN支部長A"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnBranchManagerB         : WorksPrm( dispName="UGN支部長B"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnBranchManagerC         : WorksPrm( dispName="UGN支部長C"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.UgnBranchDirectorD        : WorksPrm( dispName="UGN支部長D"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Criminal                  : WorksPrm( dispName="刑事"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Discipline                : WorksPrm( dispName="鑑識"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Lawyer                    : WorksPrm( dispName="弁護士"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.DefensiveMember           : WorksPrm( dispName="防衛隊員"         , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Mercenary                 : WorksPrm( dispName="傭兵"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Researcher                : WorksPrm( dispName="研究者"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Professor                 : WorksPrm( dispName="教授"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Nurse                     : WorksPrm( dispName="看護師"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Doctor                    : WorksPrm( dispName="医者"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Politician                : WorksPrm( dispName="政治家"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Businessman               : WorksPrm( dispName="ビジネスマン"     , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Executive                 : WorksPrm( dispName="エグゼクティブ"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.BarBusiness               : WorksPrm( dispName="水商売"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Shopkeeper                : WorksPrm( dispName="商店主"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.ReligiousPerson           : WorksPrm( dispName="宗教家"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Detective                 : WorksPrm( dispName="探偵"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Bodyguard                 : WorksPrm( dispName="ボディーガード"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Driver                    : WorksPrm( dispName="ドライバー"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Yakuza                    : WorksPrm( dispName="ヤクザ"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Mafia                     : WorksPrm( dispName="マフィア"         , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Thief                     : WorksPrm( dispName="泥棒"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.EgoWetter                 : WorksPrm( dispName="エゴシエーター"   , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Assassin                  : WorksPrm( dispName="暗殺者"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.FortuneTeller             : WorksPrm( dispName="占い師"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Artist                    : WorksPrm( dispName="アーティスト"     , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Singer                    : WorksPrm( dispName="歌手"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Actor                     : WorksPrm( dispName="俳優"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Magician                  : WorksPrm( dispName="奇術師"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Athlete                   : WorksPrm( dispName="アスリート"       , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Fighter                   : WorksPrm( dispName="格闘家"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Reporter                  : WorksPrm( dispName="記者"             , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Announcer                 : WorksPrm( dispName="アナウンサー"     , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Programmer                : WorksPrm( dispName="プログラマー"     , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Hacker                    : WorksPrm( dispName="ハッカー"         , factor="", skills=["", "", "", "", "", ] ),
        eWorks.JackOfAllTrades           : WorksPrm( dispName="何でも屋"         , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Informer                  : WorksPrm( dispName="情報屋"           , factor="", skills=["", "", "", "", "", ] ),
        eWorks.Operative                 : WorksPrm( dispName="工作員"           , factor="", skills=["", "", "", "", "", ] ),
    }

    @classmethod
    def getPrm( cls, id : eWorks ) :
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

# ################################################################################################
# 出自
# ################################################################################################
@unique
class eBirthPlace(IntEnum):
    solitude                = auto() # 天涯孤独
    parentless              = auto() # 父親（母親）不在
    parentInLaw             = auto() # 義理の両親
    memberOfAssociation     = auto() # 結社の一員
    politicalPower          = auto() # 政治権力
    pedigreeOfPower         = auto() # 権力者の血統
    wealthyMan              = auto() # 資産家
    celebrity               = auto() # 有名人
    brother                 = auto() # 兄弟
    sister                  = auto() # 姉妹
    bomOfFamousFamily       = auto() # 名家の生まれ
    parentsUnderstanding    = auto() # 親の理解
    poor                    = auto() # 貧乏
    sparseChild             = auto() # 疎まれた子
    awaitedChild            = auto() # 待ち望まれた子
    stableFamily            = auto() # 安定した家庭
    alienationWithRelatives = auto() # 親戚と疎遠
    MultipleBrothers        = auto() # 複数の兄弟姉妹がいる
    twins                   = auto() # 双子
    criminalChild           = auto() # 犯罪者の子


class BirthPlacePrm :
    """ 出自パラメータ class """
    def __init__(self, dispName : str, recommendedRois : str = "" ) :
        # instance vars
        self.dispName  = dispName
        self.recommendedLois = recommendedRois
    def __del__(self) :
        pass
    

class BirthPlace :
    """ 出自 class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eBirthPlace.solitude                : BirthPlacePrm( dispName="天涯孤独"             , recommendedRois="理解者"        ),
        eBirthPlace.parentless              : BirthPlacePrm( dispName="父親（母親）不在"     , recommendedRois="父親（母親）"  ),
        eBirthPlace.parentInLaw             : BirthPlacePrm( dispName="義理の両親"           , recommendedRois="義理の親"      ),
        eBirthPlace.memberOfAssociation     : BirthPlacePrm( dispName="結社の一員"           , recommendedRois="結社員"        ),
        eBirthPlace.politicalPower          : BirthPlacePrm( dispName="政治権力"             , recommendedRois="父親（母親）"  ),
        eBirthPlace.pedigreeOfPower         : BirthPlacePrm( dispName="権力者の血統"         , recommendedRois="教育者"        ),
        eBirthPlace.wealthyMan              : BirthPlacePrm( dispName="資産家"               , recommendedRois="父親（母親）"  ),
        eBirthPlace.celebrity               : BirthPlacePrm( dispName="有名人"               , recommendedRois="父親（母親）"  ),
        eBirthPlace.brother                 : BirthPlacePrm( dispName="兄弟"                 , recommendedRois="兄（弟）"      ),
        eBirthPlace.sister                  : BirthPlacePrm( dispName="姉妹"                 , recommendedRois="姉（妹）"      ),
        eBirthPlace.bomOfFamousFamily       : BirthPlacePrm( dispName="名家の生まれ"         , recommendedRois="父親（母親）"  ),
        eBirthPlace.parentsUnderstanding    : BirthPlacePrm( dispName="親の理解"             , recommendedRois="父親（母親）"  ),
        eBirthPlace.poor                    : BirthPlacePrm( dispName="貧乏"                 , recommendedRois="友人"          ),
        eBirthPlace.sparseChild             : BirthPlacePrm( dispName="疎まれた子"           , recommendedRois="親戚"          ),
        eBirthPlace.awaitedChild            : BirthPlacePrm( dispName="待ち望まれた子"       , recommendedRois="家族"          ),
        eBirthPlace.stableFamily            : BirthPlacePrm( dispName="安定した家庭"         , recommendedRois="父親（母親）"  ),
        eBirthPlace.alienationWithRelatives : BirthPlacePrm( dispName="親戚と疎遠"           , recommendedRois="親戚"          ),
        eBirthPlace.MultipleBrothers        : BirthPlacePrm( dispName="複数の兄弟姉妹がいる" , recommendedRois="兄弟姉妹"      ),
        eBirthPlace.twins                   : BirthPlacePrm( dispName="双子"                 , recommendedRois="双子"          ),
        eBirthPlace.criminalChild           : BirthPlacePrm( dispName="犯罪者の子"           , recommendedRois="父親（母親）"  ),
    }

    @classmethod
    def getPrm( cls, id : eWorks ) :
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eWorks ) :
        return cls.prm[id].dispName
    @classmethod
    def getRecommendedLois( cls, id : eWorks ) :
        return cls.prm[id].recommendedLois

# ################################################################################################
# 経験
# ################################################################################################
@unique
class eStudentExperience(IntEnum):
    mediocre                = auto() # 平凡
    eternalParting          = auto() # 永劫の別れ
    longtermHospitalization = auto() # 長期入院
    majorAccident           = auto() # 大事故
    deathAndRegeneration    = auto() # 死と再生
    loss                    = auto() # 喪失
    killing                 = auto() # 殺傷
    news                    = auto() # ニュース
    livingAbroad            = auto() # 海外生活
    greatSuccess            = auto() # 大成功
    trauma                  = auto() # トラウマ
    escape                  = auto() # 逃走
    firstLove               = auto() # 初恋
    transferring            = auto() # 転校
    bigTurninngPoint        = auto() # 大きな転機
    smallHonor              = auto() # 小さな名誉
    greatFailure            = auto() # 大失敗
    bestFriend              = auto() # 親友
    promise                 = auto() # 約束
    amnesia                 = auto() # 記憶喪失

class eSocietyExperience(IntEnum):
    mediocre                = auto() # 平凡
    eternalParting          = auto() # 永劫の別れ
    longtermHospitalization = auto() # 長期入院
    marriage                = auto() # 結婚
    deathAndRegeneration    = auto() # 死と再生
    loss                    = auto() # 喪失
    victim                  = auto() # 被害者
    news                    = auto() # ニュース
    livingAbroad            = auto() # 海外生活
    greatSuccess            = auto() # 大成功
    childTreasure           = auto() # 子宝
    advancement             = auto() # 出世
    brokenHeart             = auto() # 失恋
    busy                    = auto() # 多忙
    blankPeriod             = auto() # 空白期間
    bigFall                 = auto() # 大転落
    humiliation             = auto() # 屈辱
    ally                    = auto() # 盟友
    forbiddenLove           = auto() # 禁断の愛
    amnesia                 = auto() # 記憶喪失

class eUndergroundExperience(IntEnum):
    idleless                = auto() # 無為
    eternalParting          = auto() # 永劫の別れ
    longtermHospitalization = auto() # 長期入院
    majorAccident           = auto() # 大事故
    deathAndRegeneration    = auto() # 死と再生
    loss                    = auto() # 喪失
    crime                   = auto() # 犯罪
    threeSidedArticle       = auto() # 三面記事
    betayal                 = auto() # 裏切り
    rising                  = auto() # 成り上がり
    legend                  = auto() # 伝説
    infiniteCorridor        = auto() # 無限回廊
    greatLove               = auto() # 大恋愛
    dangerousWork           = auto() # 危険な仕事
    fightingDays            = auto() # 闘いの日々
    inspiredWound           = auto() # 消せない傷
    defeat                  = auto() # 敗北
    insulation              = auto() # 絶縁
    wolf                    = auto() # 一匹狼
    amnesia                 = auto() # 記憶喪失

class eUgnExperience(IntEnum):
    loyaltyToUGN            = auto() # UGNへの忠誠
    runawayOfPower          = auto() # 力の暴走
    subject                 = auto() # 実験体
    wallOfMind              = auto() # 心の壁
    deathOfFriend           = auto() # 仲間の死
    secret                  = auto() # 秘密
    betrayal                = auto() # 裏切った
    betrayed                = auto() # 裏切られた
    longingForMediocre      = auto() # 平凡への憧れ
    reboundIntoMediocre     = auto() # 平凡への反発
    amnesia                 = auto() # 記憶喪失
    escape                  = auto() # 脱走
    oldSoldier              = auto() # 古強者
    technicalField          = auto() # 技術畑
    enemyOrganization       = auto() # 敵性組織
    pureCulture             = auto() # 純粋培養
    greatVictory            = auto() # 大勝利
    dirtyWork               = auto() # 汚れ仕事
    bigBlunder              = auto() # 大失態
    aweForUGN               = auto() # UGNへの畏怖

class ExperiencePrm :
    """ 経験パラメータ class """
    def __init__(self, dispName : str, recommendedRois : str = "" ) :
        # instance vars
        self.dispName  = dispName
        self.recommendedLois = recommendedRois
    def __del__(self) :
        pass
    

class StudendExperience :
    """ 経験 class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eStudentExperience.mediocre                : BirthPlacePrm( dispName="平凡"         ),
        eStudentExperience.eternalParting          : BirthPlacePrm( dispName="永劫の別れ"   ),
        eStudentExperience.longtermHospitalization : BirthPlacePrm( dispName="長期入院"     ),
        eStudentExperience.majorAccident           : BirthPlacePrm( dispName="大事故"       ),
        eStudentExperience.deathAndRegeneration    : BirthPlacePrm( dispName="死と再生"     ),
        eStudentExperience.loss                    : BirthPlacePrm( dispName="喪失"         ),
        eStudentExperience.killing                 : BirthPlacePrm( dispName="殺傷"         ),
        eStudentExperience.news                    : BirthPlacePrm( dispName="ニュース"     ),
        eStudentExperience.livingAbroad            : BirthPlacePrm( dispName="海外生活"     ),
        eStudentExperience.greatSuccess            : BirthPlacePrm( dispName="大成功"       ),
        eStudentExperience.trauma                  : BirthPlacePrm( dispName="トラウマ"     ),
        eStudentExperience.escape                  : BirthPlacePrm( dispName="逃走"         ),
        eStudentExperience.firstLove               : BirthPlacePrm( dispName="初恋"         ),
        eStudentExperience.transferring            : BirthPlacePrm( dispName="転校"         ),
        eStudentExperience.bigTurninngPoint        : BirthPlacePrm( dispName="大きな転機"   ),
        eStudentExperience.smallHonor              : BirthPlacePrm( dispName="小さな名誉"   ),
        eStudentExperience.greatFailure            : BirthPlacePrm( dispName="大失敗"       ),
        eStudentExperience.bestFriend              : BirthPlacePrm( dispName="親友"         ),
        eStudentExperience.promise                 : BirthPlacePrm( dispName="約束"         ),
        eStudentExperience.amnesia                 : BirthPlacePrm( dispName="記憶喪失"     ),
    }

    @classmethod
    def getPrm( cls, id : eStudentExperience ) -> ExperiencePrm:
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eStudentExperience ) -> str:
        return cls.prm[id].dispName
    @classmethod
    def getRecommendedLois( cls, id : eStudentExperience ) -> str:
        return cls.prm[id].recommendedLois

class SocietyExperience :
    """ 経験 class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eSocietyExperience.mediocre                : BirthPlacePrm( dispName="平凡"       ),
        eSocietyExperience.eternalParting          : BirthPlacePrm( dispName="永劫の別れ" ),
        eSocietyExperience.longtermHospitalization : BirthPlacePrm( dispName="長期入院"   ),
        eSocietyExperience.marriage                : BirthPlacePrm( dispName="結婚"       ),
        eSocietyExperience.deathAndRegeneration    : BirthPlacePrm( dispName="死と再生"   ),
        eSocietyExperience.loss                    : BirthPlacePrm( dispName="喪失"       ),
        eSocietyExperience.victim                  : BirthPlacePrm( dispName="被害者"     ),
        eSocietyExperience.news                    : BirthPlacePrm( dispName="ニュース"   ),
        eSocietyExperience.livingAbroad            : BirthPlacePrm( dispName="海外生活"   ),
        eSocietyExperience.greatSuccess            : BirthPlacePrm( dispName="大成功"     ),
        eSocietyExperience.childTreasure           : BirthPlacePrm( dispName="子宝"       ),
        eSocietyExperience.advancement             : BirthPlacePrm( dispName="出世"       ),
        eSocietyExperience.brokenHeart             : BirthPlacePrm( dispName="失恋"       ),
        eSocietyExperience.busy                    : BirthPlacePrm( dispName="多忙"       ),
        eSocietyExperience.blankPeriod             : BirthPlacePrm( dispName="空白期間"   ),
        eSocietyExperience.bigFall                 : BirthPlacePrm( dispName="大転落"     ),
        eSocietyExperience.humiliation             : BirthPlacePrm( dispName="屈辱"       ),
        eSocietyExperience.ally                    : BirthPlacePrm( dispName="盟友"       ),
        eSocietyExperience.forbiddenLove           : BirthPlacePrm( dispName="禁断の愛"   ),
        eSocietyExperience.amnesia                 : BirthPlacePrm( dispName="記憶喪失"   ),
    }

    @classmethod
    def getPrm( cls, id : eSocietyExperience ) -> ExperiencePrm:
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eSocietyExperience ) -> str:
        return cls.prm[id].dispName
    @classmethod
    def getRecommendedLois( cls, id : eSocietyExperience ) -> str:
        return cls.prm[id].recommendedLois

class UndergroundExperience :
    """ 経験 class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eUndergroundExperience.idleless                : BirthPlacePrm( dispName="無為"       ),
        eUndergroundExperience.eternalParting          : BirthPlacePrm( dispName="永劫の別れ" ),
        eUndergroundExperience.longtermHospitalization : BirthPlacePrm( dispName="長期入院"   ),
        eUndergroundExperience.majorAccident           : BirthPlacePrm( dispName="大事故"     ),
        eUndergroundExperience.deathAndRegeneration    : BirthPlacePrm( dispName="死と再生"   ),
        eUndergroundExperience.loss                    : BirthPlacePrm( dispName="喪失"       ),
        eUndergroundExperience.crime                   : BirthPlacePrm( dispName="犯罪"       ),
        eUndergroundExperience.threeSidedArticle       : BirthPlacePrm( dispName="三面記事"   ),
        eUndergroundExperience.betayal                 : BirthPlacePrm( dispName="裏切り"     ),
        eUndergroundExperience.rising                  : BirthPlacePrm( dispName="成り上がり" ),
        eUndergroundExperience.legend                  : BirthPlacePrm( dispName="伝説"       ),
        eUndergroundExperience.infiniteCorridor        : BirthPlacePrm( dispName="無限回廊"   ),
        eUndergroundExperience.greatLove               : BirthPlacePrm( dispName="大恋愛"     ),
        eUndergroundExperience.dangerousWork           : BirthPlacePrm( dispName="危険な仕事" ),
        eUndergroundExperience.fightingDays            : BirthPlacePrm( dispName="闘いの日々" ),
        eUndergroundExperience.inspiredWound           : BirthPlacePrm( dispName="消せない傷" ),
        eUndergroundExperience.defeat                  : BirthPlacePrm( dispName="敗北"       ),
        eUndergroundExperience.insulation              : BirthPlacePrm( dispName="絶縁"       ),
        eUndergroundExperience.wolf                    : BirthPlacePrm( dispName="一匹狼"     ),
        eUndergroundExperience.amnesia                 : BirthPlacePrm( dispName="記憶喪失"   ),
    }

    @classmethod
    def getPrm( cls, id : eUndergroundExperience ) -> ExperiencePrm:
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eUndergroundExperience ) -> str:
        return cls.prm[id].dispName
    @classmethod
    def getRecommendedLois( cls, id : eUndergroundExperience ) -> str:
        return cls.prm[id].recommendedLois

class UgnExperience :
    """ 経験 class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eUgnExperience.loyaltyToUGN            : BirthPlacePrm( dispName="UGNへの忠誠"  ),
        eUgnExperience.runawayOfPower          : BirthPlacePrm( dispName="力の暴走"     ),
        eUgnExperience.subject                 : BirthPlacePrm( dispName="実験体"       ),
        eUgnExperience.wallOfMind              : BirthPlacePrm( dispName="心の壁"       ),
        eUgnExperience.deathOfFriend           : BirthPlacePrm( dispName="仲間の死"     ),
        eUgnExperience.secret                  : BirthPlacePrm( dispName="秘密"         ),
        eUgnExperience.betrayal                : BirthPlacePrm( dispName="裏切った"     ),
        eUgnExperience.betrayed                : BirthPlacePrm( dispName="裏切られた"   ),
        eUgnExperience.longingForMediocre      : BirthPlacePrm( dispName="平凡への憧れ" ),
        eUgnExperience.reboundIntoMediocre     : BirthPlacePrm( dispName="平凡への反発" ),
        eUgnExperience.amnesia                 : BirthPlacePrm( dispName="記憶喪失"     ),
        eUgnExperience.escape                  : BirthPlacePrm( dispName="脱走"         ),
        eUgnExperience.oldSoldier              : BirthPlacePrm( dispName="古強者"       ),
        eUgnExperience.technicalField          : BirthPlacePrm( dispName="技術畑"       ),
        eUgnExperience.enemyOrganization       : BirthPlacePrm( dispName="敵性組織"     ),
        eUgnExperience.pureCulture             : BirthPlacePrm( dispName="純粋培養"     ),
        eUgnExperience.greatVictory            : BirthPlacePrm( dispName="大勝利"       ),
        eUgnExperience.dirtyWork               : BirthPlacePrm( dispName="汚れ仕事"     ),
        eUgnExperience.bigBlunder              : BirthPlacePrm( dispName="大失態"       ),
        eUgnExperience.aweForUGN               : BirthPlacePrm( dispName="UGNへの畏怖"  ),
    }

    @classmethod
    def getPrm( cls, id : eUgnExperience ) -> ExperiencePrm:
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eUgnExperience ) -> str:
        return cls.prm[id].dispName
    @classmethod
    def getRecommendedLois( cls, id : eUgnExperience ) -> str:
        return cls.prm[id].recommendedLois

