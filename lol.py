import random
from typing import List, Set
from player import Player

# Global Variables
blue_players: List[Player] = []
red_players: List[Player] = []

def main() -> None:
    """Entrypoint of program"""
    
    continue_msg: Str = "Press ENTER to continue...\n"
    
    input("Press ENTER to play...")
    
    blue_towers: int = 11
    blue_win: bool = False
    red_towers: int = 11
    red_win: bool = False
    game_time: int = 0
    
    for users in range(10):
        if (users < 5):
            username: str = input("Enter blue team username: ")
            player: Player = Player(username)
            blue_players.append(player)
        else:
            username: str = input("Enter red team username: ")
            player: Player = Player(username)
            red_players.append(player)
           
    input(continue_msg)

    # Game loop
    while blue_win == False and red_win == False:
        
        # Early Game (laning phase)
        while game_time < 15:
            early_game(game_time)
            print_scoreboard()
            game_time += 3
            input(continue_msg)
                 
        # Mid / Late game (our win check is above)
        
        while blue_towers >= 0 and red_towers >= 0:
            print(f"{game_time} min: \n")
            # call buyitems() for every player
            for p in range(5):
                blue_players[p].buyitems()
            for p2 in range(5):
                red_players[p2].buyitems()
                
            event: int = random.randint(0,2)    # 0 = pick, 1 = fight, 2 = baron
            
            # if event = pick
            if event == 0:
                towers_taken: int = take_towers(event)
                target_team: int = random.randint(0,1)  # 0 if blue player picked off, 1 is red player picked off
                contributors = set()  # contains the id of the people who helped with the pickoff
                
                for hl in range(5):   # up to 5 people can help with the pickoff
                    pid: int = random.randint(0,4)  
                    contributors.add(pid)
                    
                contributors_list: List[int] = list(contributors)  # convert the set to a list to be able to assign kill to 1 and assists to others

                if target_team == 0:  # blue team gets a pick
                    
                    target_player: int = random.randint(0,4)
                    red_players[target_player].deaths += 1
                    
                    collectorindex: int = random.randint(0, len(contributors_list)-1)       # pick a random player id to receive the kill gold
                    collectorid: int = contributors_list.pop(collectorindex)                # now we knew the id of the player to get the kill gold
                    blue_players[collectorid].kills += 1                         # contributors_list now only has the players who will get the assist gold
                    print(f"{red_players[target_player].name} (red) caught out!")
                    print(f"{blue_players[collectorid].name} (blue) collects the kill")
                    
                    for ap in range(len(contributors_list)):
                        helperid: int = contributors_list[ap]
                        blue_players[helperid].assists += 1
                       
                    red_towers -= towers_taken 
                                  
                elif target_team == 1:  # red team gets a pick
                    
                    target_player: int = random.randint(0,4)
                    blue_players[target_player].deaths += 1
                    
                    collectorindex: int = random.randint(0, len(contributors_list)-1)       # pick a random player id to receive the kill gold
                    collectorid: int = contributors_list.pop(collectorindex)                # now we knew the id of the player to get the kill gold
                    red_players[collectorid].kills += 1                         # contributors_list now only has the players who will get the assist gold
                    print(f"{blue_players[target_player].name} (blue) caught out!")
                    print(f"{red_players[collectorid].name} (red) collects the kill")
                    
                    for ap in range(len(contributors_list)):
                        helperid: int = contributors_list[ap]                      
                        red_players[helperid].assists += 1
                        
                    blue_towers -= towers_taken
                            
            # if fight:
            if event == 1:
                print("Teamfight!")
                blue_total: float = 0
                red_total: float = 0
                
                # everyone player gets a roll 
                for summoner in range(10):
                    roll: int = random.randint(0, 10)
                    if summoner < 5:
                        blue_players[summoner].roll = roll
                    else:
                        red_players[summoner % 5].roll = roll
                        
                # sum up rolls for everyone in blue / red including roll_mod for each player, stored in blue_total and red_total
                for sumroll in range(10):
                    if sumroll < 5:
                        blue_target: Player = blue_players[sumroll]
                        blue_total += blue_target.roll + blue_target.roll_mod
                    else:
                        red_target: Player = red_players[sumroll % 5]
                        red_total += red_target.roll + red_target.roll_mod
                        
                # store the order in blue and red team players will be killed off (random)
                blue_order: List[int] = [0, 1, 2, 3, 4]
                red_order: List[int] = [0, 1, 2, 3, 4]
                random.shuffle(blue_order)
                random.shuffle(red_order)
               
                # team with higher roll will pick up 3-5 kills while team with lower will pick up 0-2
                winkills: int = random.randint(3,5)
                losekills: int = random.randint(0,2)
                
                # winning team gets 3, 4, or 5 kills, losing team gets 0, 1, or 2
                if blue_total > red_total:    
                    
                    # determine the kills and assists for blue team (winners)
                    for winner_pickoff in range(winkills):
                        contributors = set()  # contains the id of the people who helped with the pickoff
                        for hl in range(5):   # up to 5 people can help with the pickoff
                            pid: int = random.randint(0,4)  
                            contributors.add(pid)
                        contributors_list: List[int] = list(contributors)  # convert the set to a list to be able to assign kill to 1 and assists to others
                        
                        red_players[red_order[winner_pickoff]].deaths += 1
                        collectorindex: int = random.randint(0, len(contributors_list)-1)       # pick a random player id to receive the kill gold
                        collectorid: int = contributors_list.pop(collectorindex)                # now we knew the id of the player to get the kill gold
                        blue_players[collectorid].kills += 1                         # contributors_list now only has the players who will get the assist gold
                        
                        for ap in range(len(contributors_list)):
                            helperid: int = contributors_list[ap]
                            blue_players[helperid].assists += 1
                            
                    # determine kills and assists for red team (losers)      
                    for loser_pickoff in range(losekills):
                        contributors2 = set()
                        for hl2 in range(5):
                            pid2: int = random.randint(0,4)
                            contributors2.add(pid2)
                        contributors_list2: List[int] = list(contributors2)
                        
                        blue_players[blue_order[loser_pickoff]].deaths += 1
                        collectorindex2: int = random.randint(0, len(contributors_list2)-1)
                        collectorid2: int = contributors_list2.pop(collectorindex2)
                        red_players[collectorid2].kills += 1
                        for ap2 in range(len(contributors_list2)):
                            helperid2: int = contributors_list2[ap2]
                            red_players[helperid2].assists += 1
                        
                    print(f"Blue {winkills}, Red {losekills}")
                    towers_taken: int = take_towers(event)
                    red_towers -= towers_taken
                                            
                elif red_total > blue_total:
                    # determine the kills and assists for red team (winners)
                    for winner_pickoff in range(winkills):
                        contributors = set()  # contains the id of the people who helped with the pickoff
                        for hl in range(5):   # up to 5 people can help with the pickoff
                            pid: int = random.randint(0,4)  
                            contributors.add(pid)
                        contributors_list: List[int] = list(contributors)  # convert the set to a list to be able to assign kill to 1 and assists to others
                        
                        blue_players[red_order[winner_pickoff]].deaths += 1
                        collectorindex: int = random.randint(0, len(contributors_list)-1)       # pick a random player id to receive the kill gold
                        collectorid: int = contributors_list.pop(collectorindex)                # now we knew the id of the player to get the kill gold
                        red_players[collectorid].kills += 1                         # contributors_list now only has the players who will get the assist gold
                        
                        for ap in range(len(contributors_list)):
                            helperid: int = contributors_list[ap]
                            red_players[helperid].assists += 1
                            
                    # determine kills and assists for blue team (losers)      
                    for loser_pickoff in range(losekills):
                        contributors2 = set()
                        for hl2 in range(5):
                            pid2: int = random.randint(0,4)
                            contributors2.add(pid2)
                        contributors_list2: List[int] = list(contributors2)
                        
                        red_players[blue_order[loser_pickoff]].deaths += 1
                        collectorindex2: int = random.randint(0, len(contributors_list2)-1)
                        collectorid2: int = contributors_list2.pop(collectorindex2)
                        blue_players[collectorid2].kills += 1
                        for ap2 in range(len(contributors_list2)):
                            helperid2: int = contributors_list2[ap2]
                            blue_players[helperid2].assists += 1   
                                         
                    print(f"Red {winkills}, Blue {losekills}")      
                    towers_taken: int = take_towers(event)
                    blue_towers -= towers_taken  
                    
                # even teamfight, both teams end up the same (VERY RARE)
                elif blue_total == red_total:    
                    numkills: int = random.randint(0,4)
                    # determine the kills and assists for blue team (winners)
                    for winner_pickoff in range(numkills):
                        contributors = set()  # contains the id of the people who helped with the pickoff
                        for hl in range(5):   # up to 5 people can help with the pickoff
                            pid: int = random.randint(0,4)  
                            contributors.add(pid)
                            
                        contributors_list: List[int] = list(contributors)  # convert the set to a list to be able to assign kill to 1 and assists to others
                        red_players[red_order[winner_pickoff]].deaths += 1
                        collectorindex: int = random.randint(0, len(contributors_list)-1)       # pick a random player id to receive the kill gold
                        collectorid: int = contributors_list.pop(collectorindex)                # now we knew the id of the player to get the kill gold
                        blue_players[collectorid].kills += 1                         # contributors_list now only has the players who will get the assist gold
                        
                        for ap in range(len(contributors_list)):
                            helperid: int = contributors_list[ap]
                            blue_players[helperid].assists += 1    
                    # determine kills and assists for red team (losers)      
                    for loser_pickoff in range(numkills):
                        contributors2 = set()
                        for hl2 in range(5):
                            pid2: int = random.randint(0,4)
                            contributors2.add(pid2)
                        
                        contributors_list2: List[int] = list(contributors2)
                        blue_players[blue_order[loser_pickoff]].deaths += 1
                        collectorindex2: int = random.randint(0, len(contributors_list2)-1)
                        collectorid2: int = contributors_list2.pop(collectorindex2)
                        red_players[collectorid2].kills += 1
                        
                        for ap2 in range(len(contributors_list2)):
                            helperid2: int = contributors_list2[ap2]
                            red_players[helperid2].assists += 1
                            
                    print(f"Even Fight: Blue {numkills}, Red {numkills}")
                    
                            
            # if baron                
            if event == 2:
                blue_total: int = 0
                red_total: int = 0
                
                # everyone player gets a roll 
                for summoner in range(10):
                    roll: int = random.randint(0, 10)
                    if summoner < 5:
                        blue_players[summoner].roll = roll
                    else:
                        red_players[summoner % 5].roll = roll       
                # sum up rolls for everyone in blue / red including roll_mod for each player, stored in blue_total and red_total
                for sumroll in range(10):
                    if sumroll < 5:
                        blue_target: Player = blue_players[sumroll]
                        blue_total += blue_target.roll + blue_target.roll_mod
                    else:
                        red_target: Player = red_players[sumroll % 5]
                        red_total += red_target.roll + red_target.roll_mod
                        

                if blue_total > red_total:
                    print("Blue team takes baron")
                    towers_taken: int = take_towers(event)
                    red_towers -= towers_taken
                elif red_total > blue_total:
                    print("Red team takes baron")
                    towers_taken: int = take_towers(event)
                    blue_towers -= towers_taken
                
            print_scoreboard()      
                   
            # End the game and display message
            if blue_towers < 0:
                print("======================================")
                print(f"Red team wins in {game_time} min!")
                print("======================================")
                red_win = True
            elif red_towers < 0:
                print("======================================")
                print(f"Blue team wins in {game_time} min!")
                print("======================================")
                blue_win = True


            game_time += 1
            
            # display continue or exit based on whether or not the game ended
            if blue_win or red_win:
                quit()
            else: 
                input(continue_msg)
        
    
