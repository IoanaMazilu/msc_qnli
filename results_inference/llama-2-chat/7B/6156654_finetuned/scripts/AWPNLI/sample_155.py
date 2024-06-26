pet_fish_premise = 26.0
pet_fish_buy_premise = 6.0
pet_fish_hypothesis = 27.0

# the hypothesis refers to the number of pet fish, which is also mentioned in the premise
# calculate the difference between the number of pet fish in the premise and the hypothesis
difference = pet_fish_hypothesis - pet_fish_premise

# check if the difference is equal to the number of pet fish bought in the premise
if difference == pet_fish_buy_premise:
    # if the difference is equal to the number of pet fish bought, we can infer entailment
    label = "entailment"
else:
    # if the difference is not equal to the number of pet fish bought, we can infer contradiction
    label = "contradiction"

print(label)
