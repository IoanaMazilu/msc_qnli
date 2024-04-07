# Premise: Sakshi can do a piece of work in less than 80 days.
# Hypothesis: Sakshi can do a piece of work in 20 days.
# Golden Label: neutral

work_duration_premise = 80
work_duration_hypothesis = 20

# the hypothesis talks about the time Sakshi needs to do a piece of work, referenced also in the premise
if work_duration_hypothesis >= work_duration_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_duration_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the work
    # any duration less than 'work_duration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

