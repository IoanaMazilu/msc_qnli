# Premise: Working independently, Ann can do the same job in 9 hours.
# Hypothesis: Working independently, Ann can do the same job in more than 7 hours.
# Golden Label: entailment

job_hours_premise = 9
job_hours_hypothesis = 7

# the hypothesis talks about the number of hours Ann can do a job, referenced also in the premise
if job_hours_premise < job_hours_hypothesis:
    # check if the hours in the premise contradict the estimate of more than 'job_hours_hypothesis'
    label = "contradiction"
elif job_hours_premise == job_hours_hypothesis:
    # the premise gives a specific number of hours 
    # any number of hours equal to 'job_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

