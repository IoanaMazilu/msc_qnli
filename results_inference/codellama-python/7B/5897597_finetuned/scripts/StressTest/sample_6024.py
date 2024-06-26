percentage_given_back_premise = 4
percentage_given_back_hypothesis = 6

# the hypothesis refers to the percentage of the amount given back each month by Dana, mentioned in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the estimate of 'percentage_given_back_hypothesis' contradicts the percentage given back in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)