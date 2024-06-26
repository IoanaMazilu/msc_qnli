profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit in the business at the end of the year, mentioned in the premise
if profit_premise <= profit_hypothesis:
    # check if the estimate of 'profit_hypothesis' contradicts the profit in the premise
    label = "contradiction"
elif profit_hypothesis - profit_premise!= 0:
    # check if the difference between the hypothesis and the premise contradicts the profit in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
