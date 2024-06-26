percentage_premise = 50
percentage_hypothesis = 50

# the hypothesis and premise mention the percentage of the population owned by the richest people
if percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis is the same as the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
