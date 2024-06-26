corn_dinner_premise = 200
corn_dinner_hypothesis = 300

# the hypothesis refers to the amount of corn Sandy ate for dinner, mentioned in the premise
if corn_dinner_hypothesis >= corn_dinner_premise:
    # check if the estimate of 'corn_dinner_hypothesis' contradicts the amount of corn eaten for dinner in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment as the rest of the information remains the same
    label = "entailment"

print(label)
