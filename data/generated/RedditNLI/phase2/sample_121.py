# Premise: Wages Salaries jump by 3.1 percent; highest in decade.
# Hypothesis: Wages and salaries jump by 3.1%, highest level in a decade.
# Golden Label: entailment

percentage_premise = 3.1
percentage_hypothesis = 3.1

# the hypothesis and premise mention the same percentage increase in wages and salaries
if percentage_hypothesis != percentage_premise:
    # check if the percentage increase in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
else:
    # if the percentage increase in the hypothesis does not contradict the percentage increase in the premise, we can infer entailment
    label = "entailment"

print(label)

