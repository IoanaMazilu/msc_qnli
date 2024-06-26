peanuts_premise = 4
peanuts_hypothesis = 1

# the hypothesis refers to the number of peanuts in a box and the number of additional peanuts Mary puts inside
if peanuts_hypothesis <= peanuts_premise:
    # check if the estimate of 'peanuts_hypothesis' contradicts the number of peanuts in the premise
    label = "contradiction"
elif peanuts_hypothesis!= peanuts_premise + 8:
    # check if the number of additional peanuts in the hypothesis contradicts the number of additional peanuts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
