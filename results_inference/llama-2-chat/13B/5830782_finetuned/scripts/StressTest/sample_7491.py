peanuts_in_box_premise = 4
peanuts_added = 8
peanuts_in_box_hypothesis = 1

# the hypothesis refers to the initial number of peanuts in a box and the number added by Mary, as mentioned in the premise
if peanuts_in_box_premise <= peanuts_in_box_hypothesis:
    # check if the initial number of peanuts in the hypothesis contradicts the initial number of peanuts in the premise
    label = "contradiction"
elif peanuts_added!= peanuts_added:
    # check if the number of peanuts added by Mary in the hypothesis contradicts the number of peanuts added by Mary in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
