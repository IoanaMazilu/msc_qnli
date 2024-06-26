fruit_dinner_premise = 460
fruit_dinner_hypothesis = 360

# the hypothesis talks about the amount of fruit Sue ate for dinner, referenced also in the premise
if fruit_dinner_hypothesis > fruit_dinner_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'fruit_dinner_premise'
    label = "contradiction"
elif fruit_dinner_hypothesis < fruit_dinner_premise:
    # the premise gives only an estimate for the amount of fruit eaten for dinner
    # any amount of fruit less than 'fruit_dinner_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
