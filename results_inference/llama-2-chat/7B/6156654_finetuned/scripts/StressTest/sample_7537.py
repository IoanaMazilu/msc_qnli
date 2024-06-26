average_score_premise = 50
average_score_hypothesis = 80

# the hypothesis refers to the average score of Reeya in different subjects
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_score_hypothesis > average_score_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # if the hypothesis value is neutral with the premise value
    label = "neutral"

print(label)
