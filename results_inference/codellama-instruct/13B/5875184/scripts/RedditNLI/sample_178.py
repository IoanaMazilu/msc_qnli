premise_jobs_lost = 533000
hypothesis_jobs_lost = 533000

if premise_jobs_lost!= hypothesis_jobs_lost:
    label = "contradiction"
else:
    label = "entailment"

print(label)
