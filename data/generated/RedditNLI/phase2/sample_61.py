# Premise: Trump is pushing 25% auto tariff, despite top advisers scrambling to stop him, sources say.
# Hypothesis: Trump pushes 25 percent auto tariff as top advisers scramble to stop him.
# Golden Label: entailment

tariff_premise = 25
tariff_hypothesis = 25

# the hypothesis and premise mention the percentage of the auto tariff Trump is pushing
if tariff_hypothesis != tariff_premise:
    # check if the tariff percentage in the hypothesis contradicts the tariff percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

