"""Configuration settings for the Digimon Randomizer"""
from pathlib import Path
from typing import Dict, List
from dataclasses import dataclass, field

@dataclass
class DigimonStages:
    """Digimon evolution stages and their corresponding IDs"""
    BABY: List[int] = field(default_factory=lambda: [629,387,437,317,320])
    BABY_TWO: List[int] = field(default_factory=lambda: [62,322,512,438,631,325,515,567,510,514,388,321])
    CHILD: List[int] = field(default_factory=lambda: [50,143,63,707,81,564,582,55,569,151,713,90,53,626,595,111,343,709,697,728,20,701,303,708,457,208,112,9,96,687,348,97,307,705,42,114,361,389,706,607,458,56,390,2,391,750,392,190,781,682,761,762,763,764,765])
    ADULT: List[int] = field(default_factory=lambda: [102,730,758,15,676,64,711,344,377,680,393,11,365,87,394,341,760,68,304,455,710,12,714,395,78,630,326,712,398,367,399,729,218,209,113,5,452,30,58,347,130,54,313,14,91,16,698,755,621,759,363,92,93,349,396,375,70,308,115,13,397,22,752,43,314,702,10,369,370,548,25,590,72,3,77,454,191,783,716])
    PERFECT: List[int] = field(default_factory=lambda: [305,65,731,342,756,627,85,210,679,400,311,148,401,309,681,402,44,727,211,403,26,4,719,723,379,720,79,404,6,345,116,405,129,84,23,374,406,699,376,33,407,718,576,408,409,41,596,410,82,584,753,177,411,21,101,59,31,74,412,132,134,302,327,364,413,61,721,71,73,722,359,39,107,140,715,726,192,751])
    ULTIMATE: List[int] = field(default_factory=lambda: [66,416,417,451,732,419,346,773,117,600,27,421,744,677,150,422,688,127,754,423,32,704,83,734,774,735,48,424,425,749,94,737,86,213,315,741,771,745,440,128,733,632,38,126,738,700,739,743,19,75,426,60,36,49,427,428,69,175,429,214,450,306,35,439,310,453,431,678,675,748,24,747,95,385,47,312,135,182,434,80,383,37,34,740,703,57,742,901,902,903,905,193,382,683,782,784])
    ULTIMATE_PLUS: List[int] = field(default_factory=lambda: [106,67,766,420,215,88,757,772,118,104,105,40,435,328,776,775,777,778,779,904])
    EATERS: List[int] = field(default_factory=lambda: [800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817])
    GATES: List[int] = field(default_factory=lambda: [818,819,820,821,822,823,824])

@dataclass
class Paths:
    """Path configurations for the randomizer"""
    BASE_DIR: Path = Path(".")
    BACKUP_DIR: Path = BASE_DIR / "backup"
    MOD_DIR: Path = BASE_DIR / "mods"
    INFO_DIR: Path = BASE_DIR / "infolist"
    
    def __post_init__(self):
        """Ensure directories exist"""
        for path in [self.BACKUP_DIR, self.MOD_DIR, self.INFO_DIR]:
            path.mkdir(exist_ok=True)

@dataclass
class RandomizerConfig:
    """Main configuration for the randomizer"""
    paths: Paths = field(default_factory=Paths)
    stages: DigimonStages = field(default_factory=DigimonStages)
    item_ids: List[int] = field(default_factory=lambda: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,79,80,90,91,92,100,101,102,103,104,105,106,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231]) 