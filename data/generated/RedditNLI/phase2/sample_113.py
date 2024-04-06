# Premise: Richest 1% To Own More Than Half Worlds Wealth By 2016 Oxfam.
# Hypothesis: Oxfam says richest one percent to own more than rest by 2016.
# Golden Label: entailment

richest_percentage_premise = 1
richest_percentage_hypothesis = 1
wealth_percentage_premise = 50
wealth_percentage_hypothesis = 50

# both the hypothesis and premise mention the 1% richest people and the percentage of wealth they will own
if richest_percentage_premise != richest_percentage_hypothesis:
    # check if the percentage of richest people in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif wealth_percentage_hypothesis != wealth_percentage_premise:
    # check if the estimated wealth percentage in the hypothesis contradicts the premise estimate
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

