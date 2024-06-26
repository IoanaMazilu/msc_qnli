survey_size_premise = 120
survey_size_hypothesis = 120
preference_brand_a_premise = 0.6
preference_brand_a_hypothesis = 0.6

# the hypothesis refers to the number of people surveyed and the percentage of preference for Brand A
if survey_size_hypothesis >= survey_size_premise:
    # check if the hypothesis value contradicts the number of people surveyed in the premise
    label = "contradiction"
elif preference_brand_a_hypothesis!= preference_brand_a_premise:
    # check if the percentage of preference for Brand A in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