def take_towers(event: int) -> int:
    """randomly determine how many towers were taken based on the event that happened when called"""
    if event == 0:
        towers_down = random.randint(0,1)
        print(f"{towers_down} towers taken")
        return towers_down
    elif event == 1:
        towers_down = random.randint(0,2)
        print(f"{towers_down} towers taken")
        return towers_down
    elif event == 2:
        towers_down = random.randint(1,2)
        print(f"{towers_down} towers taken")
        return towers_down
    
    
def print_scoreboard() -> None:
    print("")     
    global blue_players
    global red_players
    for x in range(5):
        bp = blue_players[x]
        rp = red_players[x]
        print(f"{bp.getrole(x)}: {bp.name}: {bp.kills}/{bp.deaths}/{bp.assists}  vs:  " + f"{rp.name}: {rp.kills}/{rp.deaths}/{rp.assists}")            
    print("--------------------------------------")
   
    
def early_game(time) -> None:
    print(f"{time} min:\n")
    # Each player is given a "roll" to determine how good they are this round
    for summoner in range(10):
        roll: int = random.randint(0, 10)
        if summoner < 5:
            blue_players[summoner].roll = roll
        else:
            red_players[summoner % 5].roll = roll
            
        # Each lane will have an "event" (numbered 0 - 2)
    for lane in range(5): 
        event: int = random.randint(0, 2)   # 0 = nothing, 1 = solokill, 2 = gank
        blue: Player = blue_players[lane]
        red: Player = red_players[lane]
                  
        if lane == 1:
            event = random.randint(0, 1)   # jg cant gank themselves, so remove the possibility of event 2
                
        # Solokill
        if event == 1: 
            if blue.roll > red.roll:
                blue.kills += 1
                red.deaths += 1
                if lane != 4:   # print a different message (defined below) if we are on role SUP
                    print(f"{blue.getrole(lane)}: Blue solokill")
                # Supports dont get solokills, so streat it as a 2v2 instead
                if lane == 4:
                    blue.kills -= 1
                    blue.assists += 1
                    blue_players[3].kills += 1
                    print(f"{blue.getrole(lane)}: Blue 2v2 kill")
            elif red.roll > blue.roll:
                red.kills += 1
                blue.deaths += 1
                if lane != 4:  # print a different message (defined below) if we are on the role SUP   
                    print(f"{red.getrole(lane)}: Red solokill")
                    # Supports dont get solokills, so treat it as a 2v2 win instead
                if lane == 4:
                    red.kills -= 1
                    red.assists += 1
                    red_players[3].kills += 1
                    print(f"{red.getrole(lane)}: Red 2v2 kill")
                        
        # Gank        
        elif event == 2:  # Gank
            whichjg: int = random.randint(0, 1)  # 0 if blue gank, 1 is red gank
                    
            # Blue gank
            if whichjg == 0:
                bluejg: Player = blue_players[1]
                        
                if blue.roll + bluejg.roll > red.roll:  # blue gank successful
                    blue.kills += 1
                    bluejg.assists += 1
                    red.deaths += 1
                    if lane == 4:     # is support is the role getting ganked, the jg gets the kill
                        blue.kills -= 1
                        blue.assists += 1
                        blue_players[1].kills += 1
                        print(f"{blue.getrole(lane)}: Blue gank...Success")
                                
                elif blue.roll + bluejg.roll < red.roll:  # blue gank fail
                    if red.roll >= 9:  # red gets 2 (after rolling 9 or 10)
                        blue.deaths += 1
                        bluejg.deaths += 1
                        red.kills += 2
                        print(f"{blue.getrole(lane)}: Blue gank...Blunder!")
                    elif red.roll >= 7:  # red gets 1 (after rolling 7 or 8)
                        blue.deaths += 1
                        red.kills += 1
                        print(f"{blue.getrole(lane)}: Blue gank...Traded")
                    else:
                        print(f"{blue.getrole(lane)}: Blue gank...Nothing")
                    
            # Red gank
            else:
                redjg: Player = red_players[1]
                        
                if red.roll + redjg.roll > blue.roll:  # red gank successful
                    red.kills += 1
                    redjg.assists += 1
                    blue.deaths += 1
                    if lane == 4:   # if support is the one getting ganked, jg picks up the kill
                        red.kills -= 1
                        red.assists += 1
                        red_players[1].kills += 1
                        print(f"{red.getrole(lane)}: Red gank...Success")
                            
                elif red.roll + redjg.roll < blue.roll:  # red gank fail
                    if blue.roll >= 9:  # blue gets 2
                        red.deaths += 1
                        redjg.deaths += 1
                        blue.kills += 2
                        print(f"{red.getrole(lane)}: Red gank...Blunder!")

                    elif blue.roll >= 7:  # blue gets 1
                        red.deaths += 1
                        blue.kills += 1
                        print(f"{red.getrole(lane)}: Red gank...Traded")
                    else:
                        print(f"{red.getrole(lane)}: Red gank...Nothing")
                    

                # End of possible gank outcomes
                
    
if __name__ == "__main__":
    main()
    