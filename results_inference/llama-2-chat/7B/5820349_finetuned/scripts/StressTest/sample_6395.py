oil_premise = 8
oil_hypothesis = 8

# the hypothesis refers to the amount of oil needed for each cylinder of George's car, which is also mentioned in the premise
if oil_hypothesis >= oil_premise:
    # check if the hypothesis value contradicts the exact amount of 'oil_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
