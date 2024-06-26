cleaning_time_premise = 3
cleaning_time_hypothesis = 5

# the hypothesis refers to the cleaning time if Anne's speed were doubled, also mentioned in the premise
if cleaning_time_hypothesis < cleaning_time_premise:
    # check if the hypothesis value contradicts the cleaning time in the premise
    label = "contradiction"
elif cleaning_time_hypothesis == cleaning_time_premise:
    # check if the hypothesis value is equal to the cleaning time in the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict or is not equal to the premise value, we can infer neutrality
    label = "neutral"

print(label)
