suspected_cases_premise = 157
deaths_premise = 101
suspected_cases_hypothesis = 3

# the hypothesis mentions the number of suspected Ebola cases in Mali, which is not referenced in the premise
# the premise provides information about the number of suspected cases and deaths in Guinea
# the hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise either
label = "neutral"

print(label)
