survey_size_premise = 120
survey_size_hypothesis = 120
preference_brand_a_premise = 0.6
preference_brand_a_hypothesis = 0.6

# the hypothesis refers to a survey of less than 120 people, which is consistent with the premise
if survey_size_hypothesis >= survey_size_premise:
    # check if the hypothesis value contradicts the preference for Brand A in the premise
    if preference_brand_a_hypothesis!= preference_brand_a_premise:
        label = "contradiction"
    else:
        label = "neutral"
else:
    # the hypothesis value contradicts the premise
    label = "contradiction"

print(label)
