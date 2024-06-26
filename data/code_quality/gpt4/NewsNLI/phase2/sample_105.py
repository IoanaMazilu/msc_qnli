deaths_serbia_premise = 15
deaths_bosnia_premise = 5
total_deaths_premise = deaths_serbia_premise + deaths_bosnia_premise

total_deaths_hypothesis = 20

# the hypothesis mentions the total number of deaths in Serbia and Bosnia-Herzegovina, which is also referenced in the premise
if total_deaths_hypothesis != total_deaths_premise:
    # check if the total number of deaths in the hypothesis contradicts the total number of deaths reported in the premise
    label = "contradiction"
else:
    # if the total number of deaths in the hypothesis does not contradict the total number of deaths in the premise, we can infer entailment
    label = "entailment"

print(label)
