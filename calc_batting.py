import json
import math
from random import random

STATS = [{"Curve Ball Speed": 130, "Fast Ball Speed": 168, "Cursed Ball": 60, "Curve": 53, "Curve Control": 50, "Char Id": 0, "Slap Contact Spot Size": 65, "Charge Contact Spot Size": 35, "Slap Hit Power": 50, "Charge Hit Power": 64, "Bunting": 35, "Speed": 50, "Throwing Arm": 60, "Weight": 2, "Captain Star Hit/Pitch": 1, "Non Captain Star Pitch": 2, "Batting Stat Bar": 6, "Pitching Stat Bar": 6, "Running Stat Bar": 5, "Fielding Stat Bar": 6, "Name": "Mario", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 1, "Non Captain Star Swing": 1, "Fielding Ability": 10}, {"Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 55, "Curve": 56, "Curve Control": 50, "Char Id": 1, "Slap Contact Spot Size": 70, "Charge Contact Spot Size": 40, "Slap Hit Power": 48, "Charge Hit Power": 59, "Bunting": 40, "Speed": 60, "Throwing Arm": 50, "Weight": 2, "Captain Star Hit/Pitch": 2, "Non Captain Star Pitch": 2, "Batting Stat Bar": 5, "Pitching Stat Bar": 6, "Running Stat Bar": 6, "Fielding Stat Bar": 6, "Name": "Luigi", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 1, "Non Captain Star Swing": 2, "Fielding Ability": 66}, {"Curve Ball Speed": 130, "Fast Ball Speed": 165, "Cursed Ball": 70, "Curve": 35, "Curve Control": 50, "Char Id": 2, "Slap Contact Spot Size": 30, "Charge Contact Spot Size": 15, "Slap Hit Power": 60, "Charge Hit Power": 80, "Bunting": 20, "Speed": 40, "Throwing Arm": 70, "Weight": 4, "Captain Star Hit/Pitch": 5, "Non Captain Star Pitch": 1, "Batting Stat Bar": 8, "Pitching Stat Bar": 7, "Running Stat Bar": 4, "Fielding Stat Bar": 4, "Name": "DK", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 1, "Vertical Hit Trajectory": 1, "Character Class": 1, "Can Be Captain": 1, "Non Captain Star Swing": 1, "Fielding Ability": 20}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 45, "Curve": 80, "Curve Control": 50, "Char Id": 3, "Slap Contact Spot Size": 45, "Charge Contact Spot Size": 15, "Slap Hit Power": 45, "Charge Hit Power": 30, "Bunting": 20, "Speed": 70, "Throwing Arm": 60, "Weight": 1, "Captain Star Hit/Pitch": 6, "Non Captain Star Pitch": 1, "Batting Stat Bar": 3, "Pitching Stat Bar": 6, "Running Stat Bar": 7, "Fielding Stat Bar": 7, "Name": "Diddy", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 1, "Non Captain Star Swing": 2, "Fielding Ability": 4}, {"Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 50, "Curve": 70, "Curve Control": 90, "Char Id": 4, "Slap Contact Spot Size": 80, "Charge Contact Spot Size": 45, "Slap Hit Power": 46, "Charge Hit Power": 45, "Bunting": 45, "Speed": 50, "Throwing Arm": 40, "Weight": 2, "Captain Star Hit/Pitch": 11, "Non Captain Star Pitch": 3, "Batting Stat Bar": 4, "Pitching Stat Bar": 8, "Running Stat Bar": 5, "Fielding Stat Bar": 7, "Name": "Peach", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 2, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 1, "Non Captain Star Swing": 2, "Fielding Ability": 32}, {"Curve Ball Speed": 120, "Fast Ball Speed": 160, "Cursed Ball": 55, "Curve": 60, "Curve Control": 55, "Char Id": 5, "Slap Contact Spot Size": 70, "Charge Contact Spot Size": 40, "Slap Hit Power": 49, "Charge Hit Power": 60, "Bunting": 55, "Speed": 40, "Throwing Arm": 40, "Weight": 2, "Captain Star Hit/Pitch": 12, "Non Captain Star Pitch": 3, "Batting Stat Bar": 6, "Pitching Stat Bar": 7, "Running Stat Bar": 4, "Fielding Stat Bar": 5, "Name": "Daisy", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 1, "Non Captain Star Swing": 1, "Fielding Ability": 40}, {"Curve Ball Speed": 120, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 51, "Curve Control": 50, "Char Id": 6, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 50, "Charge Hit Power": 45, "Bunting": 25, "Speed": 90, "Throwing Arm": 40, "Weight": 2, "Captain Star Hit/Pitch": 9, "Non Captain Star Pitch": 3, "Batting Stat Bar": 5, "Pitching Stat Bar": 4, "Running Stat Bar": 9, "Fielding Stat Bar": 6, "Name": "Yoshi", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 2, "Can Be Captain": 1, "Non Captain Star Swing": 2, "Fielding Ability": 4}, {"Curve Ball Speed": 115, "Fast Ball Speed": 150, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 7, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 25, "Slap Hit Power": 44, "Charge Hit Power": 30, "Bunting": 25, "Speed": 70, "Throwing Arm": 30, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 3, "Pitching Stat Bar": 5, "Running Stat Bar": 7, "Fielding Stat Bar": 3, "Name": "Baby Mario", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 2}, {"Curve Ball Speed": 115, "Fast Ball Speed": 150, "Cursed Ball": 40, "Curve": 50, "Curve Control": 50, "Char Id": 8, "Slap Contact Spot Size": 45, "Charge Contact Spot Size": 25, "Slap Hit Power": 42, "Charge Hit Power": 20, "Bunting": 25, "Speed": 80, "Throwing Arm": 30, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 2, "Pitching Stat Bar": 5, "Running Stat Bar": 8, "Fielding Stat Bar": 3, "Name": "Baby Luigi", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 2}, {"Curve Ball Speed": 120, "Fast Ball Speed": 175, "Cursed Ball": 90, "Curve": 35, "Curve Control": 50, "Char Id": 9, "Slap Contact Spot Size": 40, "Charge Contact Spot Size": 15, "Slap Hit Power": 60, "Charge Hit Power": 95, "Bunting": 20, "Speed": 10, "Throwing Arm": 70, "Weight": 4, "Captain Star Hit/Pitch": 7, "Non Captain Star Pitch": 2, "Batting Stat Bar": 9, "Pitching Stat Bar": 9, "Running Stat Bar": 1, "Fielding Stat Bar": 1, "Name": "Bowser", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 1, "Vertical Hit Trajectory": 1, "Character Class": 1, "Can Be Captain": 1, "Non Captain Star Swing": 1, "Fielding Ability": 17}, {"Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 80, "Curve": 30, "Curve Control": 50, "Char Id": 10, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 25, "Slap Hit Power": 55, "Charge Hit Power": 80, "Bunting": 25, "Speed": 30, "Throwing Arm": 60, "Weight": 3, "Captain Star Hit/Pitch": 3, "Non Captain Star Pitch": 2, "Batting Stat Bar": 8, "Pitching Stat Bar": 3, "Running Stat Bar": 3, "Fielding Stat Bar": 4, "Name": "Wario", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 1, "Can Be Captain": 1, "Non Captain Star Swing": 1, "Fielding Ability": 9}, {"Curve Ball Speed": 110, "Fast Ball Speed": 169, "Cursed Ball": 50, "Curve": 70, "Curve Control": 60, "Char Id": 11, "Slap Contact Spot Size": 90, "Charge Contact Spot Size": 40, "Slap Hit Power": 50, "Charge Hit Power": 1, "Bunting": 45, "Speed": 40, "Throwing Arm": 40, "Weight": 3, "Captain Star Hit/Pitch": 4, "Non Captain Star Pitch": 1, "Batting Stat Bar": 4, "Pitching Stat Bar": 9, "Running Stat Bar": 4, "Fielding Stat Bar": 4, "Name": "Waluigi", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 2, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 1, "Non Captain Star Swing": 3, "Fielding Ability": 80}, {"Curve Ball Speed": 120, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 12, "Slap Contact Spot Size": 70, "Charge Contact Spot Size": 30, "Slap Hit Power": 40, "Charge Hit Power": 50, "Bunting": 30, "Speed": 40, "Throwing Arm": 50, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 5, "Pitching Stat Bar": 4, "Running Stat Bar": 4, "Fielding Stat Bar": 5, "Name": "Koopa(R)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 8}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 13, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 45, "Charge Hit Power": 70, "Bunting": 25, "Speed": 60, "Throwing Arm": 50, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 5, "Pitching Stat Bar": 3, "Running Stat Bar": 6, "Fielding Stat Bar": 3, "Name": "Toad(R)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 0}, {"Curve Ball Speed": 120, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 90, "Curve Control": 60, "Char Id": 14, "Slap Contact Spot Size": 85, "Charge Contact Spot Size": 45, "Slap Hit Power": 40, "Charge Hit Power": 30, "Bunting": 50, "Speed": 40, "Throwing Arm": 40, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 3, "Pitching Stat Bar": 8, "Running Stat Bar": 4, "Fielding Stat Bar": 2, "Name": "Boo", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 64}, {"Curve Ball Speed": 115, "Fast Ball Speed": 150, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 15, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 44, "Charge Hit Power": 20, "Bunting": 25, "Speed": 90, "Throwing Arm": 40, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 2, "Pitching Stat Bar": 3, "Running Stat Bar": 9, "Fielding Stat Bar": 4, "Name": "Toadette", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 10}, {"Curve Ball Speed": 120, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 16, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 46, "Charge Hit Power": 55, "Bunting": 25, "Speed": 40, "Throwing Arm": 40, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 5, "Pitching Stat Bar": 3, "Running Stat Bar": 4, "Fielding Stat Bar": 5, "Name": "Shy Guy(R)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 8}, {"Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 60, "Curve": 40, "Curve Control": 50, "Char Id": 17, "Slap Contact Spot Size": 45, "Charge Contact Spot Size": 30, "Slap Hit Power": 55, "Charge Hit Power": 67, "Bunting": 20, "Speed": 40, "Throwing Arm": 60, "Weight": 3, "Captain Star Hit/Pitch": 10, "Non Captain Star Pitch": 2, "Batting Stat Bar": 6, "Pitching Stat Bar": 4, "Running Stat Bar": 4, "Fielding Stat Bar": 4, "Name": "Birdo", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 1, "Non Captain Star Swing": 1, "Fielding Ability": 1}, {"Curve Ball Speed": 120, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 18, "Slap Contact Spot Size": 40, "Charge Contact Spot Size": 30, "Slap Hit Power": 45, "Charge Hit Power": 30, "Bunting": 20, "Speed": 60, "Throwing Arm": 30, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 3, "Pitching Stat Bar": 3, "Running Stat Bar": 7, "Fielding Stat Bar": 5, "Name": "Monty", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 1}, {"Curve Ball Speed": 125, "Fast Ball Speed": 166, "Cursed Ball": 50, "Curve": 40, "Curve Control": 50, "Char Id": 19, "Slap Contact Spot Size": 35, "Charge Contact Spot Size": 20, "Slap Hit Power": 55, "Charge Hit Power": 75, "Bunting": 30, "Speed": 40, "Throwing Arm": 50, "Weight": 2, "Captain Star Hit/Pitch": 8, "Non Captain Star Pitch": 2, "Batting Stat Bar": 8, "Pitching Stat Bar": 5, "Running Stat Bar": 4, "Fielding Stat Bar": 3, "Name": "Bowser Jr", "Fielding Arm": 1, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 1, "Character Class": 1, "Can Be Captain": 1, "Non Captain Star Swing": 1, "Fielding Ability": 2}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 60, "Curve Control": 50, "Char Id": 20, "Slap Contact Spot Size": 55, "Charge Contact Spot Size": 30, "Slap Hit Power": 48, "Charge Hit Power": 35, "Bunting": 20, "Speed": 60, "Throwing Arm": 60, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 3, "Pitching Stat Bar": 3, "Running Stat Bar": 6, "Fielding Stat Bar": 4, "Name": "Paratroopa(R)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 64}, {"Curve Ball Speed": 125, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 30, "Curve Control": 50, "Char Id": 21, "Slap Contact Spot Size": 35, "Charge Contact Spot Size": 15, "Slap Hit Power": 51, "Charge Hit Power": 65, "Bunting": 20, "Speed": 20, "Throwing Arm": 80, "Weight": 3, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 6, "Pitching Stat Bar": 3, "Running Stat Bar": 2, "Fielding Stat Bar": 5, "Name": "Pianta(B)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 1, "Vertical Hit Trajectory": 2, "Character Class": 1, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 17}, {"Curve Ball Speed": 125, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 30, "Curve Control": 50, "Char Id": 22, "Slap Contact Spot Size": 35, "Charge Contact Spot Size": 15, "Slap Hit Power": 51, "Charge Hit Power": 70, "Bunting": 20, "Speed": 10, "Throwing Arm": 80, "Weight": 3, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 7, "Pitching Stat Bar": 3, "Running Stat Bar": 1, "Fielding Stat Bar": 5, "Name": "Pianta(R)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 1, "Vertical Hit Trajectory": 2, "Character Class": 1, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 17}, {"Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 50, "Curve": 40, "Curve Control": 50, "Char Id": 23, "Slap Contact Spot Size": 35, "Charge Contact Spot Size": 15, "Slap Hit Power": 51, "Charge Hit Power": 65, "Bunting": 20, "Speed": 10, "Throwing Arm": 80, "Weight": 3, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 6, "Pitching Stat Bar": 4, "Running Stat Bar": 1, "Fielding Stat Bar": 5, "Name": "Pianta(Y)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 1, "Vertical Hit Trajectory": 2, "Character Class": 1, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 17}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 24, "Slap Contact Spot Size": 40, "Charge Contact Spot Size": 15, "Slap Hit Power": 43, "Charge Hit Power": 30, "Bunting": 20, "Speed": 70, "Throwing Arm": 60, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 3, "Pitching Stat Bar": 3, "Running Stat Bar": 7, "Fielding Stat Bar": 4, "Name": "Noki(B)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 8}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 25, "Slap Contact Spot Size": 40, "Charge Contact Spot Size": 15, "Slap Hit Power": 45, "Charge Hit Power": 40, "Bunting": 20, "Speed": 60, "Throwing Arm": 60, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 4, "Pitching Stat Bar": 3, "Running Stat Bar": 6, "Fielding Stat Bar": 4, "Name": "Noki(R)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 8}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 60, "Curve Control": 50, "Char Id": 26, "Slap Contact Spot Size": 45, "Charge Contact Spot Size": 13, "Slap Hit Power": 43, "Charge Hit Power": 30, "Bunting": 25, "Speed": 60, "Throwing Arm": 60, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 3, "Pitching Stat Bar": 4, "Running Stat Bar": 6, "Fielding Stat Bar": 4, "Name": "Noki(G)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 8}, {
        "Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 50, "Curve": 40, "Curve Control": 50, "Char Id": 27, "Slap Contact Spot Size": 30, "Charge Contact Spot Size": 20, "Slap Hit Power": 10, "Charge Hit Power": 85, "Bunting": 15, "Speed": 30, "Throwing Arm": 60, "Weight": 3, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 8, "Pitching Stat Bar": 3, "Running Stat Bar": 3, "Fielding Stat Bar": 3, "Name": "Bro(H)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 1, "Vertical Hit Trajectory": 1, "Character Class": 1, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 1}, {"Curve Ball Speed": 120, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 28, "Slap Contact Spot Size": 85, "Charge Contact Spot Size": 40, "Slap Hit Power": 45, "Charge Hit Power": 40, "Bunting": 45, "Speed": 40, "Throwing Arm": 30, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 4, "Pitching Stat Bar": 4, "Running Stat Bar": 4, "Fielding Stat Bar": 6, "Name": "Toadsworth", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 1}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 29, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 40, "Charge Hit Power": 60, "Bunting": 25, "Speed": 70, "Throwing Arm": 50, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 4, "Pitching Stat Bar": 3, "Running Stat Bar": 7, "Fielding Stat Bar": 3, "Name": "Toad(B)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 0}, {"Curve Ball Speed": 120, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 55, "Curve Control": 50, "Char Id": 30, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 40, "Charge Hit Power": 60, "Bunting": 25, "Speed": 60, "Throwing Arm": 50, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 4, "Pitching Stat Bar": 4, "Running Stat Bar": 6, "Fielding Stat Bar": 3, "Name": "Toad(Y)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 0}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 31, "Slap Contact Spot Size": 55, "Charge Contact Spot Size": 35, "Slap Hit Power": 45, "Charge Hit Power": 65, "Bunting": 35, "Speed": 60, "Throwing Arm": 50, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 5, "Pitching Stat Bar": 3, "Running Stat Bar": 6, "Fielding Stat Bar": 3, "Name": "Toad(G)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 0}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 32, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 45, "Charge Hit Power": 70, "Bunting": 25, "Speed": 50, "Throwing Arm": 60, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 5, "Pitching Stat Bar": 3, "Running Stat Bar": 5, "Fielding Stat Bar": 4, "Name": "Toad(P)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 0}, {"Curve Ball Speed": 120, "Fast Ball Speed": 150, "Cursed Ball": 50, "Curve": 50, "Curve Control": 40, "Char Id": 33, "Slap Contact Spot Size": 65, "Charge Contact Spot Size": 35, "Slap Hit Power": 48, "Charge Hit Power": 40, "Bunting": 40, "Speed": 20, "Throwing Arm": 40, "Weight": 2, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 4, "Pitching Stat Bar": 2, "Running Stat Bar": 2, "Fielding Stat Bar": 8, "Name": "Magikoopa(B)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 2, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 128}, {"Curve Ball Speed": 120, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 40, "Char Id": 34, "Slap Contact Spot Size": 65, "Charge Contact Spot Size": 35, "Slap Hit Power": 50, "Charge Hit Power": 45, "Bunting": 40, "Speed": 10, "Throwing Arm": 40, "Weight": 2, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 5, "Pitching Stat Bar": 2, "Running Stat Bar": 1, "Fielding Stat Bar": 8, "Name": "Magikoopa(R)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 2, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 128}, {"Curve Ball Speed": 120, "Fast Ball Speed": 150, "Cursed Ball": 50, "Curve": 60, "Curve Control": 50, "Char Id": 35, "Slap Contact Spot Size": 65, "Charge Contact Spot Size": 35, "Slap Hit Power": 48, "Charge Hit Power": 40, "Bunting": 40, "Speed": 10, "Throwing Arm": 40, "Weight": 2, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 4, "Pitching Stat Bar": 3, "Running Stat Bar": 1, "Fielding Stat Bar": 8, "Name": "Magikoopa(G)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 2, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 128}, {"Curve Ball Speed": 120, "Fast Ball Speed": 150, "Cursed Ball": 50, "Curve": 70, "Curve Control": 50, "Char Id": 36, "Slap Contact Spot Size": 65, "Charge Contact Spot Size": 35, "Slap Hit Power": 40, "Charge Hit Power": 30, "Bunting": 40, "Speed": 10, "Throwing Arm": 40, "Weight": 2, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 3, "Pitching Stat Bar": 4, "Running Stat Bar": 1, "Fielding Stat Bar": 8, "Name": "Magikoopa(Y)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 2, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 128}, {"Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 50, "Curve": 60, "Curve Control": 50, "Char Id": 37, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 15, "Slap Hit Power": 55, "Charge Hit Power": 75, "Bunting": 20, "Speed": 30, "Throwing Arm": 70, "Weight": 4, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 7, "Pitching Stat Bar": 5, "Running Stat Bar": 3, "Fielding Stat Bar": 4, "Name": "King Boo", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 1, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 65}, {"Curve Ball Speed": 130, "Fast Ball Speed": 170, "Cursed Ball": 50, "Curve": 30, "Curve Control": 50, "Char Id": 38, "Slap Contact Spot Size": 30, "Charge Contact Spot Size": 10, "Slap Hit Power": 60, "Charge Hit Power": 95, "Bunting": 10, "Speed": 10, "Throwing Arm": 100, "Weight": 4, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 9, "Pitching Stat Bar": 4, "Running Stat Bar": 1, "Fielding Stat Bar": 3, "Name": "Petey", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 1, "Vertical Hit Trajectory": 1, "Character Class": 1, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 1}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 70, "Curve Control": 50, "Char Id": 39, "Slap Contact Spot Size": 60, "Charge Contact Spot Size": 25, "Slap Hit Power": 42, "Charge Hit Power": 25, "Bunting": 30, "Speed": 60, "Throwing Arm": 70, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 2, "Pitching Stat Bar": 5, "Running Stat Bar": 6, "Fielding Stat Bar": 6, "Name": "Dixie", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 2, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 4}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 40, "Slap Contact Spot Size": 40, "Charge Contact Spot Size": 15, "Slap Hit Power": 45, "Charge Hit Power": 40, "Bunting": 80, "Speed": 50, "Throwing Arm": 30, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 4, "Pitching Stat Bar": 3, "Running Stat Bar": 5, "Fielding Stat Bar": 4, "Name": "Goomba", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 0}, {"Curve Ball Speed": 115, "Fast Ball Speed": 154, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 41, "Slap Contact Spot Size": 30, "Charge Contact Spot Size": 15, "Slap Hit Power": 45, "Charge Hit Power": 30, "Bunting": 80, "Speed": 70, "Throwing Arm": 60, "Weight": 0, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 3, "Pitching Stat Bar": 2, "Running Stat Bar": 7, "Fielding Stat Bar": 5, "Name": "Paragoomba", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 2, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 64}, {"Curve Ball Speed": 120, "Fast Ball Speed": 165, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 42, "Slap Contact Spot Size": 70, "Charge Contact Spot Size": 30, "Slap Hit Power": 40, "Charge Hit Power": 60, "Bunting": 30, "Speed": 30, "Throwing Arm": 50, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 6, "Pitching Stat Bar": 4, "Running Stat Bar": 3, "Fielding Stat Bar": 5, "Name": "Koopa(G)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 8}, {"Curve Ball Speed": 115, "Fast Ball Speed": 155, "Cursed Ball": 50, "Curve": 60, "Curve Control": 50, "Char Id": 43, "Slap Contact Spot Size": 60, "Charge Contact Spot Size": 35, "Slap Hit Power": 40, "Charge Hit Power": 30, "Bunting": 20, "Speed": 60, "Throwing Arm": 60, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 2, "Pitching Stat Bar": 3, "Running Stat Bar": 6, "Fielding Stat Bar": 4, "Name": "Paratroopa(G)", "Fielding Arm": 0, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 2, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 64}, {"Curve Ball Speed": 120, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 44, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 42, "Charge Hit Power": 50, "Bunting": 25, "Speed": 50, "Throwing Arm": 40, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 4, "Pitching Stat Bar": 3, "Running Stat Bar": 5, "Fielding Stat Bar": 5, "Name": "Shy Guy(B)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 8}, {"Curve Ball Speed": 130, "Fast Ball Speed": 165, "Cursed Ball": 50, "Curve": 55, "Curve Control": 50, "Char Id": 45, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 42, "Charge Hit Power": 50, "Bunting": 25, "Speed": 40, "Throwing Arm": 40, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 4, "Pitching Stat Bar": 4, "Running Stat Bar": 4, "Fielding Stat Bar": 5, "Name": "Shy Guy(Y)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 8}, {"Curve Ball Speed": 125, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 60, "Curve Control": 60, "Char Id": 46, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 42, "Charge Hit Power": 50, "Bunting": 25, "Speed": 40, "Throwing Arm": 40, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 4, "Pitching Stat Bar": 4, "Running Stat Bar": 4, "Fielding Stat Bar": 5, "Name": "Shy Guy(G)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 8}, {"Curve Ball Speed": 120, "Fast Ball Speed": 160, "Cursed Ball": 50, "Curve": 50, "Curve Control": 50, "Char Id": 47, "Slap Contact Spot Size": 50, "Charge Contact Spot Size": 30, "Slap Hit Power": 42, "Charge Hit Power": 50, "Bunting": 25, "Speed": 40, "Throwing Arm": 50, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 4, "Pitching Stat Bar": 4, "Running Stat Bar": 4, "Fielding Stat Bar": 6, "Name": "Shy Guy(Bk)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 0, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 8}, {"Curve Ball Speed": 120, "Fast Ball Speed": 150, "Cursed Ball": 90, "Curve": 50, "Curve Control": 50, "Char Id": 48, "Slap Contact Spot Size": 65, "Charge Contact Spot Size": 25, "Slap Hit Power": 40, "Charge Hit Power": 55, "Bunting": 30, "Speed": 40, "Throwing Arm": 50, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 5, "Pitching Stat Bar": 4, "Running Stat Bar": 4, "Fielding Stat Bar": 3, "Name": "Dry Bones(Gy)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 9}, {"Curve Ball Speed": 120, "Fast Ball Speed": 150, "Cursed Ball": 90, "Curve": 50, "Curve Control": 50, "Char Id": 49, "Slap Contact Spot Size": 70, "Charge Contact Spot Size": 25, "Slap Hit Power": 40, "Charge Hit Power": 55, "Bunting": 30, "Speed": 30, "Throwing Arm": 50, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 6, "Pitching Stat Bar": 4, "Running Stat Bar": 3, "Fielding Stat Bar": 3, "Name": "Dry Bones(G)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 9}, {"Curve Ball Speed": 125, "Fast Ball Speed": 155, "Cursed Ball": 90, "Curve": 50, "Curve Control": 50, "Char Id": 50, "Slap Contact Spot Size": 65, "Charge Contact Spot Size": 25, "Slap Hit Power": 44, "Charge Hit Power": 60, "Bunting": 30, "Speed": 30, "Throwing Arm": 50, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 6, "Pitching Stat Bar": 4, "Running Stat Bar": 3, "Fielding Stat Bar": 3, "Name": "Dry Bones(R)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 1, "Fielding Ability": 9}, {"Curve Ball Speed": 120, "Fast Ball Speed": 150, "Cursed Ball": 90, "Curve": 50, "Curve Control": 50, "Char Id": 51, "Slap Contact Spot Size": 65, "Charge Contact Spot Size": 25, "Slap Hit Power": 40, "Charge Hit Power": 55, "Bunting": 30, "Speed": 30, "Throwing Arm": 60, "Weight": 1, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 3, "Batting Stat Bar": 5, "Pitching Stat Bar": 4, "Running Stat Bar": 3, "Fielding Stat Bar": 4, "Name": "Dry Bones(B)", "Fielding Arm": 1, "Batting Stance": 1, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 3, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 9}, {"Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 50, "Curve": 40, "Curve Control": 50, "Char Id": 52, "Slap Contact Spot Size": 30, "Charge Contact Spot Size": 20, "Slap Hit Power": 5, "Charge Hit Power": 90, "Bunting": 15, "Speed": 20, "Throwing Arm": 60, "Weight": 3, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 2, "Batting Stat Bar": 8, "Pitching Stat Bar": 3, "Running Stat Bar": 2, "Fielding Stat Bar": 3, "Name": "Bro(F)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 1, "Vertical Hit Trajectory": 2, "Character Class": 1, "Can Be Captain": 0, "Non Captain Star Swing": 2, "Fielding Ability": 1}, {"Curve Ball Speed": 125, "Fast Ball Speed": 165, "Cursed Ball": 50, "Curve": 40, "Curve Control": 50, "Char Id": 53, "Slap Contact Spot Size": 30, "Charge Contact Spot Size": 20, "Slap Hit Power": 20, "Charge Hit Power": 80, "Bunting": 15, "Speed": 30, "Throwing Arm": 60, "Weight": 3, "Captain Star Hit/Pitch": 0, "Non Captain Star Pitch": 1, "Batting Stat Bar": 8, "Pitching Stat Bar": 3, "Running Stat Bar": 3, "Fielding Stat Bar": 3, "Name": "Bro(B)", "Fielding Arm": 0, "Batting Stance": 0, "Horizontal Hit Trajectory": 0, "Vertical Hit Trajectory": 0, "Character Class": 1, "Can Be Captain": 0, "Non Captain Star Swing": 3, "Fielding Ability": 1}]

BATTER_HITBOXES = [{'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0999999046325684, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': 0.30000001192092896, 'VerticalRangeBack': 1.899999976158142, 'EasyBattingSpotHorizontal': -1.7999999523162842, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': 0.4000000059604645, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.6500000953674316, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 1.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.30000001192092896, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.75, 'HorizontalRangeFar': 0.5, 'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.2999999523162842, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6000000238418579, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.2999999523162842, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': 0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.049999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.75, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7000000476837158, 'EasyBattingSpotHorizontal': -1.7999999523162842, 'EasyBattingSpotVertical': -1.2999999523162842, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.149999976158142, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 1.4500000476837158, 'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 0.20000000298023224, 'EasyBattingSpotHorizontal': -3.5999999046325684, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.75, 'VerticalRangeFront': 0.4000000059604645, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.4000000953674316, 'EasyBattingSpotVertical': -1.600000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.8500000238418579, 'VerticalRangeFront': 0.30000001192092896, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.5, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.1500000953674316, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.949999988079071, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.44999998807907104, 'HorizontalRangeFar': 0.8500000238418579, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.4000000953674316, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.100000023841858, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.5, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7000000476837158, 'EasyBattingSpotHorizontal': -1.7999999523162842, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.8500000238418579, 'VerticalRangeFront': 0.30000001192092896, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': 0.20000000298023224, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.200000047683716, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.44999998807907104, 'HorizontalRangeFar': 0.8500000238418579, 'VerticalRangeFront': 0.5, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.44999998807907104, 'HorizontalRangeFar': 0.8500000238418579, 'VerticalRangeFront': 0.5, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.44999998807907104, 'HorizontalRangeFar': 0.8500000238418579, 'VerticalRangeFront': 0.5, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.2000000476837158, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.2000000476837158, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.2000000476837158, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0},
                {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 1.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -1.75, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 1.0}, {'HorizontalRangeNear': -0.44999998807907104, 'HorizontalRangeFar': 0.44999998807907104, 'VerticalRangeFront': -0.6000000238418579, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.44999998807907104, 'HorizontalRangeFar': 0.44999998807907104, 'VerticalRangeFront': -0.6000000238418579, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.44999998807907104, 'HorizontalRangeFar': 0.44999998807907104, 'VerticalRangeFront': -0.6000000238418579, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.44999998807907104, 'HorizontalRangeFar': 0.44999998807907104, 'VerticalRangeFront': -0.6000000238418579, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6000000238418579, 'HorizontalRangeFar': 0.699999988079071, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6000000238418579, 'HorizontalRangeFar': 0.699999988079071, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6000000238418579, 'HorizontalRangeFar': 0.699999988079071, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6000000238418579, 'HorizontalRangeFar': 0.699999988079071, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.2000000476837158, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.399999976158142, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.100000023841858, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': 0.20000000298023224, 'VerticalRangeBack': 1.7000000476837158, 'EasyBattingSpotHorizontal': -1.600000023841858, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.2000000476837158, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': 0.0, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0999999046325684, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.5, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.1500000953674316, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.0999999046325684, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.550000011920929, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.75, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.100000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.75, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.100000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.75, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.100000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.75, 'HorizontalRangeFar': 0.550000011920929, 'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.100000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 1.0}, {'HorizontalRangeNear': -0.6499999761581421, 'HorizontalRangeFar': 0.6499999761581421, 'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 1.0}]

BALL_CONTACT_ARRAY_807B6294 = [[[[50, 98, 106, 150, 30, 95, 109, 170], [40, 98, 106, 160, 20, 95, 109, 180]], [[60, 99, 101, 150, 40, 97, 103, 170], [55, 99, 101, 160, 35, 97, 103, 180]], [[50, 99, 101, 140, 40, 97, 103, 160], [45, 99, 101, 145, 35, 97, 103, 165]], [[80, 98, 102, 120, 35, 95, 105, 165], [80, 98, 102, 110, 35, 95, 105, 165]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]], [
    [[40, 96, 104, 150, 30, 93, 107, 170], [30, 96, 104, 170, 20, 93, 107, 180]], [[60, 96, 104, 140, 35, 93, 107, 170], [50, 96, 104, 150, 25, 93, 107, 180]], [[60, 99, 101, 140, 40, 97, 103, 160], [40, 99, 101, 160, 30, 97, 103, 170]], [[90, 98, 102, 110, 75, 95, 105, 125], [90, 98, 102, 110, 75, 95, 105, 125]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]]]

UINT_ARRAY_ARRAY_807B7134 = [[100, 100, 0x00111110, 0x00111110, 0], [100, 100, 0x00111110, 0x00111110, 2], [101, 102, 0x00111110, 0x00111110, 1], [90, 90, 0x00111110, 0x00111110, 0], [94, 95, 0x00111110, 0x00111110, 0], [102, 103, 0x00111110, 0x00111110, 1], [90, 90, 0x00111110, 0x01100000, 0], [85, 90, 0x00111110, 0x00111110, 0], [102, 103, 0x00111110, 0x00111110, 1], [
    100, 100, 0x00111110, 0x00111110, 0], [95, 100, 0x00111110, 0x00111110, 2], [104, 105, 0x00111110, 0x00111110, 1], [60, 60, 0x00111110, 0x00111110, 0], [70, 75, 0x00111110, 0x00111110, 0], [87, 90, 0x00111110, 0x00111110, 1], [70, 70, 0x00111110, 0x00111110, 0], [80, 85, 0x00111110, 0x00111110, 0], [105, 110, 0x00111110, 0x00111110, 1], [50, 50, 0x00110110, 0x00110110, 0]]

CONTACT_PERFECT_THRESHOLDS = [[99.1, 100.9, 100.5],
                            [99.7, 100.3, 1.1], [99.7, 100.3, 1.0]]

CONTACT_CHEM_LINK_MULTIPLIERS = [1.0, 1.05, 1.1, 1.2]

BATTING_ANGLE_RANGES = [[[[0, 0], [0, 0], [-700, -500], [-500, -350], [-400, -250], [-350, -100], [-150, 250], [200, 300], [250, 400], [350, 550], [550, 700], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [-600, -400], [-400, -200], [-300, -100], [-200, 200], [100, 400], [300, 450], [350, 600], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]], [[[0, 0], [0, 0], [-750, -500], [-500, -300], [-300, -150], [-150, 200], [200, 400], [300, 450], [400, 600], [500, 600], [600, 700], [0, 0], [0, 0],
                                                                                                                                                                                                                                                                                                                                                            [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [-600, -400], [-400, -200], [-300, 100], [100, 400], [100, 400], [200, 500], [500, 700], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]], [[[0, 0], [0, 0], [-700, -600], [-600, -400], [-450, -350], [-400, -300], [-350, -200], [-200, 150], [150, 300], [300, 700], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [-550, -300], [-400, -200], [-300, -100], [-300, -100], [-100, 200], [200, 450], [450, 650], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]]

BATTING_VERTICAL_ANGLE_WEIGHTS = [[[[[0, 10, 20, 30, 40], [20, 20, 20, 20, 20], [10, 25, 30, 25, 10], [20, 20, 20, 20, 20], [40, 30, 20, 10, 0]], [[0, 10, 20, 30, 40], [20, 20, 20, 20, 20], [10, 25, 30, 25, 10], [20, 20, 20, 20, 20], [40, 30, 20, 10, 0]]], [[[10, 0, 20, 30, 40], [20, 22, 22, 28, 8], [20, 25, 25, 25, 5], [20, 22, 22, 28, 8], [10, 0, 20, 30, 40]], [[10, 0, 20, 30, 40], [20, 22, 22, 28, 8], [20, 25, 25, 25, 5], [20, 22, 22, 28, 8], [10, 0, 20, 30, 40]]]], [[[[0, 10, 20, 30, 40], [5, 5, 15, 40, 35], [5, 5, 20, 40, 35], [5, 5, 15, 40, 35], [40, 30, 20, 10, 0]], [[0, 10, 20, 30, 40], [5, 5, 15, 40, 35], [5, 5, 20, 40, 35], [5, 5, 15, 40, 35], [
    40, 30, 20, 10, 0]]], [[[5, 0, 10, 40, 45], [5, 21, 12, 29, 33], [5, 23, 15, 27, 30], [5, 21, 12, 29, 33], [5, 0, 10, 40, 45]], [[5, 0, 10, 40, 45], [5, 21, 12, 29, 33], [5, 23, 15, 27, 30], [5, 21, 12, 29, 33], [5, 0, 10, 40, 45]]]], [[[[10, 20, 20, 20, 30], [35, 40, 15, 5, 5], [30, 40, 20, 5, 5], [35, 40, 15, 5, 5], [40, 30, 20, 5, 5]], [[10, 20, 20, 20, 30], [35, 40, 15, 5, 5], [30, 40, 20, 5, 5], [35, 40, 15, 5, 5], [40, 30, 20, 5, 5]]], [[[10, 0, 20, 30, 40], [35, 30, 22, 10, 3], [30, 30, 25, 15, 0], [35, 30, 22, 10, 3], [10, 0, 20, 30, 40]], [[10, 0, 20, 30, 40], [35, 30, 22, 10, 3], [30, 30, 25, 15, 0], [35, 30, 22, 10, 3], [10, 0, 20, 30, 40]]]]]

SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC = [[[[-50, 50], [50, 100], [100, 300], [300, 400], [400, 500]], [[50, 150], [150, 200], [200, 250], [250, 300], [300, 350]], [[50, 150], [150, 200], [150, 200], [200, 300], [300, 350]], [[50, 150], [150, 200], [200, 250], [250, 300], [300, 350]], [[-50, 50], [50, 100], [100, 300], [300, 400], [
    400, 500]]], [[[400, 450], [450, 500], [500, 550], [550, 600], [550, 600]], [[50, 100], [100, 150], [300, 400], [350, 450], [400, 500]], [[100, 200], [350, 400], [450, 500], [500, 550], [530, 580]], [[50, 100], [100, 150], [300, 400], [350, 450], [400, 500]], [[400, 450], [450, 500], [500, 550], [550, 600], [550, 600]]]]

BALL_HIT_ARRAY = [[[100, 130, -110], [140, 145, -100], [145, 150, -110], [140, 145, -100], [100, 130, -110]], [[140, 150, -120], [162, 177, -160], [160, 170, 0], [162, 177, -160], [140, 150, -120]], [[120, 130, -200], [140, 150, -200], [160, 170, -200], [140, 150, -200], [120, 130, -200]],
                [[150, 160, -300], [170, 190, -300], [190, 200, -300], [170, 190, -300], [150, 160, -300]], [[130, 140, -200], [145, 155, -300], [160, 170, -300], [145, 155, -300], [130, 140, -200]], [[140, 150, -150], [190, 200, -200], [200, 210, -180], [190, 200, -200], [140, 150, -150]]]

STAR_SWING_EXIT_VELOCITY_ARRAY = [[[150, 160, -150], [160, 170, -150], [170, 180, -100], [160, 170, -150], [150, 160, -150]], [[150, 160, -250], [160, 170, -250], [
    170, 180, -250], [160, 170, -250], [150, 160, -250]], [[170, 180, -300], [170, 180, -300], [190, 200, -300], [170, 180, -300], [170, 180, -300]]]

CURSED_BALL_DEBUFF_ARRAY = [[1.0, 1.0], [1.0, 0.8], [1.0, 0.5]]

FIELD_TRAJECTORY_BONUSES = [[1.0, 1.0, 1.0, 1.0, 1.0], [
    0.85, 0.95, 1.0, 1.05, 1.02], [1.02, 1.05, 1.0, 0.95, 0.85]]

NON_CAPTAIN_STAR_VERTICAL_ANGLES = [[[250, 300], [300, 350], [350, 400], [400, 450], [450, 500]], [
    [50, 100], [50, 100], [50, 100], [50, 100], [50, 100]], [[120, 160], [160, 200], [160, 200], [160, 200], [120, 160]]]

CAPTAIN_STAR_VERTICAL_ANGLES = [[[59, 61], [59, 61], [59, 61], [59, 61], [59, 61]], [[-101, -99], [-101, -99], [-101, -99], [-101, -99], [-101, -99]], [[350, 400], [350, 400], [350, 400], [350, 400], [350, 400]], [[450, 500], [450, 500], [450, 500], [450, 500], [450, 500]], [[120, 160], [160, 200], [160, 200], [160, 200], [120, 160]], [[250, 300], [250, 300], [
    250, 300], [250, 300], [250, 300]], [[64, 80], [64, 80], [64, 80], [64, 80], [64, 80]], [[64, 80], [64, 80], [64, 80], [64, 80], [64, 80]], [[350, 400], [350, 400], [350, 400], [350, 400], [350, 400]], [[200, 250], [200, 250], [200, 250], [200, 250], [200, 250]], [[350, 600], [350, 600], [350, 600], [350, 600], [350, 600]], [[350, 600], [350, 600], [350, 600], [350, 600], [350, 600]]]

SHORT_ARRAY_ARRAY_807B6AF4 = [[0, 0], [500, 550], [500, 550]]

CAPTAIN_STAR_SWING_EXIT_VELOCITY_ARRAY = [[[140, 150, 0], [150, 160, 150], [160, 170, 150], [150, 160, 150], [140, 150, 0]], [[120, 130, 0], [130, 150, 50], [160, 170, 100], [130, 150, 50], [120, 130, 0]], [[90, 100, 80], [100, 110, 80], [110, 120, 80], [100, 110, 80], [90, 100, 80]], [[60, 70, 80], [70, 80, 80], [70, 80, 80], [70, 80, 80], [60, 70, 80]], [[170, 180, -120], [170, 180, -130], [190, 200, -125], [170, 180, -135], [170, 180, -125]], [[150, 160, -140], [150, 160, -150], [160, 170, -150], [150, 160, -150], [150, 160, -140]], [
    [170, 180, 0], [170, 180, 0], [190, 200, 0], [170, 180, 0], [170, 180, 0]], [[160, 170, 0], [160, 170, 0], [180, 190, 0], [160, 170, 0], [160, 170, 0]], [[90, 130, -650], [90, 130, -650], [90, 130, -650], [90, 130, -650], [90, 130, -650]], [[140, 160, -400], [140, 160, -400], [140, 160, -400], [140, 160, -400], [140, 160, -400]], [[130, 140, -100], [140, 150, -100], [150, 160, -100], [140, 150, -100], [130, 140, -100]], [[130, 140, -100], [140, 150, -100], [150, 160, -100], [140, 150, -100], [130, 140, -100]]]

POWER_CHEM_LINK_MULTIPLIERS = [1.0, 1.1, 1.25, 1.5]

BATTING_REACHES = [[-0.85, 0.15], [-0.35, 0.35]]

FLOAT_ARRAY_ARRAY_807B72BC = [[0.5, 0.001, 0.003], [0.25, 0.006, 0.008]]

BUNT_ANGLE_CALC_ARRAY = [[256, 960, 256, 960], [480, 640, 480, 640], [512, 576, 512, 576], [480, 640, 480, 640], [256, 960, 256, 960]]

BUNTING_POWER_ARRAY = [[20, 50], [45, 60], [30, 45], [45, 60], [20, 50]]

BUNTING_CONTACT_ARRAY = [[[-256, 960],[-256, 960],[-256, 960],[-256, 960]], [[-96, 64],[-96, 96],[-96, 64],[-96, 96]], [[-64, 32],[-64, 32],[-64, 32],[-64, 32]], [[-96, 64],[-96, 96],[-96, 64],[-96, 96]], [[-256, 960],[-256, 960],[-256, 960],[-256, 960]]]

MOONSHOT_MULTIPLIER = 1.5

CHARACTER_INDICES = [[0, 0, 0, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 2, 2, 1, 1, 0], [0, 3, 3, 1, 1, 0], [0, 4, 4, 1, 1, 0], [0, 5, 5, 1, 1, 0], [0, 6, 6, 1, 1, 0], [0, 7, 7, 1, 0, 0], [0, 8, 8, 1, 0, 0], [0, 9, 9, 1, 1, 0], [0, 10, 10, 1, 1, 0], [0, 11, 11, 1, 1, 0], [1, 12, 12, 1, 0, 0], [2, 13, 13, 1, 0, 0], [0, 14, 14, 1, 0, 0], [0, 15, 15, 1, 0, 0], [3, 16, 16, 1, 0, 0], [0, 17, 17, 1, 1, 0], [0, 18, 18, 1, 0, 0], [0, 19, 19, 1, 1, 0], [4, 20, 20, 1, 0, 0], [5, 21, 21, 1, 0, 0], [5, 21, 21, 0, 0, 1], [5, 21, 21, 0, 0, 2], [6, 24, 22, 1, 0, 0], [6, 24, 22, 0, 0, 1], [6, 24, 22, 0, 0, 2], [7, 27, 23, 1, 0, 0], [0, 28, 24, 1, 0, 0], [2, 13, 13, 0, 0, 1], [2, 13, 13, 0, 0, 2], [2, 13, 13, 0, 0, 3], [2, 13, 13, 0, 0, 4], [8, 33, 25, 1, 0, 0], [8, 33, 25, 0, 0, 1], [8, 33, 25, 0, 0, 2], [8, 33, 25, 0, 0, 3], [0, 37, 26, 1, 0, 0], [0, 38, 27, 1, 0, 0], [0, 39, 28, 1, 0, 0], [0, 40, 29, 1, 0, 0], [0, 41, 30, 1, 0, 0], [1, 12, 12, 0, 0, 1], [4, 20, 20, 0, 0, 1], [3, 16, 16, 0, 0, 1], [3, 16, 16, 0, 0, 2], [3, 16, 16, 0, 0, 3], [3, 16, 16, 0, 0, 4], [9, 48, 31, 1, 0, 0], [9, 48, 31, 0, 0, 1], [9, 48, 31, 0, 0, 2], [9, 48, 31, 0, 0, 3], [7, 27, 23, 0, 0, 1], [7, 27, 23, 0, 0, 2]]

HBP_ARRAY = [[80, 70, 10], [30, 40, 20], [100, 80, 40], [30, 50, 50], [50, 30, 30], [40, 40, 10], [60, 40, 30], [90, 30, 50], [60, 40, 30], [180, 120, 120], [130, 80, 30], [50, 50, 10], [50, 50, 30], [100, 50, 0], [100, 60, 30], [90, 50, 0], [70, 100, 30], [60, 20, 40], [80, 120, 30], [90, 50, 30], [80, 60, 30], [110, 70, 60], [80, 70, 30], [100, 30, 50], [80, 50, 0], [50, 40, 40], [130, 80, 50], [120, 80, 30], [20, 40, 30], [100, 90, 10], [100, 90, 30], [60, 60, 20]]

FIELDER_HITBOXES = [{'AirRadius': 117, 'GroundRadius': 80, 'Hitbox3': 75, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 335, 'DiveRange': 140, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 75, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 140, 'Hitbox9': 100}, {'AirRadius': 250, 'GroundRadius': 80, 'Hitbox3': 100, 'Height': 250, 'field4_0x8': 95, 'Hitbox7': 580, 'DiveRange': 300, 'Hitbox9': 250}, {'AirRadius': 140, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 150, 'field4_0x8': 75, 'Hitbox7': 410, 'DiveRange': 170, 'Hitbox9': 100}, {'AirRadius': 77, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 242, 'field4_0x8': 161, 'Hitbox7': 572, 'DiveRange': 140, 'Hitbox9': 100}, {'AirRadius': 77, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 242, 'field4_0x8': 161, 'Hitbox7': 572, 'DiveRange': 140, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 450, 'Hitbox9': 100}, {'AirRadius': 72, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 130, 'field4_0x8': 50, 'Hitbox7': 297, 'DiveRange': 110, 'Hitbox9': 100}, {'AirRadius': 72, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 130, 'field4_0x8': 50, 'Hitbox7': 297, 'DiveRange': 110, 'Hitbox9': 100}, {'AirRadius': 196, 'GroundRadius': 80, 'Hitbox3': 100, 'Height': 269, 'field4_0x8': 180, 'Hitbox7': 633, 'DiveRange': 230, 'Hitbox9': 220}, {'AirRadius': 140, 'GroundRadius': 80, 'Hitbox3': 75, 'Height': 200, 'field4_0x8': 100, 'Hitbox7': 420, 'DiveRange': 200, 'Hitbox9': 80}, {'AirRadius': 230, 'GroundRadius': 80, 'Hitbox3': 100, 'Height': 320, 'field4_0x8': 180, 'Hitbox7': 780, 'DiveRange': 200, 'Hitbox9': 150}, {'AirRadius': 84, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 155, 'field4_0x8': 75, 'Hitbox7': 270, 'DiveRange': 120, 'Hitbox9': 130}, {'AirRadius': 70, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 130, 'field4_0x8': 42, 'Hitbox7': 228, 'DiveRange': 90, 'Hitbox9': 50}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 100, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 80, 'Hitbox9': 70}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 350, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 100, 'Hitbox9': 120}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 75, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 150, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 120, 'Hitbox9': 90}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 100, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 220, 'Hitbox9': 80}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 100, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 220, 'Hitbox9': 80}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 100, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 220, 'Hitbox9': 80}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 130, 'Hitbox9': 80}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 130, 'Hitbox9': 80}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 130, 'Hitbox9': 80}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 150, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 80, 'Hitbox9': 40}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 50}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 50}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 50}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 50}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 75, 'Height': 300, 'field4_0x8': 80, 'Hitbox7': 400, 'DiveRange': 230, 'Hitbox9': 30}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 75, 'Height': 300, 'field4_0x8': 80, 'Hitbox7': 400, 'DiveRange': 230, 'Hitbox9': 30}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 75, 'Height': 300, 'field4_0x8': 80, 'Hitbox7': 400, 'DiveRange': 230, 'Hitbox9': 30}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 75, 'Height': 300, 'field4_0x8': 80, 'Hitbox7': 400, 'DiveRange': 230, 'Hitbox9': 30}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 100, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 100, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 230, 'Hitbox9': 150}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 140, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 110, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 120, 'Hitbox9': 90}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 120, 'Hitbox9': 130}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 120, 'Hitbox9': 90}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 90, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 120, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 120, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 120, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 120, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 150, 'Hitbox9': 100}, {'AirRadius': 120, 'GroundRadius': 80, 'Hitbox3': 50, 'Height': 185, 'field4_0x8': 80, 'Hitbox7': 350, 'DiveRange': 150, 'Hitbox9': 100}]

