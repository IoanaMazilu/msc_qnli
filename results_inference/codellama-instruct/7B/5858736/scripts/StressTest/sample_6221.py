money_premise = 200
priya_share_premise = 2
mani_share_premise = 4
rani_share_premise = 8

money_hypothesis = 100
priya_share_hypothesis = 1
mani_share_hypothesis = 2
rani_share_hypothesis = 4

# the hypothesis talks about a lesser ratio than the premise
if priya_share_hypothesis <= priya_share_premise and mani_share_hypothesis <= mani_share_premise and rani_share_hypothesis <= rani_share_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives a ratio of 2:4:8, but the hypothesis talks about a lesser ratio
    # any ratio less than 2:4:8 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
