survey_people_premise = 120
survey_people_hypothesis = 100
preference_brand_a_premise = 60

# the hypothesis refers to the number of surveyed people and the percentage of Brand A preferences mentioned in the premise
if survey_people_hypothesis <= survey_people_premise:
    # check if the estimate of'survey_people_hypothesis' contradicts the number of surveyed people in the premise
    label = "contradiction"
elif preference_brand_a_hypothesis!= preference_brand_a_premise:
    # check if the percentage of Brand A preferences in the hypothesis contradicts the percentage of Brand A preferences reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
