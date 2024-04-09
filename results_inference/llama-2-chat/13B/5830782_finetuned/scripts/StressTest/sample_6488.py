rainfall_premise = 25
rainfall_hypothesis = 25

# the hypothesis refers to the total rainfall in Springdale mentioned in the premise
if rainfall_hypothesis >= rainfall_premise:
    # check if the hypothesis value contradicts the value of 'rainfall_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
