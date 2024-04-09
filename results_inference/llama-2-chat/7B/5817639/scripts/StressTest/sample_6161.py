height_premise = 356
height_hypothesis = 370

# the hypothesis talks about the height difference between two buildings, referenced also in the premise
if height_hypothesis <= height_premise:
    # check if the hypothesis value contradicts the estimate of the height difference in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the height difference, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
