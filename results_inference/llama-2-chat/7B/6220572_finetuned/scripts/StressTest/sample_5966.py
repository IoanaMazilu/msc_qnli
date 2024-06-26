driving_time_premise = 4
driving_time_hypothesis = 5

# the hypothesis talks about the time taken to drive from City A to City B, referenced also in the premise
if driving_time_hypothesis == driving_time_premise:
    # check if the hypothesis value contradicts the estimate of 'driving_time_premise'
    label = "contradiction"
else:
    # any time greater than 'driving_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
