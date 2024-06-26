percentage_given_back_premise = 3
percentage_given_back_hypothesis = 7

# the hypothesis refers to the percentage of the amount given back to Dana's parents each month
if percentage_given_back_premise >= percentage_given_back_hypothesis:
    # check if the estimate of 'percentage_given_back_premise' contradicts the percentage in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
