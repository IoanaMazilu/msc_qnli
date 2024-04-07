# Premise: Jerry alone cleans the entire house in 6 hours.
# Hypothesis: Jerry alone cleans the entire house in more than 4 hours.
# Golden Label: entailment

cleaning_time_premise = 6
cleaning_time_hypothesis = 4

# the hypothesis refers to the time Jerry cleans the entire house, mentioned in the premise
if cleaning_time_premise < cleaning_time_hypothesis:
    # check if the cleaning time in the premise contradicts the estimate of the cleaning time in the hypothesis
    label = "contradiction"
elif cleaning_time_premise != cleaning_time_hypothesis:
    # check if the cleaning time in the hypothesis contradicts the cleaning time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

