quarter_premise = 2010
quarter_hypothesis = 25

# the premise and hypothesis mention the quarter in which the events occur
if quarter_premise!= quarter_hypothesis:
    # check if the quarter in the hypothesis contradicts the quarter in the premise
    label = "contradiction"
elif quarter_hypothesis < quarter_premise:
    # check if the quarter in the hypothesis is before the quarter in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same quarter, so we can infer entailment
    label = "entailment"

print(label)
