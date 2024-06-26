percentage_decrease_hypothesis = 60
percentage_decrease_premise = 10

if percentage_decrease_hypothesis > percentage_decrease_premise:
    # check if the percentage of saving amount decrease in the hypothesis contradicts the percentage of saving amount decrease in the premise
    label = "contradiction"
elif percentage_decrease_hypothesis < percentage_decrease_premise:
    # check if the percentage of saving amount decrease in the hypothesis is consistent with the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
