peanuts_in_box_premise = 4
peanuts_added = 8
peanuts_in_box_hypothesis = 1

# the hypothesis refers to the initial number of peanuts in the box, which is also mentioned in the premise
if peanuts_in_box_premise <= peanuts_in_box_hypothesis:
    # check if the initial number of peanuts in the box according to the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the initial number of peanuts does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
