percentage_given_premise = 4
percentage_given_hypothesis = 6

# the hypothesis refers to the percentage given back to parents, which is also mentioned in the premise
if percentage_given_hypothesis < percentage_given_premise:
    # check if the percentage given in the hypothesis contradicts the percentage given in the premise
    label = "contradiction"
else:
    # if the percentage given in the hypothesis does not contradict the percentage given in the premise, we can infer entailment
    label = "entailment"

print(label)
