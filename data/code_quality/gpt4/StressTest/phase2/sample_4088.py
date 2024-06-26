salary_decrease_premise = 0.5
salary_increase_premise = 0.5
salary_decrease_hypothesis = 0.4
salary_increase_hypothesis = 0.5

# the hypothesis and premise refer to the same event of Paul's salary decrease and increase
if salary_decrease_hypothesis != salary_decrease_premise or salary_increase_hypothesis != salary_increase_premise:
    # check if the hypothesis contradicts the premise directly
    label = "contradiction"
else:
    # if the hypothesis and premise are identical, we can infer entailment
    label = "entailment"

print(label)
