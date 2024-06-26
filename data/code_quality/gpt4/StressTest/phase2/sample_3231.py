gloves_premise = 20
gloves_hypothesis = 30

# the hypothesis refers to the number of matched gloves Andy has, which is also mentioned in the premise
if gloves_hypothesis <= gloves_premise:
    # check if the estimate of 'gloves_hypothesis' contradicts the number of gloves in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of gloves, which is less than the number in the hypothesis
    # thus, the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
