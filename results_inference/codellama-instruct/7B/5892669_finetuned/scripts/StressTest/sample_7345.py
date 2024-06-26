price_slump_premise = 68
price_slump_hypothesis = 28

# the hypothesis refers to the price slump mentioned in the premise
if price_slump_hypothesis >= price_slump_premise:
    # check if the 'price_slump_hypothesis' contradicts the premise of slumping less than 'price_slump_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
