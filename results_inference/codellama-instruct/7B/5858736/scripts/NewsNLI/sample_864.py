suspected_cases_premise = 157
suspected_cases_hypothesis = 3
deaths_premise = 101
deaths_hypothesis = 0

if suspected_cases_hypothesis > suspected_cases_premise:
    # check if the number of suspected cases in the hypothesis exceeds the number of suspected cases in the premise
    label = "entailment"
elif deaths_hypothesis > deaths_premise:
    # check if the number of deaths in the hypothesis exceeds the number of deaths in the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
