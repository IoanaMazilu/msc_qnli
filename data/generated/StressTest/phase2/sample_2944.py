# Premise: Working independently, Ann can do the same job in more than 7 hours.
# Hypothesis: Working independently, Ann can do the same job in 9 hours.
# Golden Label: neutral

work_hours_premise = 7
work_hours_hypothesis = 9

# the hypothesis refers to the number of hours Ann needs to finish the job, also mentioned in the premise
if work_hours_hypothesis <= work_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

