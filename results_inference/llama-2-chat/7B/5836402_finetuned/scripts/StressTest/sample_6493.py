percentage_given_back_premise = 7
percentage_given_back_hypothesis = 3

# the hypothesis refers to the percentage given back to parents, which is also mentioned in the premise
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the percentage given back in the hypothesis contradicts the percentage given back in the premise
    label = "contradiction"
else:
    # if the percentage given back in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
