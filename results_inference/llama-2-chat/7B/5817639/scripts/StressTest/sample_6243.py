preference_survey_premise = 120
prefrence_survey_hypothesis = 520

# the hypothesis refers to the number of people surveyed in the premise
if preference_survey_hypothesis <= preference_survey_premise:
    # check if the estimate of 'prefrence_survey_hypothesis' contradicts the number of people surveyed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people surveyed
    # any number of people surveyed greater than 'prefrence_survey_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
