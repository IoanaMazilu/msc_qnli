peanuts_in_box_premise = 4
peanuts_added = 12
peanuts_in_box_hypothesis = 2

# the hypothesis talks about the number of peanuts in a box before and after Mary adds some, referenced also in the premise
if peanuts_in_box_hypothesis!= peanuts_in_box_premise:
    # check if the initial number of peanuts in the box in the hypothesis contradicts the initial number of peanuts in the box in the premise
    label = "contradiction"
else:
    # if the initial number of peanuts in the box does not contradict, we can infer entailment
    label = "entailment"

print(label)
