# coding: UTF-8

import weakref
from enum import IntEnum, auto, unique

# ################################################################################################
# パラメータID
# ################################################################################################
@unique
class ePrmId(IntEnum):
    charName              = auto()
    codeName              = auto()
    works                 = auto()
    cover                 = auto()
    age                   = auto()
    gender                = auto()
    zodiacSign            = auto()
    bodyHeight            = auto()
    bodyWeight            = auto()
    bloodType             = auto()
    memo                  = auto()
    playerName            = auto()
    resumeExp             = auto()
    birthPlace            = auto()
    experience            = auto()
    encount               = auto()
    arousal               = auto()
    impulse               = auto()
    erodedVal             = auto()
    appearance            = auto()
    maxHp                 = auto()
    regularStock          = auto()
    battleMove            = auto()
    movePoint             = auto()
    walletPoint           = auto()
    fullPowerMove         = auto()
    bodyPoint             = auto()
    sensePoint            = auto()
    mentalPoint           = auto()
    socialityPoint        = auto()
    bodyGrowthPoint       = auto()
    senseGrowthPoint      = auto()
    mentalGrowthPoint     = auto()
    socialityGrowthPoint  = auto()
    bodySkillPoint        = auto()
    senseSkillPoint       = auto()
    mentalSkillPoint      = auto()
    socialitySkillPoint   = auto()
    bleed                 = auto()
    syndrome              = auto()
    syndrome2             = auto()
    optionalSyndrome      = auto()
    effect                = auto()
    combo                 = auto()

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
    def getPrm( cls, id : eWorks ) -> WorksPrm:
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eWorks ) -> str:
        return cls.prm[id].dispName
    @classmethod
    def getFactor( cls, id : eWorks ) -> str:
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
class eExperienceList(IntEnum):
    student     = auto() # 学生
    sociality   = auto() # 社会人
    underground = auto() # 裏社会
    ugn         = auto() # UGN

class ExperienceListPrm:
    """ 経験表パラメータ """
    def __init__(self, dispName : str) :
        # instance vars
        self.dispName  = dispName
    def __del__(self) :
        pass

class ExperienceList:
    """ 経験表クラス """
    prm = {
        eExperienceList.student     : BirthPlacePrm( dispName="学生"   ),
        eExperienceList.sociality   : BirthPlacePrm( dispName="社会人" ),
        eExperienceList.underground : BirthPlacePrm( dispName="裏社会" ),
        eExperienceList.ugn         : BirthPlacePrm( dispName="UGN"    ),
    }

    @classmethod
    def getPrm( cls, id : eExperienceList ) -> ExperienceListPrm:
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eExperienceList ) -> str:
        return cls.prm[id].dispName

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

@unique
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

@unique
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

@unique
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
    

class StudentExperience :
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

# ################################################################################################
# 邂逅
# ################################################################################################
class Encount:
    """ 邂逅クラス """
    dict = {
        "自身"      : "敷島あやめ"                      ,
        "師匠"      : "玉野椿"                          ,
        "保護者"    : "霧谷雄吾"                        ,
        "恩人"      : "テレーズ・ブルム"                ,
        "主人"      : "霧谷雄吾"                        ,
        "借り"      : "ヨハン・C・コードウェル"         ,
        "いいひと"  : "谷修成"                          ,
        "家族"      : "神城早月"                        ,
        "友人"      : "敷島あやめ"                      ,
        "同志"      : "テレーズ・ブルム"                ,
        "ビジネス"  : "神城早月"                        ,
        "同行者"    : "玉野椿"                          ,
        "忘却"      : "アルフレッド・J・コードウェル"   ,
        "慕情"      : "姫宮由里香"                      ,
        "貸し"      : "猫川美亜"                        ,
        "幼子"      : "テレーズ・ブルム"                ,
        "腐れ縁"    : "春日恭二"                        ,
        "秘密"      : "ローザ・バスカヴィル"            ,
        "好敵手"    : "黒崎剛道"                        ,
        "殺意"      : "伊庭宗一"                        ,
    }
    
    @classmethod
    def getPerson(cls, relation: str):
        return cls.dict[str]

