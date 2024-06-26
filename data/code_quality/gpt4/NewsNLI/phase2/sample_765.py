linked_cases_premise = 13
linked_cases_hypothesis = 50

# the hypothesis mentions the number of cases linked to Disneyland, which is not referenced in the premise
# the premise mentions the number of cases linked to the outbreak in various states
# the hypothesis number of cases is greater than those reported in the premise
if linked_cases_hypothesis > linked_cases_premise:
    # check if the number of linked cases in the hypothesis contradicts the number of linked cases reported in the premise
    label = "contradiction"
else:
    # if the hypothesis number of cases do not contradict the premise number of cases, we can infer neutrality
    label = "neutral"

print(label)
