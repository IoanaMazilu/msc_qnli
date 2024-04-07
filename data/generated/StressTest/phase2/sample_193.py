# Premise: Kim can do a work in less than 8 days while David can do the same work in 2 days.
# Hypothesis: Kim can do a work in 3 days while David can do the same work in 2 days.
# Golden Label: neutral

kim_time_premise = 8
kim_time_hypothesis = 3
david_time_premise = 2
david_time_hypothesis = 2

# the hypothesis refers to the time Kim and David can do a work mentioned in the premise
if kim_time_hypothesis >= kim_time_premise:
    # check if the time Kim takes in the hypothesis contradicts the estimate of less than 'kim_time_premise'
    label = "contradiction"
elif david_time_hypothesis != david_time_premise:
    # check if the time David takes in the hypothesis contradicts the time David takes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Kim takes
    # any time less than 'kim_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise. Hence, it's neutral.
    label = "neutral"

print(label)

