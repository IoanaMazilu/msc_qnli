survey_premise = 120
preference_premise = 60
survey_hypothesis = 520
preference_hypothesis = 60

# the hypothesis refers to the number of people surveyed and the percentage of preferences
if survey_hypothesis < survey_premise:
    # check if the estimate of'survey_hypothesis' contradicts the number of people surveyed in the premise
    label = "contradiction"
elif preference_hypothesis!= preference_premise:
    # check if the percentage of preferences in the hypothesis contradicts the percentage of preferences reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
