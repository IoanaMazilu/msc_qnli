average_increase_premise = 2
average_increase_hypothesis = 6

# the hypothesis refers to the increase in average Jerry wants to achieve, which is also mentioned in the premise
if average_increase_hypothesis <= average_increase_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
