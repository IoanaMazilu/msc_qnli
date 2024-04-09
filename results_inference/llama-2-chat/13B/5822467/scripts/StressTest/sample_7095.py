nitin_rank_premise = 15
nitin_rank_hypothesis = 75

# the hypothesis refers to the rank of Nitin in a class of 47 students, as mentioned in the premise
if nitin_rank_hypothesis <= nitin_rank_premise:
    # check if the hypothesis value contradicts the rank of Nitin in the premise
    label = "contradiction"
else:
    # the premise gives a specific rank for Nitin, while the hypothesis gives a more general rank
    # any rank less than 75th is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
