# Premise: Aamir saves 32% of his monthly salary.
# Hypothesis: Aamir saves 22% of his monthly salary.
# Golden Label: contradiction

salary_savings_premise = 32
salary_savings_hypothesis = 22

# the hypothesis refers to the percentage of salary Aamir saves, mentioned in the premise
if salary_savings_hypothesis != salary_savings_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

