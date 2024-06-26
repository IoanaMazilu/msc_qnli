commute_time_premise = 55
commute_time_hypothesis = 15

# the hypothesis refers to the difference in commute time between walking and train, mentioned in the premise
if commute_time_hypothesis >= commute_time_premise:
    # check if the hypothesis value contradicts the premise value of less than 'commute_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in commute time
    # any difference less than 'commute_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