# ################################################################################################
# 覚醒
# ################################################################################################
@unique
class eArousal(IntEnum):
    death           = auto() # 死
    anger           = auto() # 憤怒
    prime           = auto() # 素体
    infection       = auto() # 感染
    craving         = auto() # 渇望
    ignorance       = auto() # 無知
    sacrifice       = auto() # 犠牲
    order           = auto() # 命令
    forcedObles     = auto() # 忘却
    exploration     = auto() # 探求
    compensastion   = auto() # 償い
    birth           = auto() # 生誕

class ArousalPrm :
    """ 覚醒パラメータ class """
    def __init__(self, dispName : str, erodedValue : int ) :
        # instance vars
        self.dispName  = dispName
        self.erodedVal = erodedValue
    def __del__(self) :
        pass
    

class Arousal :
    """ 覚醒 class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eArousal.death           : ArousalPrm(dispName="死"  , erodedValue=18 ),
        eArousal.anger           : ArousalPrm(dispName="憤怒", erodedValue=17 ),
        eArousal.prime           : ArousalPrm(dispName="素体", erodedValue=16 ),
        eArousal.infection       : ArousalPrm(dispName="感染", erodedValue=14 ),
        eArousal.craving         : ArousalPrm(dispName="渇望", erodedValue=17 ),
        eArousal.ignorance       : ArousalPrm(dispName="無知", erodedValue=15 ),
        eArousal.sacrifice       : ArousalPrm(dispName="犠牲", erodedValue=16 ),
        eArousal.order           : ArousalPrm(dispName="命令", erodedValue=15 ),
        eArousal.forcedObles     : ArousalPrm(dispName="忘却", erodedValue=17 ),
        eArousal.exploration     : ArousalPrm(dispName="探求", erodedValue=14 ),
        eArousal.compensastion   : ArousalPrm(dispName="償い", erodedValue=18 ),
        eArousal.birth           : ArousalPrm(dispName="生誕", erodedValue=17 ),
    }

    @classmethod
    def getPrm( cls, id : eArousal ) :
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eArousal ) :
        return cls.prm[id].dispName
    @classmethod
    def getErodedValue( cls, id : eArousal ) :
        return cls.prm[id].erodedVal

# ################################################################################################
# 衝動
# ################################################################################################
@unique
class eImpulse(IntEnum):
    release      = auto() # 解放
    suckingBlood = auto() # 吸血
    hunger       = auto() # 飢餓
    slaughter    = auto() # 殺戮
    destruction  = auto() # 破壊
    abusive      = auto() # 加虐
    disgust      = auto() # 嫌悪
    struggle     = auto() # 闘争
    delusion     = auto() # 妄想
    selfHarm     = auto() # 自傷
    fear         = auto() # 恐怖
    hatraed      = auto() # 憎悪

class ImpulsePrm :
    """ 衝動パラメータ class """
    def __init__(self, dispName : str, erodedValue : int ) :
        # instance vars
        self.dispName  = dispName
        self.erodedVal = erodedValue
    def __del__(self) :
        pass

class Impulse :
    """ 衝動 class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eImpulse.release      : ImpulsePrm(dispName="解放", erodedValue=18 ),
        eImpulse.suckingBlood : ImpulsePrm(dispName="吸血", erodedValue=17 ),
        eImpulse.hunger       : ImpulsePrm(dispName="飢餓", erodedValue=14 ),
        eImpulse.slaughter    : ImpulsePrm(dispName="殺戮", erodedValue=18 ),
        eImpulse.destruction  : ImpulsePrm(dispName="破壊", erodedValue=16 ),
        eImpulse.abusive      : ImpulsePrm(dispName="加虐", erodedValue=15 ),
        eImpulse.disgust      : ImpulsePrm(dispName="嫌悪", erodedValue=15 ),
        eImpulse.struggle     : ImpulsePrm(dispName="闘争", erodedValue=16 ),
        eImpulse.delusion     : ImpulsePrm(dispName="妄想", erodedValue=14 ),
        eImpulse.selfHarm     : ImpulsePrm(dispName="自傷", erodedValue=16 ),
        eImpulse.fear         : ImpulsePrm(dispName="恐怖", erodedValue=17 ),
        eImpulse.hatraed      : ImpulsePrm(dispName="憎悪", erodedValue=18 ),
    }

    @classmethod
    def getPrm( cls, id : eImpulse ) :
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eImpulse ) :
        return cls.prm[id].dispName
    @classmethod
    def getErodedValue( cls, id : eImpulse ) :
        return cls.prm[id].erodedVal

