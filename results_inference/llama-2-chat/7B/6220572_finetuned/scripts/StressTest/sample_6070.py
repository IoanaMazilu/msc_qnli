days_premise = 15
days_hypothesis = 15

# the hypothesis refers to the number of days the builder takes to build, also referenced in the premise
if days_hypothesis == days_premise:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
