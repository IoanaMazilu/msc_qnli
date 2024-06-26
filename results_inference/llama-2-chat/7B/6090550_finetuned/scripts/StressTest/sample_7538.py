average_score_premise = 40 + 60 + 70 + 80 + 80
average_score_hypothesis = 40 + 60 + 70 + 80 + 80

# the hypothesis refers to the scores obtained by Reeya in different subjects, as mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_score_hypothesis < average_score_premise:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
