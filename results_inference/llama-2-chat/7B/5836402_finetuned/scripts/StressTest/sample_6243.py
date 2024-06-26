survey_people_premise = 120
survey_people_hypothesis = 520
preferred_brand_percentage_premise = 60
preferred_brand_percentage_hypothesis = 60

# the hypothesis refers to the number of surveyed people and the percentage of people who preferred Brand A mentioned in the premise
if survey_people_hypothesis >= survey_people_premise:
    # check if the estimate of'survey_people_hypothesis' contradicts the number of surveyed people in the premise
    label = "contradiction"
elif preferred_brand_percentage_hypothesis!= preferred_brand_percentage_premise:
    # check if the percentage of people who preferred Brand A in the hypothesis contradicts the percentage of people who preferred Brand A reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
