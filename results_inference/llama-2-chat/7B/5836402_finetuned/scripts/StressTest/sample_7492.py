peanuts_in_box_premise = 1
peanuts_in_box_hypothesis = 4
peanuts_added_premise = 8
peanuts_added_hypothesis = 8

# the hypothesis refers to the number of peanuts in a box and the number of peanuts added, both mentioned in the premise
if peanuts_in_box_hypothesis <= peanuts_in_box_premise:
    # check if the hypothesis value contradicts the estimate of more than 'peanuts_in_box_premise'
    label = "contradiction"
elif peanuts_added_hypothesis!= peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
