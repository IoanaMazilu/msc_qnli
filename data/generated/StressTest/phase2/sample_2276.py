# Premise: Suresh can complete a job in 15 hours.
# Hypothesis: Suresh can complete a job in 25 hours.
# Golden Label: contradiction

suresh_job_time_premise = 15
suresh_job_time_hypothesis = 25

# the hypothesis refers to the time Suresh takes to complete a job, as stated in the premise
if suresh_job_time_hypothesis < suresh_job_time_premise:
    # check if the hypothesis value contradicts the time Suresh takes to complete a job in the premise
    label = "contradiction"
elif suresh_job_time_hypothesis == suresh_job_time_premise:
    # check if the hypothesis value is equal to the time Suresh takes to complete a job in the premise
    label = "entailment"
else:
    # any time greater than 'suresh_job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

