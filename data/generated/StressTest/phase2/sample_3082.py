# Premise: Annie, working alone, can do the same job in just more than 7 hours.
# Hypothesis: Annie, working alone, can do the same job in just 9 hours.
# Golden Label: neutral

work_hours_premise = 7
work_hours_hypothesis = 9

# the hypothesis gives an estimate of the time Annie needs to finish a job, similarly to the premise
if work_hours_hypothesis <= work_hours_premise:
    # check if the hypothesis time contradicts the estimate of just more than 'work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time needed for Annie to finish the job
    # any time longer than 'work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

