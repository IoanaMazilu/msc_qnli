miles_per_gallon_premise = 32
miles_per_gallon_hypothesis = 72

# the hypothesis refers to the mileage of Dan's car mentioned in the premise
if miles_per_gallon_premise >= miles_per_gallon_hypothesis:
    # check if the estimate of 'miles_per_gallon_hypothesis' contradicts the number of miles per gallon in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
