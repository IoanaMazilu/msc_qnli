working_alone_premise = 3
working_alone_hypothesis = 2

# the hypothesis talks about the number of hours it will take Annie to complete the job, referenced also in the premise
if working_alone_hypothesis <= working_alone_premise:
    # check if the hypothesis value contradicts the estimate of more than 'working_alone_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours it will take Annie to complete the job
    # any number of hours greater than 'working_alone_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
