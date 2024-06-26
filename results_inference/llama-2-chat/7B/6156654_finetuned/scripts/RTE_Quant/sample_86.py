# The premise and hypothesis are talking about the same data, so we can compare the numbers directly

# The premise mentions that the Labor Department reported 144,000 new payroll jobs in August, while the hypothesis mentions that the Labor Department said this sector added nearly 1 of every 5 of the new jobs created during the last 12 months

# We can compare these numbers by dividing the number of jobs created in the premise by the number of jobs created in the hypothesis
jobs_created_premise_divided_by_jobs_created_hypothesis = 144000 / 15

# If the number of jobs created in the premise divided by the number of jobs created in the hypothesis is equal to 1, then we can infer entailment
if jobs_created_premise_divided_by_jobs_created_hypothesis == 1:
    label = "entailment"
else:
    label = "contradiction"

print(label)
