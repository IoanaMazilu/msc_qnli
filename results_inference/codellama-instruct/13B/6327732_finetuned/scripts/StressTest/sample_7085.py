hours_premise = 10
hours_hypothesis = 30

# the hypothesis talks about the number of hours required to complete a job, referenced also in the premise
if hours_hypothesis <= hours_premise:
    # check if the hypothesis value contradicts the estimate of 'hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours required to complete a job
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
