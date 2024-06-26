percentage_given_back_premise = 4
percentage_given_back_hypothesis = 6

# the hypothesis refers to the percentage of the amount Dana gives back to her parents each month, mentioned in the premise
if percentage_given_back_premise >= percentage_given_back_hypothesis:
    # check if the estimate of 'percentage_given_back_hypothesis' contradicts the percentage given back in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
