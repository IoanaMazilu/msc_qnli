deir_ezzor_cases_premise = 15
additional_cases_premise = 2
total_cases_hypothesis = 17

# the hypothesis mentions the total number of confirmed cases, which is the sum of the numbers mentioned in the premise
if deir_ezzor_cases_premise + additional_cases_premise != total_cases_hypothesis:
    # check if the total number of cases from the hypothesis contradicts the sum of cases in the premise
    label = "contradiction"
else:
    # if the total number of cases in the hypothesis does not contradict the sum of cases in the premise, we can infer entailment
    label = "entailment"

print(label)
