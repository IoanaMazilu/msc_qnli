# Premise: Saudi Arabia could be bankrupt within 5 years, IMF predicts.
# Hypothesis: Saudi Arabia could be bankrupt by 2020 IMF.
# Golden Label: entailment

years_premise = 5
year_hypothesis = 2020
current_year = 2021  # We should adjust this based on the current year

# the hypothesis and premise mention a prediction of when Saudi Arabia could be bankrupt
if year_hypothesis != current_year + years_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

