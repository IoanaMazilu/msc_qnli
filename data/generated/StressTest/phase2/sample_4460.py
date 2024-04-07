# Premise: Annie, working alone, can do the same job in just 9 hours.
# Hypothesis: Annie, working alone, can do the same job in just 1 hours.
# Golden Label: contradiction

job_time_premise = 9
job_time_hypothesis = 1

# the hypothesis refers to the time Annie needs to finish a job, which is also mentioned in the premise
if job_time_hypothesis != job_time_premise:
    # check if the time in the hypothesis contradicts the time stated in the premise
    label = "contradiction"
else:
    # if the times are the same, the hypothesis is entailed from the premise
    label = "entailment"

print(label)

