decrease_premise = 70
decrease_hypothesis = 20

# the hypothesis refers to the decrease in John's Bank's saving amount mentioned in the premise
if decrease_hypothesis >= decrease_premise:
    # check if the decrease in the hypothesis contradicts the estimate of less than 'decrease_premise'
    label = "contradiction"
elif decrease_hypothesis < decrease_premise:
    # check if the decrease in the hypothesis is less than the decrease in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
