percentage_given_back_premise = 4
percentage_given_back_hypothesis = 6

# the hypothesis refers to the percentage of amount given back to parents mentioned in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the percentage in 'percentage_given_back_hypothesis' contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
