peanuts_box_premise = 1
peanuts_added_premise = 8
peanuts_box_hypothesis = 4
peanuts_added_hypothesis = 8

# the hypothesis talks about the number of peanuts in a box and how many are added, referenced also in the premise
if peanuts_box_hypothesis <= peanuts_box_premise or peanuts_added_hypothesis != peanuts_added_premise:
    # check if the hypothesis values contradict the estimates in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts in the box
    # any number of peanuts greater than 'peanuts_box_premise' and equal peanuts added is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
