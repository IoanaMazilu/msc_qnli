# Premise: Jerry alone cleans the entire house in more than 4 hours.
# Hypothesis: Jerry alone cleans the entire house in 6 hours.
# Golden Label: neutral

cleaning_time_premise = 4
cleaning_time_hypothesis = 6

# the hypothesis refers to the time Jerry takes to clean the house as mentioned in the premise
if cleaning_time_hypothesis <= cleaning_time_premise:
    # check if the 'cleaning_time_hypothesis' contradicts the premise's estimate of more than 'cleaning_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the cleaning time
    # any cleaning time greater than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

