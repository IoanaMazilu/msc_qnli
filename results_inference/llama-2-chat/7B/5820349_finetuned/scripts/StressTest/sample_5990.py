mileage_premise = 32
mileage_hypothesis = 82

# the hypothesis refers to the mileage of Dan's car mentioned in the premise
if mileage_hypothesis!= mileage_premise:
    # check if the mileage in the hypothesis contradicts the mileage reported in the premise
    label = "contradiction"
else:
    # if the mileage in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
