# Premise: Mary has a monthly salary of $1200.
# Hypothesis: Mary has a monthly salary of $3200.
# Golden Label: contradiction

salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis talks about the same monthly salary of Mary referenced in the premise
if salary_hypothesis != salary_premise:
    # check if the salary hypothesized contradicts the salary mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesized salary is the same as the one in the premise, we can infer entailment
    label = "entailment"

print(label)

