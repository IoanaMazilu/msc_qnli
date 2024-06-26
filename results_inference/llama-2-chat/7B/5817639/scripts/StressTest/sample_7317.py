stretching_time_premise = 18
stretching_time_hypothesis = 78
catch_up_time_hypothesis = 78

# the hypothesis talks about the time it will take Jim to catch up to Cara, referenced also in the premise
if stretching_time_hypothesis <= stretching_time_premise:
    # check if the hypothesis value contradicts the estimate of less than'stretching_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes Jim to catch up to Cara
    # any time less than'stretching_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
