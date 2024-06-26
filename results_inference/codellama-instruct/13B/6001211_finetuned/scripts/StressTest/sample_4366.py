hours_premise = 60
hours_hypothesis = 40

# the hypothesis refers to the number of hours of work mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
elif hours_hypothesis < hours_premise:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
