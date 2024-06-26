percentage_premise = 5
percentage_hypothesis = 5

# the hypothesis and premise mention the percentage of stolen art that gets returned to the owners
if percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
