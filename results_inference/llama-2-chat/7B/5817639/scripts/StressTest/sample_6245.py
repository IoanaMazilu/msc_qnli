preference_survey_premise = 120
preference_survey_hypothesis = 120

# the hypothesis talks about the number of people in the town of Angie, and the preference of a brand among them
if preference_survey_hypothesis <= preference_survey_premise:
    # check if the hypothesis value contradicts the estimate of more than 'preference_survey_premise' people in the town of Angie
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the town of Angie
    # any number of people greater than 'preference_survey_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
