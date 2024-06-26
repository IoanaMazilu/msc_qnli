people_survey_premise = 120
people_survey_hypothesis = 520

# the hypothesis talks about the number of people in a survey, referenced also in the premise
if people_survey_hypothesis <= people_survey_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_survey_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the survey
    # any number of people greater than 'people_survey_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
