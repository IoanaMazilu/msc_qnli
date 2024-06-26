percentage_given_back_premise = 4
percentage_given_back_hypothesis = 6

# the hypothesis refers to the percentage of amount given back to parents each month, mentioned in the premise
if percentage_given_back_hypothesis < percentage_given_back_premise:
    # check if the percentage of amount given back in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
