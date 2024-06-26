average_premise = 90
average_hypothesis = 90

# the hypothesis refers to the average score of Jerry on the first 3 of 4 tests, which is consistent with the premise
if average_hypothesis == average_premise:
    # the hypothesis value is equal to the premise value, entailment
    label = "entailment"
elif average_hypothesis > average_premise:
    # the hypothesis value is greater than the premise value, contradiction
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, it is neutral
    label = "neutral"

print(label)
