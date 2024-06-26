pet_fish_premise = 26.0
pet_fish_hypothesis = 27.0

# compare the number of pet fish in the hypothesis with the number in the premise
if pet_fish_hypothesis >= pet_fish_premise:
    # if the number of pet fish in the hypothesis is greater than or equal to the number in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of pet fish in the hypothesis is less than the number in the premise, we can infer contradiction
    label = "contradiction"

print(label)