FIELDER_HITBOX_SCALARS = [[1.1799999475479126, 1.100000023841858], [1.1799999475479126, 1.100000023841858], [1.1100000143051147, 1.0], [1.1799999475479126, 1.149999976158142], [1.1799999475479126, 1.0800000429153442], [1.1799999475479126, 1.100000023841858], [1.1799999475479126, 1.100000023841858], [1.2000000476837158, 1.100000023841858], [1.2000000476837158, 1.1799999475479126], [1.0, 0.800000011920929], [1.1799999475479126, 1.059999942779541], [1.0, 0.800000011920929], [1.1799999475479126, 1.100000023841858], [1.399999976158142, 1.3200000524520874], [1.2000000476837158, 1.1200000047683716], [1.399999976158142, 1.3200000524520874], [1.2000000476837158, 1.1200000047683716], [1.1799999475479126, 1.100000023841858], [1.0, 0.9200000166893005], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.0800000429153442], [1.2000000476837158, 1.0800000429153442], [1.2000000476837158, 1.0800000429153442], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.399999976158142, 1.3200000524520874], [1.399999976158142, 1.3200000524520874], [1.399999976158142, 1.3200000524520874], [1.399999976158142, 1.3200000524520874], [1.399999976158142, 1.3200000524520874], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.100000023841858, 0.699999988079071], [1.1799999475479126, 1.149999976158142], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.1799999475479126, 1.100000023841858], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716], [1.2000000476837158, 1.1200000047683716]]

