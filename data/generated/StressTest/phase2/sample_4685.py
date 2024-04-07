# Premise: James can finish a job in 20 dasy he worked for 10 days alone and completed the remaining part working with David 2 days how many days would both David and James together take to complete the entire job?
# Hypothesis: James can finish a job in 50 dasy he worked for 10 days alone and completed the remaining part working with David 2 days how many days would both David and James together take to complete the entire job?
# Golden Label: contradiction

job_completion_time_james_premise = 20
job_completion_time_james_hypothesis = 50
worked_alone_time_premise = 10
worked_alone_time_hypothesis = 10
worked_together_time_premise = 2
worked_together_time_hypothesis = 2

# Both the hypothesis and premise talk about how long James can finish a job alone and with David
if job_completion_time_james_hypothesis != job_completion_time_james_premise:
    # check if the job completion time by James in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif worked_alone_time_hypothesis != worked_alone_time_premise or worked_together_time_hypothesis != worked_together_time_premise:
    # check if the time James worked alone or with David in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

