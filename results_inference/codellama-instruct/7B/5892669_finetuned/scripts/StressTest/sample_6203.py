miles_traveled_premise = 200
miles_traveled_hypothesis = 200

# the hypothesis refers to the miles traveled by Louisa on the first day of her vacation, mentioned in the premise
if miles_traveled_hypothesis >= miles_traveled_premise:
    # check if the hypothesis value contradicts the exact miles traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
