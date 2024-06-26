traveled_miles_premise = 440
traveled_miles_hypothesis = 240

# the hypothesis refers to the number of miles Louisa traveled on the first day of her vacation, mentioned in the premise
if traveled_miles_hypothesis >= traveled_miles_premise:
    # check if the estimate of 'traveled_miles_hypothesis' contradicts the number of miles Louisa traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)