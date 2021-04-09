# Random League Simulator

LeagueSim is a random text-based scenario simulator resembling League of Legends. The idea was inspired by BrantSteele's Hunger Games Simulator (https://brantsteele.net/hungergames/disclaimer.php). While this simulator has been pretty accurate in resembling scores of a normal League game from my experience, I hope to clean up the code and add some new features as I learn more about Python. 

## How to play
- Upon running, press enter to confirm playing and enter the names of the players in scoreboard order: 

  1. Blue TOP
  2. Blue JUNGLE
  3. Blue MID
  4. Blue ADC 
  5. Blue SUPPORT 
  6. Red TOP 
  7. Red JUNGLE 
  8. Red MID 
  9. Red ADC 
  10. Red SUPPORT

- Upon entering the 10th player name, the first event will pop up. From that point on, a different "event" will happen every time enter is pressed. The overall scoreboard will be displayed for every event. When enough events happen and the simulation ends, the program will exit automatically and display which team won as well as the total game time.

## How it works
- The game is divided into 2 stages: The "early" game and "late" game. When all player names are entered, the program will start in the "early" game, which is represents the laning phase in League. In the beginning, each player is assigned to a lane based on the order the names were entered. How the event plays are determined by randomly generating a number (called a "roll"). An example of an early game event is...

9 min:

MID: Red gank...Success (Red gets 1)

ADC: Blue solokill

SUP: Red gank...Blunder! (Blue gets 2)
\
\
TOP: john: 0/2/0  vs:  bill: 2/0/0

JG : smith: 0/0/3  vs:  player: 1/1/3

MID: jane: 1/2/0  vs:  randoguy: 2/1/0

ADC: doe: 3/1/0  vs:  mundo: 1/3/0

SUP: joe: 2/1/0  vs:  me: 0/1/1


- For each laning phase event, 1 of 3 things will happen for each of the 5 lanes (top, jg, mid, adc, sup): nothing, solokill, or gank. 
- If the event is "solokill", one laner will randomly gain a kill while the other corresponding laner will gain a death. If the lane that this happens is support, the ADC's will get the kill instead.
- If the event is "gank", 1 of 5 things can happen: 
  1. A laner gets a death while the other laner gets a kill and their jungler gets an assist (marked as "Success")
  2. A laner escapes the gank and nothing happens (marked as "Nothing")
  3. The laner getting ganked dies but kills the opposing laner and the jungler picks up the kill (marked as "Traded")
  4. The laner getting ganked survives and kills either the opposing laner (marked as "Fail")
  5. The laner getting ganked survives and kills both the opposing laner and jungler (marked as "Blunder")
- If the lane getting ganked is "support" the jungler will pick up the kill instead of the support.
- The "early" game will run exactly 5 times, meaning there will be 5 different early-game events.

- After all "early" game events are finished, each player will receive a bonus to the number they roll depending on the number of kills and assists received (the exact number can be found in file player.py). Instead of each lane having an event determined by a single player's roll, events will be determined by the sum of each team's role.
- After all "early" game events are completed, the program will transition to "late" game events. Unlike "early" game events, "late" game events can run a variable number of times, depending on how many towers the red and blue teams have. Each event will destroy a certain number of one team's towers depending on the event. If a team's number of towers drops below zero, the opposing team wins. An example of a "late" game event is...

19 min: 

Teamfight!

Red 4, Blue 0

1 towers taken


TOP: john: 2/5/1  vs:  bill: 4/2/4

JG : smith: 0/2/5  vs:  player: 4/1/8

MID: jane: 2/4/2  vs:  randoguy: 4/2/9

ADC: doe: 3/4/0  vs:  mundo: 4/3/5

SUP: joe: 3/3/1  vs:  me: 2/2/8


- Just like how "early" events have nothing, solokill, or gank, "late" game events are: pick, fight, and baron. 
- If the event is "pick" one random player from the team with the lower total roll will receive a death and one random player from the team with the higher roll will pick up a kill with a random number of players on the team with the higher roll receiving assists. After scores are calculated, the team that won the higher roll will destroy between 0-1 enemy towers.
- If the event is "fight", the team with the higher total roll will gain a total of between 3-5 kills while the team with the lower roll will gain a total of 0-2 kills. Assists will be distributed randomly. After scores are calculated, the team that won the higher roll will destroy between 0-2 enemy towers.
- If the event is "baron", the team with the higher roll will automatically destroy between 1-2 enemy towers.

## Differences with the actual game (possible improvements to be made)
- No player can die more than 10 times in the early/lane phase. While this is usually realistic, it doesn't model my top laner during promos.
- There is no "gold" in this simulation, only roll modifiers based on amount of kills and assists, so item spikes and more complicated mechanics are not modeled by this simulation.
- The number of kills supports get in this simulation will usually be lower than the other players, but they will sometimes be unrealisticly high because I have currently prevented supports from getting kills in the early game (which is also inaccurate because it assumes supports never take any kills during lane), but I didn't want to extend a handicap to the late game as well because supports sometimes do the most damage in the team. This may result in some ridiculous numbers, however.
- Taking baron only destroys towers and doesn't give any increased chances of winning later teamfights. It is not necessary to win a teamfight before taking baron so in this simulation baron may be taken a very large number of times but have little impact on who wins.
- Dragons, rift heralds, jungle camps, and CS are not factors in this simulation (perhaps later?)
- The laner will always take the kill during every gank, unless the lane is "support", in which case the jungler will take the kill.
- In teamfights, the team that rolls higher will always get between 3-5 kills while the other team will always get between 0-2 kills, which isn't very realistic, but it was a design choice to simplify the teamfight event.




