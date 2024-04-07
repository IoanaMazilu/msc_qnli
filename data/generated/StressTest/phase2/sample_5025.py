# Premise: If the average falls 1 second after Izzy finishes another sprint, how many seconds did it take Izzy to run the most recent sprint?
# Hypothesis: If the average falls less than 6 second after Izzy finishes another sprint, how many seconds did it take Izzy to run the most recent sprint?
# Golden Label: entailment

avg_fall_premise = 1
avg_fall_hypothesis = 6

# the hypothesis refers to the time it takes for the average to fall after Izzy finishes a sprint
if avg_fall_hypothesis < avg_fall_premise:
    # check if the time it takes for the average to fall in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif avg_fall_hypothesis > avg_fall_premise:
    # the premise gives only an estimate for the time it takes for the average to fall
    # any time less than 'avg_fall_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

