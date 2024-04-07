# Premise: If in 14 years, John will be one year younger than twice the age of Mark on that day, how old is John today?
# Hypothesis: If in less than 64 years, John will be one year younger than twice the age of Mark on that day, how old is John today?
# Golden Label: entailment

years_future_premise = 14
years_future_hypothesis = 64

# the hypothesis refers to the same situation as the premise, but changes the number of years in the future
if years_future_hypothesis < years_future_premise:
    # check if the number of future years in the hypothesis contradicts the number of future years in the premise
    label = "contradiction"
else:
    # if the number of future years in the hypothesis does not contradict the number of future years in the premise, it can be inferred as entailment
    label = "entailment"

print(label)