LEFT_SOUR = 0
LEFT_NICE = 1
PERFECT = 2
RIGHT_NICE = 3
RIGHT_SOUR = 4

RIGHTY = 0
LEFTY = 1

SLAP = 0
CHARGE = 1
STAR = 2
BUNT = 3

SOUR_CURVE_SLAP = 0x0
NICE_CURVE_SLAP = 0x1
PERFECT_CURVE_SLAP = 0x2

SOUR_CURVE_CHARGE = 0x3
NICE_CURVE_CHARGE = 0x4
PERFECT_CURVE_CHARGE = 0x5

SOUR_CHANGEUP_SLAP = 0x6
NICE_CHANGEUP_SLAP = 0x7
PERFECT_CHANGEUP_SLAP = 0x8

SOUR_CHANGEUP_CHARGE = 0x9
NICE_CHANGEUP_CHARGE = 0xa
PERFECT_CHANGEUP_CHARGE = 0xb

SOUR_PERFECTPITCH_SLAP = 0xc
NICE_PERFECTPITCH_SLAP = 0xd
PERFECT_PERFECTPITCH_SLAP = 0xe

SOUR_PERFECTPITCH_CHARGE = 0xf
NICE_PERFECTPITCH_CHARGE = 0x10
PERFECT_PERFECTPITCH_CHARGE = 0x11

