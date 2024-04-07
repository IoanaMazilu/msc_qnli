# Premise: Annie, working alone, can do the same job in just 9 hours.
# Hypothesis: Annie, working alone, can do the same job in just 6 hours.
# Golden Label: contradiction

job_time_premise = 9
job_time_hypothesis = 6

# The hypothesis refers to the time Annie needs to do a job, also mentioned in the premise
if job_time_hypothesis != job_time_premise:
    # Check if the time mentioned in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # If the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)

