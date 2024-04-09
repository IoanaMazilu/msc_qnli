# Define variables for the numerical entities in the premise and hypothesis
mark_boxes_premise = n - 6
ann_boxes_premise = n - 2

# Define variables for the numerical entities in the hypothesis
mark_boxes_hypothesis = mark_boxes_premise - 6
ann_boxes_hypothesis = ann_boxes_premise - 2

# Check if the hypothesis values contradict the premise values
if mark_boxes_hypothesis < mark_boxes_premise and ann_boxes_hypothesis < ann_boxes_premise:
    # Both Mark and Ann sold less than their respective estimates in the premise
    label = "entailment"
elif mark_boxes_hypothesis > mark_boxes_premise or ann_boxes_hypothesis > ann_boxes_premise:
    # At least one of Mark or Ann sold more than their respective estimates in the premise
    label = "contradiction"
else:
    # The hypothesis values are consistent with the premise values, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
