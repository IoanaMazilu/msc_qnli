# Premise: If it takes Pat less than 75 minutes to stretch and Cathy continues to run during this time, how many minutes will it take Pat to catch up to Cathy?
# Hypothesis: If it takes Pat 15 minutes to stretch and Cathy continues to run during this time, how many minutes will it take Pat to catch up to Cathy?
# Golden Label: neutral

stretch_time_premise = 75
stretch_time_hypothesis = 15

# the premise and hypothesis both talk about the time it takes for Pat to stretch
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the stretch time in hypothesis contradicts the premise's estimate of less than 'stretch_time_premise'
    label = "contradiction"
elif stretch_time_hypothesis < stretch_time_premise:
    # check if the stretch time in hypothesis is less than 'stretch_time_premise' as stated in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the stretch time
    # any stretch time less than 'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

