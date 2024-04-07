# Premise: John alone cleans the entire house in more than 1 hours.
# Hypothesis: John alone cleans the entire house in 6 hours.
# Golden Label: neutral

cleaning_time_premise = 1
cleaning_time_hypothesis = 6

# the hypothesis talks about the time John takes to clean the house, which is also referenced in the premise
if cleaning_time_hypothesis <= cleaning_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cleaning_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the cleaning time
    # any cleaning time greater than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

