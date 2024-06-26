peanuts_box_premise = 4
peanuts_box_hypothesis = 2

# the hypothesis refers to the number of peanuts in a box, which is also mentioned in the premise
if peanuts_box_hypothesis!= peanuts_box_premise:
    # check if the number of peanuts in the hypothesis contradicts the number of peanuts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
