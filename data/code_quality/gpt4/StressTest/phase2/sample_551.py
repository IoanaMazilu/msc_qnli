salary_savings_premise = 32
salary_savings_hypothesis = 42

# the hypothesis refers to the percentage of salary Aamir saves, mentioned in the premise
if salary_savings_hypothesis != salary_savings_premise:
    # check if the percentage of salary Aamir saves in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the values about salary savings in the hypothesis and the premise match, we can infer entailment
    label = "entailment"

print(label)
