percentage_given_back_premise = 3
percentage_given_back_hypothesis = 7

# the hypothesis refers to the percentage of the amount given back each month by Dana, mentioned in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
