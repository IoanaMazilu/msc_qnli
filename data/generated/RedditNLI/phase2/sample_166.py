# Premise: China economic growth slowest in 25 years.
# Hypothesis: China' s economy shows slowest growth in 25 years.
# Golden Label: entailment

years_premise = 25
years_hypothesis = 25

# the hypothesis and premise mention the number of years for which the economic growth of China is the slowest
if years_hypothesis != years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

