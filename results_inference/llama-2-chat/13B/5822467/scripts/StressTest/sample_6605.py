investment_premise = 2 * n
investment_hypothesis = n * 2

# the hypothesis refers to the amount of investment returned at the end of 'n' years
if investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the amount of investment returned in the premise
    label = "contradiction"
elif investment_premise!= investment_hypothesis:
    # check if the amount of investment returned in the hypothesis contradicts the amount of investment returned in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
