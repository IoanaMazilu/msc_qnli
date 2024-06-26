survey_people_premise = 110
survey_people_hypothesis = 810
preferred_brand_premise = 60
preferred_brand_hypothesis = 60

# the premise and hypothesis talk about the number of people surveyed and the percentage who preferred Brand A
if survey_people_hypothesis < survey_people_premise:
    # check if the number of people surveyed in the hypothesis contradicts the number of people surveyed in the premise
    label = "contradiction"
elif preferred_brand_hypothesis != preferred_brand_premise:
    # check if the percentage of people who preferred the brand in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
