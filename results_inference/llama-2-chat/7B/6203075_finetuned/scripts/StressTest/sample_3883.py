total_hours_premise = 4
total_hours_hypothesis = 3

# the hypothesis refers to the total jogging and walking time mentioned in the premise
if total_hours_hypothesis >= total_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_hours_premise'
    label = "contradiction"
elif total_hours_hypothesis < total_hours_premise:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer neutrality
    label = "neutral"

print(label)
