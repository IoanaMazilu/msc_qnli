peanuts_box_premise = 1
peanuts_added_premise = 12
peanuts_box_hypothesis = 4
peanuts_added_hypothesis = 12

# the hypothesis refers to the number of peanuts in a box and the number of peanuts added, both mentioned in the premise
if peanuts_box_hypothesis <= peanuts_box_premise:
    # check if the initial number of peanuts in the box in the hypothesis contradicts the premise
    label = "contradiction"
elif peanuts_added_hypothesis!= peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the initial number of peanuts in the box
    # any number of peanuts greater than 'peanuts_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
