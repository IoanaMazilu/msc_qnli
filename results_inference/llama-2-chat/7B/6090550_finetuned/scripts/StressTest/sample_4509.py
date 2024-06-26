total_hours_premise = 41
total_hours_hypothesis = 11

# the hypothesis refers to the total number of hours worked by James, which is also mentioned in the premise
if total_hours_hypothesis >= total_hours_premise:
    # check if the hypothesis value contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
