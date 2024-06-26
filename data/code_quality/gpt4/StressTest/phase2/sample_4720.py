combinations_premise = 65
combinations_hypothesis = 55

# the hypothesis refers to the number of possible combinations where Michael is not selected, mentioned also in the premise
if combinations_hypothesis >= combinations_premise:
    # check if the number of combinations in the hypothesis contradicts the premise
    label = "contradiction"
elif combinations_hypothesis < combinations_premise:
    # the premise states a maximum number of combinations, while the hypothesis specifies a lesser number
    # this lesser number is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