# ################################################################################################
# 感情
# ################################################################################################
class Feeling:
    positiveList = [
        "傾倒"      ,
        "好奇心"    ,
        "憧憬"      ,
        "尊敬"      ,
        "連帯感"    ,
        "慈愛"      ,
        "感服"      ,
        "純愛"      ,
        "友情"      ,
        "慕情"      ,
        "同情"      ,
        "意志"      ,
        "庇護"      ,
        "幸福感"    ,
        "信頼"      ,
        "執着"      ,
        "親近感"    ,
        "誠意"      ,
        "好意"      ,
        "有為"      ,
        "尽力"      ,
        "懐旧"      ,
    ]
    negativeList = [
        "侮蔑"      ,
        "食傷"      ,
        "脅威"      ,
        "嫉妬"      ,
        "悔悟"      ,
        "恐怖"      ,
        "不安"      ,
        "劣等感"    ,
        "疎外感"    ,
        "恥辱"      ,
        "憐憫"      ,
        "偏愛"      ,
        "憎悪"      ,
        "隔意"      ,
        "嫌悪"      ,
        "猜疑心"    ,
        "厭気"      ,
        "不信感"    ,
        "不快感"    ,
        "憤懣"      ,
        "敵愾心"    ,
        "無関心"    ,
    ]

# ################################################################################################
# ブリード
# ################################################################################################
@unique
class eBleed(IntEnum):
    pureBleed  = auto() # ピュアブリード
    crossBleed = auto() # クロスブリード
    triBleed   = auto() # トライブリード

class BleedPrm :
    """ ブリードパラメータ class """
    def __init__(self, dispName : str ) :
        # instance vars
        self.dispName   = dispName
    def __del__(self) :
        pass

