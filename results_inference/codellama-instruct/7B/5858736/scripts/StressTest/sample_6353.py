profit_premise = 22000
profit_hypothesis = 22000

# the hypothesis refers to the number of sold cookies and pies mentioned in the premise
if profit_premise <= profit_hypothesis:
    # check if the estimate of 'profit_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
