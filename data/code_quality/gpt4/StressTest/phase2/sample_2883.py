average_raise_premise = 2
average_raise_hypothesis = 1

# the hypothesis refers to the points Jerry wants to raise his average by, mentioned in the premise
if average_raise_premise <= average_raise_hypothesis:
    # check if the hypothesis value contradicts the number of points Jerry wants to raise his average by in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)
