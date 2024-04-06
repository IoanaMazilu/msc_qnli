# Premise: Australia, which has had no confirmed cases, was investigating 114.
# Hypothesis: Largest outbreak was in Mexico which had 156 confirmed cases.
# Golden Label: neutral

cases_australia_premise = 0
cases_investigated_australia_premise = 114
cases_mexico_hypothesis = 156

# the hypothesis mentions the number of confirmed cases in Mexico, which is not referenced in the premise
# the premise mentions the number of confirmed and investigated cases in Australia, which is not referenced in the hypothesis
# there is no numerical information that can be compared between the premise and the hypothesis
label = "neutral"

print(label)

