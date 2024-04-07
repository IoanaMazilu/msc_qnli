# Premise: If the average falls 1 second after Izzy finishes another sprint, how many seconds did it take Izzy to run the most recent sprint?
# Hypothesis: If the average falls less than 1 second after Izzy finishes another sprint, how many seconds did it take Izzy to run the most recent sprint?
# Golden Label: contradiction

average_fall_premise = 1
average_fall_hypothesis = 1

# the hypothesis talks about the average time it takes Izzy to finish a sprint, referenced also in the premise
if average_fall_hypothesis < average_fall_premise:
    # check if the hypothesis value contradicts the estimate of exactly 'average_fall_premise'
    label = "contradiction"
elif average_fall_hypothesis == average_fall_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the average fall time
    # any average fall time greater than 'average_fall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

