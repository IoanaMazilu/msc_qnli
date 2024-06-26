investment_premise = 2 * n
investment_hypothesis = n * 3

# the hypothesis refers to the amount of investment returned, which is mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of 'investment_premise'
    label = "contradiction"
elif investment_premise!= investment_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'investment_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
