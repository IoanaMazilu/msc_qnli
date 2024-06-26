percentage_premise = 6
percentage_hypothesis = 4

# the hypothesis refers to the percentage of the amount Dana gives back to her parents, also mentioned in the premise
if percentage_hypothesis >= percentage_premise:
    # check if the percentage in the hypothesis contradicts the premise, which mentions 'less than 6%'
    label = "contradiction"
elif percentage_hypothesis < percentage_premise:
    # if the percentage in the hypothesis is less than the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
