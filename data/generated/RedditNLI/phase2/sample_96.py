# Premise: Richest 1% on track to own 50% of all wealth by 2016 Oxfam warns.
# Hypothesis: Richest 1% To Own More Than Half Worlds Wealth By 2016 Oxfam.
# Golden Label: entailment

percentage_premise = 50
percentage_hypothesis = 50

# the hypothesis and premise mention the percentage of wealth that the richest 1% is predicted to own by 2016
if percentage_hypothesis != percentage_premise:
    # check if the percentage of wealth in the hypothesis contradicts the percentage of wealth in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
