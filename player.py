from typing import List

class Player:
    """Create a league player"""
    
    roles: List[str] = ["TOP", "JG ", "MID", "ADC", "SUP"]
    
    name: str = ""
    kills: int = 0
    deaths: int = 0
    assists: int = 0
    roll: int = 0
    roll_mod: float = 0  # update this value mid/late-game, more kills = higher roll_mod
    respawning: bool = False  # for teamfights
    
    def __init__(self, name):
        self.name = name
        
    def getrole(self, pos) -> int:
        return self.roles[pos]
    
    def buyitems(self) -> None:   
        """modify roll stat"""
        self.roll_mod = self.kills * 0.7 + self.assists * 0.1   # changing this number increases the "snowball" factor, higher number = team with more kills having way bigger chance to win and getting more kills
