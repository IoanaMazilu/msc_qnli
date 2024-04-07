# Premise: Tom alone cleans the entire house in 6 hours.
# Hypothesis: Tom alone cleans the entire house in more than 2 hours.
# Golden Label: entailment

cleaning_time_premise = 6
cleaning_time_hypothesis = 2

# the hypothesis refers to the time Tom takes to clean the house, which is also mentioned in the premise
if cleaning_time_premise < cleaning_time_hypothesis:
    # check if the cleaning time in the premise contradicts the estimate of more than 'cleaning_time_hypothesis'
    label = "contradiction"
elif cleaning_time_premise == cleaning_time_hypothesis:
    # check if the cleaning time in the premise contradicts the estimate of more than 'cleaning_time_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

