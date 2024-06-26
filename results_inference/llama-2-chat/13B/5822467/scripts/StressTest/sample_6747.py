butter_premise = 44
butter_hypothesis = 84
rs_premise = Rs

# the hypothesis refers to the amount of butter mixed and the price mentioned in the premise
if butter_hypothesis <= butter_premise:
    # check if the estimate of 'butter_hypothesis' contradicts the amount of butter mixed in the premise
    label = "contradiction"
elif rs_premise!= rs:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
