average_premise = 60
average_hypothesis = 60

# the hypothesis refers to the number of tests taken by Joe, which is also mentioned in the premise
if average_hypothesis == average_premise:
    # the hypothesis value matches the estimate in the premise, so entailment
    label = "entailment"
elif average_hypothesis > average_premise:
    # the hypothesis value is greater than the estimate in the premise, so contradiction
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests taken by Joe,
    # so any number of tests greater than the estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
