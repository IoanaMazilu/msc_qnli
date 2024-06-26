percentage_given_premise = 40
percentage_given_hypothesis = 70

# the hypothesis refers to the percentage of money Jones gave to his wife, which is also mentioned in the premise
if percentage_given_hypothesis <= percentage_given_premise:
    # check if the percentage given in hypothesis contradicts the percentage given in premise
    label = "contradiction"
elif percentage_given_hypothesis > percentage_given_premise:
    # the premise gives only a specific percentage of money given
    # any percentage less than 'percentage_given_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
