suspected_cases_premise = 157
deaths_premise = 101
suspected_cases_hypothesis = 3

# the hypothesis mentions the number of suspected Ebola cases in Mali, which is not referenced in the premise
# the premise refers to the number of suspected cases and deaths in Guinea, which is not mentioned in the hypothesis
# there is no numerical information in the hypothesis that can be compared to the premise
label = "neutral"

print(label)