class Bleed :
    """ ブリード class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eBleed.pureBleed  : BleedPrm(dispName="ピュアブリード"),
        eBleed.crossBleed : BleedPrm(dispName="クロスブリード"),
        eBleed.triBleed   : BleedPrm(dispName="トライブリード"),
    }

    @classmethod
    def getPrm( cls, id : eArousal ) :
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eArousal ) :
        return cls.prm[id].dispName

# ################################################################################################
# シンドローム
# ################################################################################################
@unique
class eSyndrome(IntEnum):
    empty      = auto() # 空白
    angelHalo  = auto() # エンジェルハィロゥ
    balor      = auto() # バロール
    blackDog   = auto() # ブラックドッグ
    bramStoker = auto() # ブラム＝ストーカー
    chimaera   = auto() # キュマイラ
    exile      = auto() # エグザイル
    hanuman    = auto() # ハヌマーン
    morpheus   = auto() # モルフェウス
    neumann    = auto() # ノイマン
    orcus      = auto() # オルクス
    saramandra = auto() # サラマンダー
    solaris    = auto() # ソラリス

class SyndromePrm :
    """ シンドロームパラメータ class """
    def __init__(self, dispName : str, bodyVal : int, senseVal : int, mentalVal : int, socialityVal : int ) :
        # instance vars
        self.dispName     = dispName
        self.bodyVal      = bodyVal
        self.senseVal     = senseVal
        self.mentalVal    = mentalVal
        self.socialityVal = socialityVal
        
    def __del__(self) :
        pass

class Syndrome :
    """ シンドローム class """
    # IDとパラメータを辞書型で管理する
    prm = {
        eSyndrome.empty      : SyndromePrm( dispName=""                   , bodyVal = 0, senseVal = 0, mentalVal = 0, socialityVal = 0 ),
        eSyndrome.angelHalo  : SyndromePrm( dispName="エンジェルハィロゥ" , bodyVal = 0, senseVal = 3, mentalVal = 1, socialityVal = 0 ),
        eSyndrome.balor      : SyndromePrm( dispName="バロール"           , bodyVal = 0, senseVal = 1, mentalVal = 3, socialityVal = 1 ),
        eSyndrome.blackDog   : SyndromePrm( dispName="ブラックドッグ"     , bodyVal = 2, senseVal = 1, mentalVal = 1, socialityVal = 0 ),
        eSyndrome.bramStoker : SyndromePrm( dispName="ブラム＝ストーカー" , bodyVal = 1, senseVal = 2, mentalVal = 1, socialityVal = 0 ),
        eSyndrome.chimaera   : SyndromePrm( dispName="キュマイラ"         , bodyVal = 3, senseVal = 0, mentalVal = 0, socialityVal = 1 ),
        eSyndrome.exile      : SyndromePrm( dispName="エグザイル"         , bodyVal = 2, senseVal = 1, mentalVal = 0, socialityVal = 1 ),
        eSyndrome.hanuman    : SyndromePrm( dispName="ハヌマーン"         , bodyVal = 1, senseVal = 1, mentalVal = 1, socialityVal = 1 ),
        eSyndrome.morpheus   : SyndromePrm( dispName="モルフェウス"       , bodyVal = 1, senseVal = 2, mentalVal = 0, socialityVal = 1 ),
        eSyndrome.neumann    : SyndromePrm( dispName="ノイマン"           , bodyVal = 0, senseVal = 0, mentalVal = 3, socialityVal = 1 ),
        eSyndrome.orcus      : SyndromePrm( dispName="オルクス"           , bodyVal = 0, senseVal = 1, mentalVal = 1, socialityVal = 2 ),
        eSyndrome.saramandra : SyndromePrm( dispName="サラマンダー"       , bodyVal = 2, senseVal = 0, mentalVal = 1, socialityVal = 1 ),
        eSyndrome.solaris    : SyndromePrm( dispName="ソラリス"           , bodyVal = 0, senseVal = 0, mentalVal = 1, socialityVal = 1 ),
    }

    @classmethod
    def getPrm( cls, id : eSyndrome ) :
        return cls.prm[id]
    @classmethod
    def getDispName( cls, id : eSyndrome ) :
        return cls.prm[id].dispName

# ################################################################################################
# エフェクト
# ################################################################################################
class EffectPrm:
    """ エフェクトパラメータ class """
    def __init__(self,
            dispName,
            syndrome,
            maxLevel,
            timing,
            skill,
            difficulty,
            target,
            reach,
            erodedVal,
            limit,
            diceNumChange = False,
            remarks : str = "",
            ruleBookPage = "",
            # その他適宜必要なフラグなどを後で追加する
            isForceSameSyndrome  : bool = False,
            isForceTarget        : bool = False,
            isForceRange         : bool = False,
            isAssignableSyndrome : bool = False,
        ):
        # vars
        self.dispName     = dispName
        self.syndrome     = syndrome
        self.maxLevel     = maxLevel
        self.timing       = timing
        self.difficulty   = difficulty
        self.skill        = skill
        self.target       = target
        self.reach        = reach
        self.erodedVal    = erodedVal
        self.limit        = limit
        self.remarks      = remarks
        self.ruleBookPage = ruleBookPage
        
        # flags
        self.isForceSameSyndrome  = isForceSameSyndrome 
        self.isForceTarget        = isForceTarget       
        self.isForceRange         = isForceRange        
        self.isAssignableSyndrome = isAssignableSyndrome


class Effect:
    """ エフェクト class """
    def __init__(self):
        pass
        
# ################################################################################################
# コンボ
# ################################################################################################
class ComboPrm:
    """ コンボパラメータ class """
    def __init__(self):
        self.effects = []
        
    def setEffects( self, effects : list[Effect] ) -> None :
        for effect in effects:
            self.effects.append( effect )

# ################################################################################################
# バフ
# ################################################################################################
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
