ys_premise: 5
ys_hypothesis: more_than_5

# the hypothesis talks about the number of baseball cards given to John, which is also mentioned in the premise
if ys_hypothesis == ys_premise:
    # check if the hypothesis value is equal to the premise value
    label = "entailment"
else:
    # if the hypothesis value is not equal to the premise value, it contradicts the premise
    label = "contradiction"

print(label)
