cleaning_time_premise = 5
cleaning_time_hypothesis = 3

# The hypothesis refers to the time it would take to clean the house if Anne's speed were doubled, which was also mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cleaning_time_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the cleaning time
    # any cleaning time less than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
