average_premise = 48
average_hypothesis = 38

# the hypothesis refers to the number of sold cookies and pies mentioned in the premise
if average_hypothesis <= average_premise:
    # check if the estimate of 'average_hypothesis' contradicts the number of sold cookies and pies reported in the premise
    label = "contradiction"
elif average_hypothesis!= average_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
