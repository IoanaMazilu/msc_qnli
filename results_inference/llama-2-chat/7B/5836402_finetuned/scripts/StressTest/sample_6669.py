efficient_premise = 25
efficient_hypothesis = 35

# the hypothesis refers to the efficiency difference between Suresh and Kamal mentioned in the premise
if efficient_hypothesis < efficient_premise:
    # check if the hypothesis value contradicts the estimate of more than 'efficient_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
