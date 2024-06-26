distance_traveled_premise = 200
distance_traveled_hypothesis = 200

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation
if distance_traveled_hypothesis == distance_traveled_premise:
    # if the distance traveled in the hypothesis is equal to the distance traveled in the premise, we can infer entailment
    label = "entailment"
elif distance_traveled_hypothesis < distance_traveled_premise:
    # if the distance traveled in the hypothesis is less than the distance traveled in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the distance traveled in the hypothesis is not equal to or less than the distance traveled in the premise, we can infer neutrality
    label = "neutral"

print(label)
