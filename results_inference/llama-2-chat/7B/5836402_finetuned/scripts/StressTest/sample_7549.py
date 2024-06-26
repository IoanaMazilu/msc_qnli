decrease_percentage_premise = 80
decrease_percentage_hypothesis = 30

# the hypothesis refers to the percentage of decrease in saving amount, which is also mentioned in the premise
if decrease_percentage_hypothesis >= decrease_percentage_premise:
    # check if the estimate of 'decrease_percentage_hypothesis' contradicts the percentage of decrease in the premise
    label = "contradiction"
elif decrease_percentage_hypothesis < decrease_percentage_premise:
    # check if the percentage of decrease in the hypothesis contradicts the percentage of decrease in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
