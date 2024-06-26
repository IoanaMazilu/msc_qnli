decrease_premise = 10
decrease_hypothesis = 60

# the hypothesis refers to the percentage of decrease in David's Bank's saving amount, which is also mentioned in the premise
if decrease_hypothesis >= decrease_premise:
    # check if the estimate of 'decrease_hypothesis' contradicts the percentage of decrease in the premise
    label = "contradiction"
elif decrease_hypothesis < decrease_premise:
    # check if the percentage of decrease in the hypothesis is less than the percentage of decrease in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
