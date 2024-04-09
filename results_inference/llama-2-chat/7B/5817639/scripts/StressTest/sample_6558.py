average_premise = 78
average_hypothesis = 78

# the premise and hypothesis refer to the same concept of average score
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the average score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score, any value greater than or equal to the premise value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
