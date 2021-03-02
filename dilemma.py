#!/usr/bin/env python3
#1 = trahir
#0 = cooperer
def main():
    list_play_j1 = []
    list_play_j2 = []
    score_j1 = 0
    score_j2 = 0
    print (list_play_j1)
    print (list_play_j2)
    for i in range (10):
        rep_j1 = j1(i, list_play_j1, list_play_j2, score_j1, score_j2)
        rep_j2 = j2(i, list_play_j2, list_play_j1, score_j2, score_j1)
        list_play_j1.append(rep_j1)
        list_play_j2.append(rep_j2)
        if (rep_j1 == 1 and rep_j2 == 0):
            score_j1 += 5
        if (rep_j2 == 1 and rep_j1 == 0):
            score_j2 += 5
        if (rep_j2 == 0 and rep_j1 == 0):
            score_j2 += 3
            score_j1 += 3
        if (rep_j2 == 1 and rep_j1 == 1):
            score_j2 += 1
            score_j1 += 1
    print ("JOUEUR 1 :\n\tScore = ", score_j1, "\n\t",list_play_j1)
    print ("JOUEUR 2 :\n\tScore = ", score_j2, "\n\t",list_play_j2)
    
def j1(turn, my_list, your_list, my_score, your_score):
    if (turn == 0) :
        return 0
    return (your_list[turn-1])

def j2(turn, my_list, your_list, my_score, your_score):
    return (turn%2)

#1 = trahir
#0 = cooperer

main()