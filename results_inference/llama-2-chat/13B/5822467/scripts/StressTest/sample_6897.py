# Define variables for numerical entities in the premise and hypothesis
mark_boxes_premise = n - 7
ann_boxes_premise = n - 2
mark_boxes_hypothesis = n - 6
ann_boxes_hypothesis = n - 2

# Check if Mark's sold boxes contradict the premise
if mark_boxes_hypothesis < mark_boxes_premise:
    # Mark's sold boxes contradict the premise, label as contradiction
    label = "contradiction"
elif ann_boxes_hypothesis < ann_boxes_premise:
    # Ann's sold boxes contradict the premise, label as contradiction
    label = "contradiction"
else:
    # If both Mark and Ann's sold boxes do not contradict the premise, we can infer neutrality
    label = "neutral"

print(label)
