decrease_percentage_premise = 30
decrease_percentage_hypothesis = 20

# the hypothesis refers to the percentage of decrease in saving amount mentioned in the premise
if decrease_percentage_hypothesis!= decrease_percentage_premise:
    # check if the percentage of decrease in the hypothesis contradicts the percentage of decrease reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
