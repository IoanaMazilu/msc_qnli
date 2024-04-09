marks_reema_premise = 86
marks_reema_hypothesis = 36

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if marks_reema_hypothesis >= marks_reema_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_reema_premise'
    label = "contradiction"
elif marks_reema_hypothesis < marks_reema_premise:
    # if the hypothesis value is less than the premise one, it can be explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
