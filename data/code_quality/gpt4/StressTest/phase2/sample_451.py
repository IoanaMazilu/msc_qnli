life_fraction_premise = 7/7
life_fraction_hypothesis = 1/7

# the hypothesis refers to the fraction of life spent until marriage mentioned in the premise
if life_fraction_hypothesis > life_fraction_premise:
    # check if the fraction of life spent until marriage contradicts the estimate of 'life_fraction_premise'
    label = "contradiction"
elif life_fraction_hypothesis < life_fraction_premise:
    # the premise gives only an estimate for the fraction of life spent until marriage
    # any fraction less than 'life_fraction_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
