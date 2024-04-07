# Premise: Mary has a monthly salary of $1200.
# Hypothesis: Mary has a monthly salary of $less than 3200.
# Golden Label: entailment

salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis talks about Mary's monthly salary, referenced also in the premise
if salary_premise >= salary_hypothesis:
    # check if the statement of 'salary_premise' contradicts the maximum limit of salary in the hypothesis
    label = "contradiction"
elif salary_premise != salary_hypothesis:
    # check if the exact value of salary in the hypothesis does not match with the 'salary_premise'
    label = "neutral"
else:
    # if the salary in the hypothesis does not contradict the premise and is exactly the same, we can infer entailment
    label = "entailment"

print(label)

