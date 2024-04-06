# Premise: Census shows 1 in 2 people in U.S. are poor or low-income.
# Hypothesis: Census: 1 In 2 Americans Is Poor Or Low-Income.
# Golden Label: entailment

ratio_poor_low_income_premise = 1/2
ratio_poor_low_income_hypothesis = 1/2

# the hypothesis and premise mention the ratio of people in the U.S. that are poor or low-income
if ratio_poor_low_income_hypothesis != ratio_poor_low_income_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