PITCHCURVE = 0
PITCHCHARGE = 1
PITCHCHANGEUP = 2

PITCHCHARGETYPE_NONE = 0
PITCHCHARGETYPE_UNKNOWN = 1
PITCHCHARGETYPE_CHARGE = 2
PITCHCHARGETYPE_PERFECT = 3

PUSHPULL_NONE = 0
PUSHPULL_PULL = 1
PUSHPULL_PUSH = 2
class BattingCalculator:
    StaticRandomInt1 = 7769  # <= 32767
    StaticRandomInt2 = 5359  # <= 32767
    USHORT_8089269c = 1828  # <= 32767
    inMemBatter = {}
    inMemPitcher = {}
    inMemBall = {}
    readValues = {}
    Hit_HorizontalAngle = 0
    Hit_VerticalAngle = 0
    Hit_HorizontalPower = 0
    AddedContactGravity = 0
    Display_Output = {}


    def floor(f):
        return math.trunc(f)


    def LinearInterpolateToNewRange(value, prevMin, prevMax, nextMin, nextMax):
        min = 0.0
        max = 0.0
        if (min == (prevMax - prevMin)):
            max = 1.0
        else:
            max = 1.0
            calcedValue = (value - prevMin) / (prevMax - prevMin)

            if ((calcedValue <= max)):
                max = calcedValue
                if (calcedValue < min):
                    max = min
        return (nextMax - nextMin) * max + nextMin

    def calculateContact(self):
        chargeUp = self.inMemBatter["BatterAtPlate_BatterCharge_Up"]
        contactSize = self.inMemBatter["Batter_SlapContactSize"]
        if (self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] != 0):
            # if there was a star swing, make contact size 100
            chargeUp = 0.0
            contactSize = 100.0

        if (self.inMemBatter["Batter_IsBunting"] == False):
            if (chargeUp <= 0.0):
                # If not charging
                if (self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"] != 0):
                    # If there are chem links on base, make the contact size larger
                    contactSize *= CONTACT_CHEM_LINK_MULTIPLIERS[self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"]]

            else:
                # else there is a charge
                contactSize = self.inMemBatter["Batter_ChargeContactSize"]

        else:
            # else bunting, use bunting contact size
            contactSize = self.inMemBatter["Batter_Bunting"]

        diffInX = self.inMemBatter["interstitialBallContact_X"] - self.inMemBatter["posX"]
        if (self.inMemBatter["AtBat_BatterHand"] == LEFTY):
            diffInX = -diffInX

        if (diffInX >= 0.0):
            self.inMemBatter["CalculatedBallPos"] = 100.0 * \
                (diffInX /
                BATTER_HITBOXES[self.inMemBatter["Batter_CharID"]]["HorizontalRangeFar"]) + 100.0

        else:
            self.inMemBatter["CalculatedBallPos"] = - \
                (100.0 * (diffInX /
                        BATTER_HITBOXES[self.inMemBatter["Batter_CharID"]]["HorizontalRangeNear"]) - 100.0)

        if (self.inMemBatter["CalculatedBallPos"] < 0.0):
            self.inMemBatter["CalculatedBallPos"] = 0.0

        if (200.0 < self.inMemBatter["CalculatedBallPos"]):
            self.inMemBatter["CalculatedBallPos"] = 200.0

        # Higher is better, makes ranges larger
        contactSize = contactSize / 100.0
        # Contact sizes are only based on slap/charge and trimming, and AI
        big_Array = BALL_CONTACT_ARRAY_807B6294[self.inMemBatter["AtBat_TrimmedBat"]][
            self.inMemBatter["Batter_Contact_SlapChargeBuntStar"]][self.inMemBatter["EasyBatting"]]
        b0 = big_Array[0]
        b1 = big_Array[1]
        b2 = big_Array[2]
        b3 = big_Array[3]

        self.inMemBatter["LeftNiceThreshold"] = contactSize * (big_Array[4] - b0) + b0
        self.inMemBatter["LeftPerfectThreshold"] = contactSize * (big_Array[5] - b1) + b1
        self.inMemBatter["RightPerfectThreshold"] = contactSize * (big_Array[6] - b2) + b2
        self.inMemBatter["RightNiceThreshold"] = contactSize * (big_Array[7] - b3) + b3

        

        self.inMemBatter["Batter_ContactType"] = LEFT_SOUR
        if (self.inMemBatter["LeftNiceThreshold"] <= self.inMemBatter["CalculatedBallPos"]):
            self.inMemBatter["Batter_ContactType"] = LEFT_NICE

            if (self.inMemBatter["LeftPerfectThreshold"] <= self.inMemBatter["CalculatedBallPos"]):
                self.inMemBatter["Batter_ContactType"] = PERFECT

                if (self.inMemBatter["RightPerfectThreshold"] <= self.inMemBatter["CalculatedBallPos"]):
                    self.inMemBatter["Batter_ContactType"] = RIGHT_NICE

                    if (self.inMemBatter["RightNiceThreshold"] <= self.inMemBatter["CalculatedBallPos"]):
                        self.inMemBatter["Batter_ContactType"] = RIGHT_SOUR

        if (self.inMemBatter["Batter_ContactType"] == PERFECT):
            if (self.inMemBatter["CalculatedBallPos"] >= 100.0):
                self.inMemBatter["ContactQuality"] = 1.0 - (self.inMemBatter["CalculatedBallPos"] - self.inMemBatter["LeftPerfectThreshold"]) / (
                    self.inMemBatter["RightPerfectThreshold"] - self.inMemBatter["LeftPerfectThreshold"])

            else:
                self.inMemBatter["ContactQuality"] = (self.inMemBatter["CalculatedBallPos"] - self.inMemBatter["LeftPerfectThreshold"]) / (
                    self.inMemBatter["RightPerfectThreshold"] - self.inMemBatter["LeftPerfectThreshold"])

            # if ((CONTACT_PERFECT_THRESHOLDS[self.inMemBatter["Batter_Contact_SlapChargeBuntStar"]][0] <= self.inMemBatter["CalculatedBallPos"]) and (self.inMemBatter["CalculatedBallPos"] <= CONTACT_PERFECT_THRESHOLDS[self.inMemBatter["Batter_Contact_SlapChargeBuntStar"]][1])):
            #     self.inMemBatter["mostPerfectContact"] = True

        elif (self.inMemBatter["Batter_ContactType"] < PERFECT):
            if (self.inMemBatter["Batter_ContactType"] == LEFT_SOUR):
                self.inMemBatter["ContactQuality"] = self.inMemBatter["CalculatedBallPos"] / \
                    self.inMemBatter["LeftNiceThreshold"]

            else:
                self.inMemBatter["ContactQuality"] = (self.inMemBatter["CalculatedBallPos"] - self.inMemBatter["LeftNiceThreshold"]) / (
                    self.inMemBatter["LeftPerfectThreshold"] - self.inMemBatter["LeftNiceThreshold"])

        elif (self.inMemBatter["Batter_ContactType"] < RIGHT_SOUR):
            self.inMemBatter["ContactQuality"] = 1.0 - (self.inMemBatter["CalculatedBallPos"] - self.inMemBatter["RightPerfectThreshold"]) / (
                self.inMemBatter["RightNiceThreshold"] - self.inMemBatter["RightPerfectThreshold"])

        else:
            self.inMemBatter["ContactQuality"] = 1.0 - \
                (self.inMemBatter["CalculatedBallPos"] - self.inMemBatter["RightNiceThreshold"]) / \
                (200.0 - self.inMemBatter["RightNiceThreshold"])

        if (self.inMemBatter["AtBat_MoonShot"] != False):
            if (self.inMemBatter["Batter_ContactType"] == PERFECT):
                self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] = 0

            else:
                self.inMemBatter["AtBat_MoonShot"] = False

        self.inMemBatter["Batter_HitType"] = -1
        if ((self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == SLAP) or (self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == CHARGE)):
            # Default to Sour
            self.inMemBatter["Batter_HitType"] = SOUR_CURVE_SLAP
            # Adjust if the hit was nice or perfect
            if (self.inMemBatter["Batter_ContactType"] == PERFECT):
                self.inMemBatter["Batter_HitType"] = PERFECT_CURVE_SLAP

            elif ((self.inMemBatter["Batter_ContactType"] == LEFT_NICE) or (self.inMemBatter["Batter_ContactType"] == RIGHT_NICE)):
                self.inMemBatter["Batter_HitType"] = NICE_CURVE_SLAP

            # Adjust the HitType on a perfect pitch
            # 0xc for strike, 0xf for hit
            if (self.inMemPitcher["ChargePitchType"] == PITCHCHARGETYPE_PERFECT):
                if (self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == SLAP):
                    self.inMemBatter["Batter_HitType"] += SOUR_PERFECTPITCH_SLAP

                else:
                    self.inMemBatter["Batter_HitType"] += SOUR_PERFECTPITCH_CHARGE

            else:
                # Else not perfect charge pitch
                # If the pitch was Curve and contact was not a hit, it was a charge:
                # adjust by 0x3
                if (self.inMemPitcher["Pitcher_TypeOfPitch"] == PITCHCURVE):
                    if (self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] != SLAP):
                        self.inMemBatter["Batter_HitType"] += SOUR_CURVE_CHARGE

                else:
                    # Else non-curve, which I believe is just a change up
                    # adjust by 0x6 for Hit
                    # adjust by 0x9 for Charge
                    if (self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == SLAP):
                        self.inMemBatter["Batter_HitType"] += SOUR_CHANGEUP_SLAP

                    else:
                        self.inMemBatter["Batter_HitType"] += SOUR_CHANGEUP_CHARGE

        self.Display_Output["Contact"] = {
            "DistanceFromPerfect": diffInX,
            "ContactZone": ["Left Sour", "Left Nice", "Perfect", "Right Nice", "Right Sour"][self.inMemBatter["Batter_ContactType"]],
            "ContactQuality": self.inMemBatter["ContactQuality"],
            "AbsoluteContact": self.inMemBatter["CalculatedBallPos"],
            "LeftNiceThreshold" : self.inMemBatter["LeftNiceThreshold"],
            "LeftPerfectThreshold" : self.inMemBatter["LeftPerfectThreshold"],
            "RightPerfectThreshold" : self.inMemBatter["RightPerfectThreshold"],
            "RightNiceThreshold" : self.inMemBatter["RightNiceThreshold"],
        }
        return


    def AdjustBallAngle(ballAngle):
        if (ballAngle < 0):
            while ballAngle < 0:
                ballAngle += 0x1000
        if (0xfff < ballAngle):
            while 0xfff < ballAngle:
                ballAngle += -0x1000
        return ballAngle


    def WeightedRandomIndex(self, vals, count):
        randomSum = 0

        loopSum = 0

        for element in vals:
            loopSum += element

        finSum = loopSum

        if (loopSum < 0):
            finSum = -loopSum

        if (finSum < 2):
            randomSum = 0

        else:
            # update RandomInt in case it's called successive times
            self.StaticRandomInt1 = (self.StaticRandomInt1 - (self.StaticRandomInt2 & 0xff)) + BattingCalculator.floor(self.StaticRandomInt2 / finSum) + self.USHORT_8089269c
            randomRange = self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 / finSum) * finSum
            randomSum = (randomRange >> 0x1f ^ randomRange) - (randomRange >> 0x1f)
            if (loopSum < 0):
                randomSum = -randomSum

        p_loopArray = vals
        newIndex = 0
        i = 0
        if (0 < count):
            while (count != 0):
                if (randomSum < p_loopArray[i]):
                    return newIndex

                randomSum -= p_loopArray[i]
                newIndex += 1
                count += -1
                i += 1

        return 0

    def calculateBuntAngle(self):
        iVar3 = 0
        input = self.inMemBatter["ControllerInput"]

        contactType = self.inMemBatter["Batter_ContactType"]
        iVar2 = self.inMemBatter["Batter_SlapContactSize"] * (BUNT_ANGLE_CALC_ARRAY[contactType][2] - BUNT_ANGLE_CALC_ARRAY[contactType][0])
        iVar1 = self.inMemBatter["Batter_SlapContactSize"] * (BUNT_ANGLE_CALC_ARRAY[contactType][3] - BUNT_ANGLE_CALC_ARRAY[contactType][1])
        iVar2 = BattingCalculator.floor(iVar2 / 100) + (iVar2 >> 0x1f)
        iVar1 = BattingCalculator.floor(iVar1 / 100) + (iVar1 >> 0x1f)
        iVar2 = BUNT_ANGLE_CALC_ARRAY[contactType][0] + (iVar2 - (iVar2 >> 0x1f))
        iVar1 = (BUNT_ANGLE_CALC_ARRAY[contactType][1] + (iVar1 - (iVar1 >> 0x1f))) - iVar2
        iVar2 += self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 / iVar1) * iVar1
        if (contactType != 0):
            if (contactType < 4):
                if (not input["Left"]):
                    if (not input["Right"]):
                        iVar3 = (self.StaticRandomInt2 & 1 ^ -(self.StaticRandomInt2 >> 0x1f)) + (self.StaticRandomInt2 >> 0x1f)
                    elif (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
                        iVar3 = 1
                elif (self.inMemBatter["AtBat_BatterHand"] == RIGHTY):
                    iVar3 = 1
        elif (contactType == 0):
            iVar3 = 1

        if (((self.inMemBatter["AtBat_BatterHand"] == RIGHTY) and (iVar3 != 0)) or ((self.inMemBatter["AtBat_BatterHand"] != RIGHTY and (iVar3 == 0)))):
            if (iVar2 < 0x801):
                iVar2 = 0x800 - iVar2
            else:
                iVar2 = 0x1800 - iVar2

        self.Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(iVar2)

        return

    def calculateBuntingExtras(self):
        uVar5 = ((self.StaticRandomInt1 & 1 ^ self.StaticRandomInt1 >> 0x1f) != self.StaticRandomInt1 >> 0x1f)
        uVar4 = self.inMemBatter["Batter_ContactType"]
        iVar6 = BUNTING_CONTACT_ARRAY[self.inMemBatter["Batter_ContactType"]][uVar5][0]
        iVar7 = BUNTING_CONTACT_ARRAY[uVar4][uVar5][1]
        iVar3 = self.inMemBatter["Batter_SlapContactSize"] * (BUNTING_CONTACT_ARRAY[uVar4][uVar5 + 2][0] - iVar6)
        iVar2 = self.inMemBatter["Batter_SlapContactSize"] * (BUNTING_CONTACT_ARRAY[uVar4][uVar5 + 2][1] - iVar7)
        iVar3 = BattingCalculator.floor(iVar3 / 100) + (iVar3 >> 0x1f)
        iVar2 = BattingCalculator.floor(iVar2 / 100) + (iVar2 >> 0x1f)
        iVar6 += iVar3 - (iVar3 >> 0x1f)
        iVar2 = (iVar7 + (iVar2 - (iVar2 >> 0x1f))) - iVar6
        Hit_VerticalAngle = iVar6 + (self.StaticRandomInt1 - (self.StaticRandomInt1 / iVar2) * iVar2)

        if (Hit_VerticalAngle < 0x401):
            if (Hit_VerticalAngle < -0x400):
                Hit_VerticalAngle += 0x1000
                Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(Hit_HorizontalAngle + 0x800)

            elif (Hit_VerticalAngle < 0):
                Hit_VerticalAngle += 0x1000
        else:
            Hit_VerticalAngle = 0x800 - Hit_VerticalAngle
            Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(Hit_HorizontalAngle + 0x800)

        iVar2 = BUNTING_POWER_ARRAY[self.inMemBatter["Batter_ContactType"]][1] - BUNTING_POWER_ARRAY[self.inMemBatter["Batter_ContactType"]][0]
        self.Hit_HorizontalPower = (self.StaticRandomInt1 - (self.StaticRandomInt1 / iVar2) * iVar2) + BUNTING_POWER_ARRAY[self.inMemBatter["Batter_ContactType"]][0]
        
        self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] = 0
        return

    def calculateHorizontalAngle(self):
        input = self.inMemBatter["ControllerInput"]

        isCharge = 1 if self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] != SLAP else 0
        self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_NONE
        if (self.inMemBatter["AtBat_Mystery_BatDirection"] == 0):
            if (not input["Right"]):
                if (input["Left"]):
                    if (self.inMemBatter["AtBat_BatterHand"] == RIGHTY):
                        self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_PULL

                    else:
                        self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_PUSH

            elif (self.inMemBatter["AtBat_BatterHand"] == RIGHTY):
                self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_PUSH

            else:
                self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_PULL

        inputDirection = self.inMemBatter["AtBat_InputDirection"]
        frameOfContact = self.inMemBatter["Frame_SwingContact1"]
        iVar2 = BATTING_ANGLE_RANGES[inputDirection][isCharge][frameOfContact][0]
        iVar1 = BATTING_ANGLE_RANGES[inputDirection][isCharge][frameOfContact][1]

        self.Display_Output["Horizontal Range"] = [
            BATTING_ANGLE_RANGES[inputDirection][isCharge][frameOfContact][0] + 0x400,
            BATTING_ANGLE_RANGES[inputDirection][isCharge][frameOfContact][1] + 0x400
        ]

        iVar1 -= iVar2
        if (iVar1 < 0):
            iVar2 += self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 / -iVar1) * -iVar1

        elif (0 < iVar1):
            iVar2 += self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 / iVar1) * iVar1

        iVar2 += 0x400
        if (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
            if (iVar2 < 0x801):
                iVar2 = 0x800 - iVar2

            else:
                iVar2 = 0x1800 - iVar2

        self.Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(iVar2)

        if "override_horizontal_angle" in self.readValues:
            self.Hit_HorizontalAngle = self.readValues["override_horizontal_angle"]


    def calculateVerticalAngle(self):
        iVar5 = 0
        upDown = 0
        slapOrCharge = 0 if self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == 0 else 1
        pInput = self.inMemBatter["ControllerInput"]

        handledVerticalZones = False

        captainStarSwing = self.inMemBatter["AtBat_Mystery_CaptainStarSwing"]
        if (captainStarSwing == 0):
            if (self.inMemBatter["AtBat_MoonShot"] == False):
                noncaptainStarSwing = self.inMemBatter["nonCaptainStarSwingContact"]
                if (noncaptainStarSwing == 0):
                    if (self.inMemBatter["AtBat_Mystery_BatDirection"] == 0):
                        if (not pInput["Up"]):
                            if (pInput["Down"]):
                                # 2 == Down
                                upDown = 2

                        else:
                            # 1 == Up
                            upDown = 1

                    pabVar4 = BATTING_VERTICAL_ANGLE_WEIGHTS[self.inMemBatter["AtBat_HitTrajectoryLow"]][slapOrCharge][self.inMemBatter["EasyBatting"]][self.inMemBatter["Batter_ContactType"]]
                    local_28 = pabVar4[0]
                    local_27 = pabVar4[1]
                    local_26 = pabVar4[2]
                    local_25 = pabVar4[3]
                    local_24 = pabVar4[4]

                    uVar4 = UINT_ARRAY_ARRAY_807B7134[self.inMemBatter["Batter_HitType"]][3 - self.inMemBatter["EasyBatting"]]
                    uVar6 = UINT_ARRAY_ARRAY_807B7134[self.inMemBatter["Batter_HitType"]][4]
                    uVar5 = uVar4 & 0xf000000
                    if (uVar5 == 0):
                        uVar16 = uVar4 & 0xf
                        if (uVar16 != 0):
                            iVar5 = 2
                            if (uVar16 == 2):
                                if (upDown == 2):
                                    iVar5 = 0
                                    uVar6 = 2

                            elif ((uVar16 == 3) and (upDown == 1)):
                                iVar5 = 0
                                uVar6 = 2

                    else:
                        iVar5 = 1
                        if (uVar5 == 0x2000000):
                            if (upDown == 2):
                                iVar5 = 0
                                uVar6 = 2

                        elif ((uVar5 == 0x3000000) and (upDown == 1)):
                            iVar5 = 0
                            uVar6 = 2

                    if (uVar6 == 1):
                        DAT_80893800_VertAngle = 2

                    elif (uVar6 == 2):
                        DAT_80893800_VertAngle = 3

                    if (iVar5 == 0):
                        if ((uVar4 & 0x1e0) == 0):
                            local_28 = 0

                        if ((uVar4 & 0xf0) == 0):
                            local_27 = 0

                        if ((uVar4 & 0x78) == 0):
                            local_26 = 0

                        if ((uVar4 & 0x3c) == 0):
                            local_25 = 0

                        if ((uVar4 & 0x1e) == 0):
                            local_24 = 0

                        if (upDown == 2):
                            local_24 += local_28
                            local_28 = 0

                        elif (upDown == 1):
                            cVar2 = local_24 + local_28
                            local_24 = 0
                            local_28 = local_25 + cVar2
                            local_25 = 0

                    if (iVar5 == 0):
                        weightedRandomIndex = self.WeightedRandomIndex([local_28, local_27, local_26, local_25, local_24], 5)

                        if "override_vertical_range" in self.readValues:
                            weightedRandomIndex = self.readValues["override_vertical_range"]

                        # Regular star swings
                        lowerRange = SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[slapOrCharge][self.inMemBatter["Batter_ContactType"]][weightedRandomIndex][0]
                        higherRange = SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[slapOrCharge][self.inMemBatter["Batter_ContactType"]][weightedRandomIndex][1]
                        
                        self.Display_Output["Vertical Details"] = {
                            "Zones" : SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[slapOrCharge][self.inMemBatter["Batter_ContactType"]],
                            "Weights": [local_28, local_27, local_26, local_25, local_24],
                            "Selected Zone": weightedRandomIndex
                        }

                        handledVerticalZones = True

                    else:
                        lowerRange = SHORT_ARRAY_ARRAY_807B6AF4[iVar5][0]
                        higherRange = SHORT_ARRAY_ARRAY_807B6AF4[iVar5][1]

                else:
                    # Non Captain Star Swings
                    lowerRange = NON_CAPTAIN_STAR_VERTICAL_ANGLES[
                        noncaptainStarSwing - 1][self.inMemBatter["Batter_ContactType"]][0]
                    higherRange = NON_CAPTAIN_STAR_VERTICAL_ANGLES[
                        noncaptainStarSwing - 1][self.inMemBatter["Batter_ContactType"]][1]

            else:
                # Moonshot, also uses Charge Angles
                lowerRange = SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[1][self.inMemBatter["Batter_ContactType"]][2][0]
                higherRange = SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[1][self.inMemBatter["Batter_ContactType"]][2][1]

        else:
            # Captain Star Swings
            lowerRange = CAPTAIN_STAR_VERTICAL_ANGLES[captainStarSwing - 1][self.inMemBatter["Batter_ContactType"]][0]
            higherRange = CAPTAIN_STAR_VERTICAL_ANGLES[captainStarSwing - 1][self.inMemBatter["Batter_ContactType"]][1]

        if (not handledVerticalZones):
            self.Display_Output["Vertical Details"] = {
                "Zones": [[lowerRange, higherRange]],
                "Weights": [100],
                "Selected Zone": 0
            }

        self.Display_Output["Vertical Details"]["Selected Range"] = [lowerRange, higherRange]

        sVar3 = lowerRange + (self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 /
                                                    (higherRange - lowerRange)) * (higherRange - lowerRange))

        self.Hit_VerticalAngle = sVar3

        if "override_vertical_angle" in self.readValues:
            self.Hit_VerticalAngle = self.readValues["override_vertical_angle"]

        if (self.Hit_VerticalAngle < 0x401):
            if (self.Hit_VerticalAngle < -0x400):
                self.Hit_VerticalAngle += 0x1000
                self.Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(self.Hit_HorizontalAngle + 0x800)

            elif (self.Hit_VerticalAngle < 0):
                self.Hit_VerticalAngle += 0x1000

        else:
            self.Hit_VerticalAngle = 0x800 - self.Hit_VerticalAngle
            self.Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(self.Hit_HorizontalAngle + 0x800)


    def calculateHitPower(self):
        uVar2 = 0
        niceSour = self.inMemBatter["Batter_ContactType"]
        charged = self.inMemBatter["BatterAtPlate_BatterCharge_Up"]

        # Regular contact array
        contactArray = BALL_HIT_ARRAY[self.inMemBatter["Batter_Contact_SlapChargeBuntStar"]][niceSour]

        if (self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] == 0):
            if (self.inMemBatter["nonCaptainStarSwingContact"] != 0):
                charged = 0.0
                # NonCaptainStarSwing array
                contactArray = STAR_SWING_EXIT_VELOCITY_ARRAY[self.inMemBatter["nonCaptainStarSwingContact"] - 1][niceSour]

        else:
            charged = 0.0
            # CaptainStarSwingArray
            contactArray = CAPTAIN_STAR_SWING_EXIT_VELOCITY_ARRAY[self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] - 1][niceSour]

        if (self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] != False):
            self.inMemBatter["BatterAtPlate_BatterCharge_Down"] = 1.0

        if (self.inMemBatter["AtBat_MoonShot"]):
            # Moonshot array
            contactArray = BALL_HIT_ARRAY[1][self.inMemBatter["Batter_ContactType"]]

        # Low value
        arrayV1 = contactArray[0]
        # High Value
        arrayV2 = contactArray[1]
        # 0x44 is a range 0-1 towards the better contact
        calcedDistance = self.inMemBatter["ContactQuality"] * (arrayV2 - arrayV1) + arrayV1
        # Non star swing
        if (self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] == 0):
            if (charged <= 0.0):
                # If not charged, use slap hit power
                power = self.inMemBatter["Batter_SlapHitPower"]

            else:
                # use charge power
                power = (self.inMemBatter["BatterAtPlate_ChargePower"] - (self.inMemBatter["BatterAtPlate_ChargePower"] - self.inMemBatter["Batter_SlapHitPower"]) * 0.5 * (1.0 - self.inMemBatter["BatterAtPlate_BatterCharge_Down"]))

        else:
            # if star swing, power is always 100
            power = 100.0

        if ((self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] == 0) and (self.inMemBatter["nonCaptainStarSwingContact"] == 0)):
            perfectNiceSour = 2
            if ((self.inMemBatter["Batter_ContactType"] == LEFT_NICE) or (self.inMemBatter["Batter_ContactType"] == RIGHT_NICE)):
                perfectNiceSour = 1

            elif (self.inMemBatter["Batter_ContactType"] == PERFECT):
                perfectNiceSour = 0

            dVar3 = BattingCalculator.LinearInterpolateToNewRange(self.inMemPitcher["calced_cursedBall"], 0.0, 100.0,
                                                CURSED_BALL_DEBUFF_ARRAY[perfectNiceSour][0], CURSED_BALL_DEBUFF_ARRAY[perfectNiceSour][1])
            power = (power * dVar3)

        if ((self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"] != 0) and (0.0 < charged)):
            # If charging, add a multiplier for chem on base
            power = (
                power * POWER_CHEM_LINK_MULTIPLIERS[self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"]])

        if (-1 < self.inMemBatter["Batter_HitType"]):
            power = (
                power * UINT_ARRAY_ARRAY_807B7134[self.inMemBatter["Batter_HitType"]][1 - self.inMemBatter["EasyBatting"]]) / 100.0

        fVar1 = (calcedDistance * ((power / 100.0) * (1.0 - 0.8) + 0.8))

        self.AddedContactGravity = 0.00001 * contactArray[2]

        self.Display_Output["PowerDetails"] = {
            "CalculatedCharacterPower" : power,
            "CalculatedContactPower" : calcedDistance,
            "AddedGravity" : contactArray[2],
        }

        if (self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] == 0):
            ballAngle = self.Hit_HorizontalAngle
            if (ballAngle < 0x200):
                niceSour = 0

            elif (ballAngle < 0x601):
                niceSour = ballAngle - 0x200

            else:
                niceSour = 0x400

            if (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
                niceSour = 0x400 - niceSour

            if (niceSour < 0x100):
                iVar1 = 0

            elif (niceSour < 0x200):
                iVar1 = 1
                niceSour -= 0x100

            elif (niceSour < 0x300):
                iVar1 = 2
                niceSour -= 0x200

            else:
                iVar1 = 3
                niceSour -= 0x300
            
            fieldAreaBonus = BattingCalculator.LinearInterpolateToNewRange(
                (niceSour / 256), 0.0, 1.0, FIELD_TRAJECTORY_BONUSES[self.inMemBatter["BatterAtPlate_TrajectoryNearFar"]][iVar1], FIELD_TRAJECTORY_BONUSES[self.inMemBatter["BatterAtPlate_TrajectoryNearFar"]][iVar1 + 1])
            self.Display_Output["PowerDetails"]["FieldBonus"] = fieldAreaBonus
            fVar1 = (fVar1 * fieldAreaBonus)
        else:
            self.Display_Output["PowerDetails"]["FieldBonus"] = 0.0
        if (self.inMemBatter["AtBat_MoonShot"]):
            fVar1 = (fVar1 * MOONSHOT_MULTIPLIER)

        if "override_power" in self.readValues:
            fVar1 = self.readValues["override_power"] 

        self.Hit_HorizontalPower = BattingCalculator.floor(fVar1)
        return


    def isEmptyOrSpaces(s: str):
        return True if len(s) == 0 else s.isspace()

    def parseValues(self):
        self.Display_Output = {}
        self.inMemBall = {}
        self.inMemPitcher = {}
        self.inMemPitcher["calced_cursedBall"] = STATS[self.readValues["pitcher_id"]]["Cursed Ball"]
        pitcherChargeVal = self.readValues["pitcherChargeVal"]
        if (pitcherChargeVal == 0):
            self.inMemPitcher["Pitcher_TypeOfPitch"] = PITCHCURVE
            self.inMemPitcher["ChargePitchType"] = PITCHCHARGETYPE_NONE

        elif (pitcherChargeVal == 1):
            self.inMemPitcher["Pitcher_TypeOfPitch"] = PITCHCHARGE
            self.inMemPitcher["ChargePitchType"] = PITCHCHARGETYPE_CHARGE

        elif (pitcherChargeVal == 2):
            self.inMemPitcher["Pitcher_TypeOfPitch"] = PITCHCHARGE
            self.inMemPitcher["ChargePitchType"] = PITCHCHARGETYPE_PERFECT

        elif (pitcherChargeVal == 3):
            self.inMemPitcher["Pitcher_TypeOfPitch"] = PITCHCHANGEUP
            self.inMemPitcher["ChargePitchType"] = PITCHCHARGETYPE_NONE

        self.StaticRandomInt1 = None
        self.StaticRandomInt2 = None
        self.USHORT_8089269c = None

        if (self.readValues["StaticRandomInt1"] != None):
            self.StaticRandomInt1 = self.readValues["StaticRandomInt1"]
        else:
            self.StaticRandomInt1 = BattingCalculator.floor(random() * 2 ** 15)

        if (self.readValues["StaticRandomInt2"] != None):
            self.StaticRandomInt2 = self.readValues["StaticRandomInt2"]
        else:
            self.StaticRandomInt2 = BattingCalculator.floor(random() * 2 ** 15)

        if (self.readValues["USHORT_8089269c"] != None):
            self.USHORT_8089269c = self.readValues["USHORT_8089269c"]
        else:
            self.USHORT_8089269c = BattingCalculator.floor(random() * 2 ** 15)

        self.inMemBatter = {}
        id = self.readValues["batter_id"]

        self.inMemBatter["Batter_CharID"] = id
        self.inMemBatter["IsCaptain"] = self.readValues["IsCaptain"]
        self.inMemBatter["Name"] = STATS[id]["Name"]
        self.inMemBatter["AtBat_Mystery_BatDirection"] = 0
        self.inMemBatter["AtBat_TrimmedBat"] = 0 if BATTER_HITBOXES[id]["TrimmedBat"] == 0.0 else 1

        self.inMemBatter["ballContact_X"] = self.readValues["ballContact_X"]
        self.inMemBatter["ballContact_Z"] = self.readValues["ballContact_Z"]
        self.inMemBatter["posX"] = self.readValues["posX"]

        self.inMemBatter["AtBat_BatterHand"] = self.readValues["AtBat_BatterHand"]

        self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = self.readValues["Batter_Contact_SlapChargeBuntStar"]
        self.inMemBatter["Batter_IsBunting"] = self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == BUNT

        self.inMemBatter["BatterAtPlate_BatterCharge_Up"] = self.readValues["chargeUp"]
        self.inMemBatter["BatterAtPlate_BatterCharge_Down"] = self.readValues["chargeDown"]
        self.inMemBatter["AtBat_IsFullyCharged"] = self.inMemBatter["BatterAtPlate_BatterCharge_Up"] == 1.0

        self.inMemBatter["Batter_SlapHitPower"] = STATS[id]["Slap Hit Power"]
        self.inMemBatter["BatterAtPlate_ChargePower"] = STATS[id]["Charge Hit Power"]

        self.inMemBatter["Batter_SlapContactSize"] = STATS[id]["Slap Contact Spot Size"]
        self.inMemBatter["Batter_ChargeContactSize"] = STATS[id]["Charge Contact Spot Size"]
        self.inMemBatter["Batter_Bunting"] = STATS[id]["Bunting"]

        self.inMemBatter["BatterAtPlate_TrajectoryNearFar"] = STATS[id]["Horizontal Hit Trajectory"]
        self.inMemBatter["AtBat_HitTrajectoryLow"] = STATS[id]["Vertical Hit Trajectory"]

        self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"] = self.readValues["RandomBattingFactors_ChemLinksOnBase"]
        self.inMemBatter["Frame_SwingContact1"] = self.readValues["frameOfContact"]

        self.inMemBatter["EasyBatting"] = self.readValues["EasyBatting"]
        self.inMemBatter["isStar"] = self.readValues["isStar"]

        self.inMemBatter["AtBat_MoonShot"] = False

        self.inMemBatter["ControllerInput"] = {
            "Up": self.readValues["Up"],
            "Down": self.readValues["Down"],
            "Left": self.readValues["Left"],
            "Right": self.readValues["Right"]
        }

        self.inMemBatter["AtBat_CaptainStarHitPitch"] = STATS[id]["Captain Star Hit/Pitch"]
        self.inMemBatter["AtBat_NonCaptainStarSwing"] = STATS[id]["Non Captain Star Swing"]

        self.inMemBatter["nonCaptainStarSwingContact"] = 0
        self.inMemBatter["nonCaptainStarSwingContact"] = 0
        self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] = 0
        self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] = False

        self.inMemBatter["Stars"] = self.readValues["numStars"]

        if(self.readValues["is_starred"]):
            self.inMemBatter["Batter_SlapContactSize"] = min(self.inMemBatter["Batter_SlapContactSize"]+ 50, 100)
            self.inMemBatter["Batter_ChargeContactSize"] = min(self.inMemBatter["Batter_ChargeContactSize"]+ 50, 100)

            self.inMemBatter["Batter_SlapHitPower"] = min(self.inMemBatter["Batter_SlapHitPower"]+ 50, 100)
            self.inMemBatter["BatterAtPlate_ChargePower"] = min(self.inMemBatter["BatterAtPlate_ChargePower"]+ 50, 100)
            self.inMemBatter["Batter_Bunting"] = min(self.inMemBatter["Batter_Bunting"]+ 50, 100)

            self.inMemPitcher["calced_cursedBall"] = min(self.inMemPitcher["calced_cursedBall"]+ 50, 100)


    def hitBall(self):
        fVar1 = self.inMemBatter["ballContact_X"]

        if (BATTING_REACHES[self.inMemBatter["AtBat_TrimmedBat"]][0] <= fVar1 - self.inMemBatter["posX"]):
            if (fVar1 - self.inMemBatter["posX"] <= BATTING_REACHES[self.inMemBatter["AtBat_TrimmedBat"]][1]):
                self.inMemBatter["interstitialBallContact_X"] = fVar1
                return True

        return False


    def mssbConvertToRadians(param_1):
        if (param_1 < 0):
            param_1 += 0x1000

        if (0xfff < param_1):
            param_1 += -0x1000

        dVar1 = (math.pi * (param_1 << 1)) / 4096
        if (math.pi < dVar1):
            dVar1 = -(2*math.pi - dVar1)

        return dVar1


    def convertPowerToVelocity(self):
        self.inMemBall["ballVelocity"] = {"X": 0, "Y": 0, "Z": 0}
        self.inMemBall["ballAcceleration"] = {"X": 0, "Y": 0, "Z": 0}

        half_power = self.Hit_HorizontalPower * 0.5

        horizontalAngle = BattingCalculator.mssbConvertToRadians(self.Hit_HorizontalAngle)
        verticalAngle = BattingCalculator.mssbConvertToRadians(self.Hit_VerticalAngle)

        s_verticalAngle = math.sin(verticalAngle)
        c_verticalAngle = math.cos(verticalAngle)

        half_power_x_cos_vert_angle = half_power * c_verticalAngle

        c_horizontalAngle = math.cos(horizontalAngle)
        s_horizontalAngle = math.sin(horizontalAngle)

        x_groundVelocity = c_horizontalAngle * half_power_x_cos_vert_angle
        z_groundVelocity = s_horizontalAngle * half_power_x_cos_vert_angle

        self.inMemBall["ballVelocity"]["X"] = x_groundVelocity / 100.0
        self.inMemBall["ballVelocity"]["Y"] = (half_power * s_verticalAngle) / 100.0
        self.inMemBall["ballVelocity"]["Z"] = z_groundVelocity / 100.0

        self.inMemBall["ballAcceleration"]["X"] = 0.0
        self.inMemBall["ballAcceleration"]["Y"] = self.AddedContactGravity
        self.inMemBall["ballAcceleration"]["Z"] = 0.0

        if ((self.inMemBatter["Batter_IsBunting"] == False) and (self.Hit_HorizontalAngle < 0x901 or 0xeff < self.Hit_HorizontalAngle)):
            # has Super Curve
            hasSuperCurve = 1 if self.inMemBatter["Batter_CharID"] in [
                0xe, 0x35, 0x25] else 0

            # non-captain star swing 3 has super curve
            if (self.inMemBatter["nonCaptainStarSwingContact"] == 3):
                hasSuperCurve = 1

            # if contact above 100, flip it
            contact = self.inMemBatter["CalculatedBallPos"]
            if (100.0 < self.inMemBatter["CalculatedBallPos"]):
                contact = 200.0 - self.inMemBatter["CalculatedBallPos"]

            vAngle = self.Hit_VerticalAngle
            fVar1 = (1.0 - (1.0 - contact * 0.01) *
                    FLOAT_ARRAY_ARRAY_807B72BC[hasSuperCurve][0])

            if ((0x180 < vAngle) and (vAngle < 0x401)):
                uVar3 = vAngle - 0x180
                contact = uVar3
                if (512.0 < uVar3):
                    contact = 512.0

                fVar1 = fVar1 * (1.0 - contact * 1.0 / 512.0)

            hAngle = self.Hit_HorizontalAngle

            if ((hAngle < 0xc01) and (0xff < hAngle)):
                if (0x700 < hAngle):
                    hAngle = 0x700

            else:
                hAngle = 0x100

            if (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
                hAngle = 0x800 - hAngle

            if (hAngle < 0x460):
                contact = (0x460 - hAngle) / 864.0

            else:
                contact = (0x460 - hAngle) / 672.0

            contact = (fVar1 * contact)
            if (0.0 <= contact):
                if (0.0 < contact):
                    z_groundVelocity = -c_horizontalAngle
                    x_groundVelocity = s_horizontalAngle

            else:
                contact = -contact
                z_groundVelocity = c_horizontalAngle
                x_groundVelocity = -s_horizontalAngle

            # finalize acceleration
            self.inMemBall["ballAcceleration"]["Z"] = (
                z_groundVelocity * contact) * FLOAT_ARRAY_ARRAY_807B72BC[hasSuperCurve][2]
            self.inMemBall["ballAcceleration"]["X"] = (
                x_groundVelocity * contact) * FLOAT_ARRAY_ARRAY_807B72BC[hasSuperCurve][1]

            # if z is backwards, flip it
            if (0.0 < self.inMemBall["ballAcceleration"]["Z"]):
                self.inMemBall["ballAcceleration"]["Z"] = -self.inMemBall["ballAcceleration"]["Z"]

            # if batting lefty, flip it
            if (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
                self.inMemBall["ballAcceleration"]["X"] = -self.inMemBall["ballAcceleration"]["X"]
        
        self.Display_Output["BallDetails"] = { 
            "HorizontalAngle":self.Hit_HorizontalAngle,
            "VerticalAngle":self.Hit_VerticalAngle,
            "Power":self.Hit_HorizontalPower,

            "Velocity":self.inMemBall["ballVelocity"],
            "Acceleration":self.inMemBall["ballAcceleration"],
        }

    def calculateHitGround(self):
        p = {"X": self.inMemBatter["ballContact_X"], "Y": BATTER_HITBOXES[self.inMemBatter["Batter_CharID"]]["PitchingHeight"], "Z": self.inMemBatter["ballContact_Z"]}
        if self.inMemBatter["AtBat_BatterHand"] != RIGHTY:
            p["X"] = -p["X"]

        CalculatedPoints = []

        v = {k: v for k, v in self.inMemBall["ballVelocity"].items()}
        a = {k: v for k, v in self.inMemBall["ballAcceleration"].items()}

        airResistance = 0.996
        gravity = 0.00275

        while (p["Y"] > 0):
            CalculatedPoints.append({k: v for k, v in p.items()})

            p["X"] = p["X"] + v["X"]
            p["Y"] = p["Y"] + v["Y"]
            p["Z"] = p["Z"] + v["Z"]

            v["X"] = v["X"] * airResistance + a["X"]
            v["Y"] = (v["Y"] - gravity) * airResistance + a["Y"]
            v["Z"] = v["Z"] * airResistance + a["Z"]
        
        self.Display_Output["FlightDetails"] = {
            "Frames": len(CalculatedPoints), 
            "HitGround": CalculatedPoints[-1], 
            "Distance": math.sqrt(CalculatedPoints[-1]["X"] ** 2 + CalculatedPoints[-1]["Z"] ** 2),
            "Path": CalculatedPoints
        } 
        # print(CalculatedPoints)


    def calculateValues(self):
        if(not self.hitBall()):
            self.Display_Output["err"] = "The ball would not hit the bat with these values"
            return

        starsForBatter = self.inMemBatter["Stars"]
        if (self.inMemBatter["isStar"]):
            if (self.inMemBatter["Batter_IsBunting"] == False):
                if (starsForBatter != 0):
                    if ((self.inMemBatter["AtBat_IsFullyCharged"] == False) or (starsForBatter < 5)):
                        if (self.inMemBatter["AtBat_CaptainStarHitPitch"] == 0):
                            if ((starsForBatter < 1) or (self.inMemBatter["AtBat_NonCaptainStarSwing"] == 0)):
                                self.inMemBatter["isStar"] = False

                            else:
                                self.inMemBatter["nonCaptainStarSwingContact"] = self.inMemBatter["AtBat_NonCaptainStarSwing"]
                                if (self.inMemBatter["AtBat_NonCaptainStarSwing"] == 2):
                                    self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = CHARGE
                                    self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] = True
                                    self.inMemBatter["BatterAtPlate_BatterCharge_Up"] = 1.0

                                elif (self.inMemBatter["AtBat_NonCaptainStarSwing"] < 2):
                                    if (self.inMemBatter["AtBat_NonCaptainStarSwing"] != 0):
                                        self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = CHARGE
                                        self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] = True
                                        self.inMemBatter["BatterAtPlate_BatterCharge_Up"] = 1.0

                                elif (self.inMemBatter["AtBat_NonCaptainStarSwing"] < 4):
                                    self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = SLAP

                        elif (self.inMemBatter["IsCaptain"]):
                            if (starsForBatter < 1):
                                self.inMemBatter["isStar"] = False

                            else:
                                self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = STAR

                        elif (starsForBatter < 2):
                            self.inMemBatter["isStar"] = False

                        else:
                            self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = STAR

                    else:
                        self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = STAR
                        self.inMemBatter["AtBat_MoonShot"] = True

                    if ((self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == STAR) or (self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] != False)):
                        self.inMemBatter["AtBat_Mystery7"] = 0
                        self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] = self.inMemBatter["AtBat_CaptainStarHitPitch"]

            else:
                self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = BUNT
                self.inMemBatter["AtBat_MoonShot"] = False

        self.calculateContact()
        if(not self.inMemBatter["Batter_IsBunting"]):
            self.calculateHorizontalAngle()

            self.calculateVerticalAngle()

            self.calculateHitPower()
        else:
            self.calculateBuntAngle()

            self.calculateBuntingExtras()

        self.convertPowerToVelocity()

        self.calculateHitGround()

        self.Display_Output["err"] = None

        return self.Display_Output


    def valueToDegrees(v):
        return (v / 4096) * 360


    def degreesToRadians(d):
        return d * math.pi / 180



