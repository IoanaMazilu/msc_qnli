# Premise: If in 12 years, John will be one year younger than twice the age of Mark on that day, how old is Mark today?
# Hypothesis: If in less than 22 years, John will be one year younger than twice the age of Mark on that day, how old is Mark today?
# Golden Label: entailment

years_premise = 12
years_hypothesis = 22

# the hypothesis talks about the same situation as the premise but in a different number of years
if years_hypothesis >= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis are discussing the same situation, but the hypothesis refers to a greater number of years
    label = "neutral"

print(label)

