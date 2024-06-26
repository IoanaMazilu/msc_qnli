peanuts_premise = 1
peanuts_hypothesis = 4
peanuts_added = 12

# the hypothesis talks about the number of peanuts in a box and the number of peanuts added, both mentioned in the premise
if peanuts_hypothesis <= peanuts_premise:
    # check if the number of peanuts in the hypothesis contradicts the premise
    label = "contradiction"
elif peanuts_added!= peanuts_premise:
    # check if the number of peanuts added in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
