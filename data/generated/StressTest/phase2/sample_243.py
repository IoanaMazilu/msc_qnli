# Premise: If Anne’s speed were doubled, they could clean their house in 3 hours working at their respective rates.
# Hypothesis: If Anne’s speed were doubled, they could clean their house in more than 1 hours working at their respective rates.
# Golden Label: entailment

cleaning_time_premise = 3
cleaning_time_hypothesis = 1

# the hypothesis refers to the time needed to clean the house if Anne's speed were doubled, which is also the case in the premise
if cleaning_time_premise < cleaning_time_hypothesis:
    # check if the estimate of 'cleaning_time_premise' contradicts with the hypothesis that it would take more than 'cleaning_time_hypothesis' hours
    label = "contradiction"
elif cleaning_time_premise == cleaning_time_hypothesis:
    # check if the time in the hypothesis is the same as the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