def hit_ball(**kwargs) -> dict:
    """ Returns power, trajectory, and other information about hitting a ball.

    batter_id: int, default 0, (short) 80890972
    is_batter_captain: bool, default False
    pitcher_id: int, default 0, (short) 80890ada

    easy_batting: bool, default false, (bool) 8089098a
    handedness: int, (0) Righty, (1) Lefty, default 0, (bool) 8089098a

    batter_x: float, default 0.0, (float) 8089095c
    ball_x: float, default 0.0, (float) 80890934
    ball_z: float, default 0.0, (float) 8089093c

    chem: int, default 0, (byte) 808909ba

    num_stars: int, default 4, (Used to calculate if moonshot)

    hit_type: int, (0) Slap, (1) Charge, default 0, (byte) 8089099b
    is_star_hit: bool, default false, (bool) 808909b1
    is_starred: bool, default false

    pitch_type: int, (0)Curve (1)Charge (2)PerfectCharge (3)ChangeUp, default 0, (byte) 80890b21 (byte) 80890b1f

    charge_up, float, default 0.0, (float) 80890968
    charge_down, float, default 0.0, (float) 8089096c

    frame: int, default 2, (short) 80890976

    stick_up: bool, default false
    stick_down: bool, default false
    stick_left: bool, default false
    stick_right: bool, default false

    rand_1: int, default 0, (uint) 80892684
    rand_2: int, default 0, (uint) 80892688
    rand_3: int, default 0, (ushort) 8089269C
    """

    kwargs.setdefault("batter_id", 0)
    kwargs.setdefault("is_batter_captain", False)
    kwargs.setdefault("pitcher_id", 0)

    kwargs.setdefault("easy_batting", False)
    kwargs.setdefault("handedness", 0)

    kwargs.setdefault("batter_x", 0.0)
    kwargs.setdefault("ball_x", 0.0)
    kwargs.setdefault("ball_z", 0.0)

    kwargs.setdefault("chem", 0)
    kwargs.setdefault("num_stars", 4)
    
    kwargs.setdefault("hit_type", 0)
    kwargs.setdefault("is_star_hit", False)
    kwargs.setdefault("is_starred", False)

    kwargs.setdefault("pitch_type", 0)

    kwargs.setdefault("charge_up", 0.0)
    kwargs.setdefault("charge_down", 0.0)

    kwargs.setdefault("frame", 0)

    kwargs.setdefault("stick_up", False)
    kwargs.setdefault("stick_down", False)
    kwargs.setdefault("stick_left", False)
    kwargs.setdefault("stick_right", False)

    kwargs.setdefault("rand_1", 0)
    kwargs.setdefault("rand_2", 0)
    kwargs.setdefault("rand_3", 0)


    newArgs = {
        "batter_id": kwargs["batter_id"],
        "IsCaptain": kwargs["is_batter_captain"],
        "pitcher_id": kwargs["pitcher_id"],

        "EasyBatting": kwargs["easy_batting"],
        "AtBat_BatterHand": kwargs["handedness"],
        
        "posX": kwargs["batter_x"],
        "ballContact_X": kwargs["ball_x"],
        "ballContact_Z": kwargs["ball_z"],

        "RandomBattingFactors_ChemLinksOnBase": kwargs["chem"],

        "Batter_Contact_SlapChargeBuntStar": kwargs["hit_type"],
        "isStar": kwargs["is_star_hit"],
        "is_starred": kwargs["is_starred"],

        "pitcherChargeVal": kwargs["pitch_type"],

        "chargeUp": kwargs["charge_up"],
        "chargeDown": kwargs["charge_down"],

        "frameOfContact" : kwargs["frame"],

        "Up" : kwargs["stick_up"],
        "Down" : kwargs["stick_down"],
        "Left" : kwargs["stick_left"],
        "Right" : kwargs["stick_right"],

        "StaticRandomInt1" : kwargs["rand_1"],
        "StaticRandomInt2" : kwargs["rand_2"],
        "USHORT_8089269c" : kwargs["rand_3"],

        "numStars" : kwargs["num_stars"]
    }

    if "override_vertical_range" in kwargs:
        newArgs["override_vertical_range"] = kwargs["override_vertical_range"]

    if "override_vertical_angle" in kwargs:
        newArgs["override_vertical_angle"] = kwargs["override_vertical_angle"]
    
    if "override_horizontal_angle" in kwargs:
        newArgs["override_horizontal_angle"] = kwargs["override_horizontal_angle"]

    if "override_power" in kwargs:
        newArgs["override_power"] = kwargs["override_power"]

    c = BattingCalculator()

    c.readValues = newArgs
    c.parseValues()
    try:
        return c.calculateValues()
    except BaseException as e:
        return {"err": f"{e=}"}

