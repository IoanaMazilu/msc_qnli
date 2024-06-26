peanuts_box_premise = 4
peanuts_added_premise = 8
peanuts_box_hypothesis = 1
peanuts_added_hypothesis = 8

# the hypothesis refers to the number of peanuts in a box and the number of peanuts added to the box, both mentioned in the premise
if peanuts_box_hypothesis >= peanuts_box_premise:
    # check if the hypothesis value contradicts the number of peanuts in the box in the premise
    label = "contradiction"
elif peanuts_added_hypothesis!= peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
