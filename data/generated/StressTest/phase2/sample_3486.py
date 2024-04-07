# Premise: How many days will it take both of them to complete the entire job, given that it would have taken David 12 days to complete the job alone?
# Hypothesis: How many days will it take both of them to complete the entire job, given that it would have taken David less than 52 days to complete the job alone?
# Golden Label: entailment

days_to_complete_job_alone_premise = 12
days_to_complete_job_alone_hypothesis = 52

# the hypothesis refers to the number of days it would have taken David to complete the job alone, also mentioned in the premise
if days_to_complete_job_alone_hypothesis < days_to_complete_job_alone_premise:
    # check if the estimate of 'days_to_complete_job_alone_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif days_to_complete_job_alone_hypothesis > days_to_complete_job_alone_premise:
    # if the hypothesis values and estimates are greater than the premise ones, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

