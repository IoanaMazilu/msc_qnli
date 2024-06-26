males_premise = 25
males_hypothesis = 45

# the hypothesis refers to the number of males mentioned in the premise
if males_premise <= males_hypothesis:
    # check if the estimate of'males_hypothesis' contradicts the number of males in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males
    # any number of males greater than'males_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
