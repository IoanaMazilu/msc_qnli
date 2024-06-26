dan_leaving_time_premise = 90
dan_leaving_time_hypothesis = 90

# the hypothesis speaks about the time Dan leaves City A, which is also mentioned in the premise
if dan_leaving_time_hypothesis >= dan_leaving_time_premise:
    # check if the hypothesis value contradicts the premise value of 'dan_leaving_time_premise'
    label = "contradiction"
else:
    # any value less than 'dan_leaving_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
