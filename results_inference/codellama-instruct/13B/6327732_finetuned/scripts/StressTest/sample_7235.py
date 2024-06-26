sisters_premise = 2
sisters_hypothesis = 3

# the hypothesis refers to the number of km each sister runs, which is mentioned in the premise
if sisters_hypothesis <= sisters_premise:
    # check if the estimate of'sisters_hypothesis' contradicts the number of km each sister runs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of km each sister runs
    # any number of km greater than'sisters_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
