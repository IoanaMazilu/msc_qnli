peanuts_in_box_premise = 4
peanuts_added = 8
peanuts_in_box_hypothesis = 7

# the hypothesis refers to the initial number of peanuts in a box, which is also mentioned in the premise
if peanuts_in_box_premise!= peanuts_in_box_hypothesis:
    # check if the initial number of peanuts in the hypothesis contradicts the initial number of peanuts in the premise
    label = "contradiction"
else:
    # if the initial number of peanuts in the hypothesis does not contradict the initial number of peanuts in the premise, we can infer entailment
    label = "entailment"

print(label)
