people_surveyed_premise = 120
people_surveyed_hypothesis = 120
percentage_brand_a_premise = 60
percentage_brand_a_hypothesis = 60

# the hypothesis refers to the number of people surveyed and the percentage who prefer Brand A, mentioned in the premise
if people_surveyed_hypothesis >= people_surveyed_premise:
    # check if the estimate of 'people_surveyed_hypothesis' contradicts the number of people surveyed in the premise
    label = "contradiction"
elif percentage_brand_a_hypothesis!= percentage_brand_a_premise:
    # check if the percentage of people who prefer Brand A in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
