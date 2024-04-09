raman_butter_premise = 84
raman_butter_hypothesis = 44
rs_premise = Rs

# the hypothesis refers to the amount of butter mixed and the price mentioned in the premise
if raman_butter_hypothesis <= raman_butter_premise:
    # check if the estimate of 'raman_butter_hypothesis' contradicts the amount of butter mixed in the premise
    label = "contradiction"
elif rs_premise!= rs:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
