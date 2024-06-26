traveled_miles_premise = 240
traveled_miles_hypothesis = 440

# the hypothesis refers to the number of miles Louisa traveled on the first day of her vacation, which is also mentioned in the premise
if traveled_miles_hypothesis >= traveled_miles_premise:
    # check if the estimate of 'traveled_miles_hypothesis' contradicts the number of miles traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
