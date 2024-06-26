departure_rate_premise = 70
departure_rate_hypothesis = 40

# the hypothesis refers to the on-time departure rate from Phoenix, mentioned in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the 'departure_rate_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
