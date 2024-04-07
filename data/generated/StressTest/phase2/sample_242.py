# Premise: Bruce and Anne can clean their house in 4 hours working together at their respective constant rates.
# Hypothesis: Bruce and Anne can clean their house in more than 4 hours working together at their respective constant rates.
# Golden Label: contradiction

cleaning_time_premise = 4
cleaning_time_hypothesis = 4

# the hypothesis refers to the cleaning time of Bruce and Anne's house mentioned in the premise
if cleaning_time_hypothesis > cleaning_time_premise:
    # check if the estimate of 'cleaning_time_hypothesis' contradicts the cleaning time in the premise
    label = "contradiction"
elif cleaning_time_hypothesis < cleaning_time_premise:
    # check if the cleaning time in the hypothesis contradicts the cleaning time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

