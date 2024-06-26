hours_dan_premise = 3
hours_dan_hypothesis = 4

# the hypothesis refers to the number of hours Dan works alone, which is also mentioned in the premise
if hours_dan_hypothesis!= hours_dan_premise:
    # check if the number of hours Dan works in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same number of hours Dan works alone
    # any number of hours Annie works alone to complete the job is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
