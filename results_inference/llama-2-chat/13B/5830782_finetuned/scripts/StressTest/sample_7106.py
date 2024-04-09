hours_premise = 30
hours_hypothesis = 30

# the hypothesis refers to the number of hours Harry is paid x dollars per hour, mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_premise'
    label = "contradiction"
elif hours_hypothesis < hours_premise:
    # the premise gives the exact number of hours
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
