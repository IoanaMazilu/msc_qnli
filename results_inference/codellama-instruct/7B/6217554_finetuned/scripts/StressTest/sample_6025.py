percentage_premise = 6
percentage_hypothesis = 4

# the hypothesis talks about the percentage of money Dana gives back each month, referenced also in the premise
if percentage_hypothesis >= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
