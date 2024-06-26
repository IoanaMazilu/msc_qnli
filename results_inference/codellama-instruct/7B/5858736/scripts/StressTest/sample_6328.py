kramer_boxes_premise = 20
kramer_boxes_hypothesis = 10

if kramer_boxes_hypothesis >= kramer_boxes_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
