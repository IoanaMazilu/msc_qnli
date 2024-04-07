# Premise: If it takes Pat less than 30 minutes to stretch and Cara continues to run during this time, how many minutes will it take Pat to catch up to Cara?
# Hypothesis: If it takes Pat 20 minutes to stretch and Cara continues to run during this time, how many minutes will it take Pat to catch up to Cara?
# Golden Label: neutral

stretch_time_premise = 30
stretch_time_hypothesis = 20

# the hypothesis specifies the time it takes Pat to stretch, which is less than the time given in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the specific stretch time in the hypothesis contradicts the estimate of less than 'stretch_time_premise'
    label = "contradiction"
elif stretch_time_hypothesis < stretch_time_premise:
    # the premise gives only an estimate for the stretch time
    # a specific stretch time less than 'stretch_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

