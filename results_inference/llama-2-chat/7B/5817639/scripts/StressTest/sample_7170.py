problems_premise = 70
problems_hypothesis = 30

# the hypothesis talks about the range of problems solved by Andy in a Math exercise
if problems_hypothesis <= problems_premise:
    # check if the hypothesis value contradicts the estimate of problems solved in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the range of problems solved by Andy, while the hypothesis provides a narrower range
    # any range of problems solved by Andy that is greater than the premise range but not explicitly entailed from the premise is consistent with the premise, so we label it as neutral
    label = "neutral"

print(label)
