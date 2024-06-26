percentage_given_back_premise = 2
percentage_given_back_hypothesis = 2

# the hypothesis refers to the percentage given back to Dana's parents, also mentioned in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the percentage in the hypothesis contradicts the percentage specified in the premise
    label = "contradiction"
else:
    # the premise gives an exact percentage for Dana's payback
    # any payback percentage greater than 'percentage_given_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
