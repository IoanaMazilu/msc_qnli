percentage_given_back_premise = 4
percentage_given_back_hypothesis = 6

# the hypothesis refers to the percentage of the amount given back to Dana's parents, mentioned in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
