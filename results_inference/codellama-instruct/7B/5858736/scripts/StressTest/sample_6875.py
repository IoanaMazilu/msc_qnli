john_work_days_premise = 60
john_work_days_hypothesis = 60

if john_work_days_hypothesis >= john_work_days_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
