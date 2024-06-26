working_hours_premise = 3
working_hours_hypothesis = 4

# the hypothesis talks about the number of hours it would take Annie to complete the job if Dan worked alone for a longer time
if working_hours_hypothesis <= working_hours_premise:
    # check if the hypothesis value contradicts the estimate of 'working_hours_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours it would take Annie to complete the job, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
