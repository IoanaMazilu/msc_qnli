peanuts_box_premise = 4
peanuts_box_hypothesis = 1
additional_peanuts = 8

# the hypothesis refers to the initial number of peanuts in the box and the action of adding more peanuts, both mentioned in the premise
if peanuts_box_premise <= peanuts_box_hypothesis:
    # check if the initial number of peanuts in the hypothesis contradicts the initial number of peanuts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
