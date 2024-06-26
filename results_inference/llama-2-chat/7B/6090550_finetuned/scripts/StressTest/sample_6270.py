participants_premise = 7
participants_hypothesis = 8

# the hypothesis refers to the number of participants in a cycling race mentioned in the premise
if participants_hypothesis <= participants_premise:
    # check if the hypothesis value contradicts the exact number of participants in the premise
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise, it contradicts the premise
    label = "contradiction"

print(label)
