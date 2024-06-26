kramer_boxes_premise = 10
kramer_boxes_hypothesis = 20

if kramer_boxes_hypothesis >= kramer_boxes_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
