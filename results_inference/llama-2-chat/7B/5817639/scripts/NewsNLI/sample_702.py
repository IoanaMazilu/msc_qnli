enemy_premise = 0.69
enemy_hypothesis = 0.12

# compare the percentage of people with a positive view of the United States in the hypothesis to the percentage in the premise
if enemy_hypothesis!= enemy_premise:
    # if the percentage in the hypothesis is less than the percentage in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the percentage in the hypothesis is equal to or greater than the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
