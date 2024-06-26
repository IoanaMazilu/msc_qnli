cleaning_time_premise = 6
cleaning_time_hypothesis = 3

# the hypothesis proposes a specific cleaning time with Anne's speed doubled, referenced also in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cleaning_time_premise'
    label = "contradiction"
else:
    # the premise provides only an upper limit for the cleaning time
    # any cleaning time less than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