def get_hitbox(char_id) -> tuple:
    return HBP_ARRAY[CHARACTER_INDICES[char_id][2]]

def get_box_movement(char_id):
    return BATTER_HITBOXES[char_id]


def get_bat_hitbox(char_id, pos_x, handedness):
   trimmed = 0 if BATTER_HITBOXES[char_id]["TrimmedBat"] == 0.0 else 1
   hb = BATTING_REACHES[trimmed]
   near = pos_x + hb[0]
   far = pos_x + hb[1]

   if handedness == 1:
        near *= -1.0
        far *= -1.0

   return (near, far)

def get_name(char_id)->str:
    return STATS[char_id]["Name"]

# if __name__ == "__main__":
#     e = hit_ball(
#         batter_id = 2,
#         pitcher_id = 26,
#         easy_batting = False,
#         handedness = 0,
#         batter_x = 0.0,
#         ball_x = 0.2101,
#         ball_z = 0.0,
#         chem = 2,
#         hit_type = 0,
#         is_star_hit = False,
#         pitch_type = 3,
#         charge_up = 0.0,
#         charge_down = 0.0,
#         frame = 4,
#         rand_1 = 30677,
#         rand_2 = 2380,
#         rand_3 = 29261,
#         stick_down = True,
#         num_stars = 4,
#         is_starred = False,
#     )
#     print(json.dumps(e, sort_keys=True, indent=4))
