percentage_given_back_premise = 3
percentage_given_back_hypothesis = 7

# the hypothesis refers to the percentage given back to Dana's parents, mentioned in the premise
if percentage_given_back_hypothesis < percentage_given_back_premise:
    # check if the percentage in the hypothesis contradicts the percentage given back in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage given back in the premise, we can infer entailment
    label = "entailment"

print(label)
