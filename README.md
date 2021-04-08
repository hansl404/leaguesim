# Random League Simulator

LeagueSim is a random text-based scenario simulator resembling League of Legends. The idea was inspired by BrantSteele's Hunger Games Simulator (https://brantsteele.net/hungergames/disclaimer.php). This project is currently a work in progress, as I hope to clean up the code and add some new features as I learn more about Python. 

## How to Play
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

## How it Works
- The game is divided into 2 stages: The "early" game and "late" game. When all player names are entered, the program will start in the "early" game, which is represents the laning phase in League. In the beginning, each player is assigned to a lane based on the order the names were entered. For each laning phase event, 1 of 3 things will happen for each of the 5 lanes (top, jg, mid, adc, sup): nothing, solokill, or gank. 
- If the event is "solokill", one laner will randomly gain a kill while the other corresponding laner will gain a death. If the lane that this happens is support, the ADC's will get the kill instead.
- If the event is "gank", 1 of 3 things can happen: 
  1. A laner gets a death while the other laner gets a kill and their jungler gets an assist
  2. A laner escapes the gank and nothing happens
  3. The laner getting ganked survives and kills either the other laner, the jungler, or both
- If the lane getting ganked is "support" the jungler will pick up the kill instead of the support.
- The "early" game will run exactly 5 times, meaning there will be 5 different early-game events.
- After all "early" game events are completed, the program will transition to "late" game events.
