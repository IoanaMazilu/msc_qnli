father_age_multiplier = 2
years_future = 10
hypothesis_years_future = 80

# the hypothesis refers to the same situation as the premise, but with a different estimate for the future
if years_future > hypothesis_years_future:
    # check if the hypothesis estimate contradicts the premise one
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
