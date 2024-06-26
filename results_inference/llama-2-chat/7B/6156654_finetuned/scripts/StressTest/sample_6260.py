job_time_premise = 15
job_time_hypothesis = 15

# the hypothesis refers to the same job time mentioned in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it entails the premise
    label = "entailment"

print(label)
