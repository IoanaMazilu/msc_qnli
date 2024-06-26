eb_height_premise = 356
pt_height_premise = 370

# the hypothesis talks about the height difference between the two buildings
eb_height_hypothesis = -370
pt_height_hypothesis = -356

# first, check if the hypothesis values contradict the premise values
if eb_height_hypothesis > pt_height_premise or pt_height_hypothesis > eb_height_premise:
    # the hypothesis values contradict the premise values, so the label is contradiction
    label = "contradiction"
elif eb_height_hypothesis == pt_height_premise or pt_height_hypothesis == eb_height_premise:
    # the hypothesis values are consistent with the premise values, so the label is neutral
    label = "neutral"
else:
    # the hypothesis values do not contradict the premise values, so the label is entailment
    label = "entailment"

print(label)
