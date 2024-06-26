priya_share_premise = 0 # less than 4
mani_share_premise = 0 # 4
rani_share_premise = 0 # 8

priya_share_hypothesis = 2
mani_share_hypothesis = 4
rani_share_hypothesis = 8

if priya_share_hypothesis <= priya_share_premise and mani_share_hypothesis <= mani_share_premise and rani_share_hypothesis <= rani_share_premise:
    # all shares are consistent with the premise, no contradiction
    label = "neutral"
elif priya_share_hypothesis > priya_share_premise or mani_share_hypothesis > mani_share_premise or rani_share_hypothesis > rani_share_premise:
    # at least one share contradicts the premise
    label = "contradiction"
else:
    # the premise only gives a ratio, not explicit numbers, so we can't entail anything
    label = "neutral"

print(label)
