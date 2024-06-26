eggs_per_box_premise = 3.0
eggs_hypothesis = 2.0
boxes_hypothesis = 2.0

# the hypothesis refers to the number of eggs in boxes, which is also mentioned in the premise
# compute the total number of eggs in the hypothesis
total_eggs_hypothesis = eggs_hypothesis * boxes_hypothesis
if eggs_per_box_premise != total_eggs_hypothesis / boxes_hypothesis:
    # check if the number of eggs per box in the hypothesis contradicts the number of eggs per box from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
