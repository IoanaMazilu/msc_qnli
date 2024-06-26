cleaning_time_premise = 3
cleaning_time_hypothesis = 8

# the hypothesis refers to the time needed to clean the house if Anne's speed is doubled, a situation also described in the premise
if cleaning_time_hypothesis < cleaning_time_premise:
    # check if the hypothesis value contradicts the 'cleaning_time_premise'
    label = "contradiction"
elif cleaning_time_hypothesis > cleaning_time_premise:
    # check if the hypothesis value is greater than the 'cleaning_time_premise'
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise one, we can infer entailment
    label = "entailment"

print(label)
