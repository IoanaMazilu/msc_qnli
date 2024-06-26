peanuts_in_box_premise = 4
peanuts_added_premise = 8
peanuts_in_box_hypothesis = 7
peanuts_added_hypothesis = 8

# the hypothesis refers to the number of peanuts in a box and the number of peanuts added, both mentioned in the premise
if peanuts_in_box_premise!= peanuts_in_box_hypothesis:
    # check if the number of peanuts in the box in the hypothesis contradicts the number of peanuts in the box reported in the premise
    label = "contradiction"
elif peanuts_added_premise!= peanuts_added_hypothesis:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
