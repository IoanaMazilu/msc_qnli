hours_paid_x_premise = 30
hours_paid_x_hypothesis = 30

# the hypothesis refers to the hours of work paid with x dollars, mentioned also in the premise
if hours_paid_x_hypothesis >= hours_paid_x_premise:
    # check if the hypothesis value contradicts the premise value of 'hours_paid_x_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
