dan_hours_premise = 3
dan_hours_hypothesis = float(input("Enter the number of hours Dan works alone (more than 2): "))
annie_hours_premise = 0

# the hypothesis talks about the number of hours Annie needs to complete the job, referenced also in the premise
if dan_hours_hypothesis <= annie_hours_premise:
    # check if the hypothesis value contradicts the estimate of 0 hours in the premise
    label = "contradiction"
elif dan_hours_hypothesis > annie_hours_premise:
    # check if the hypothesis value entails the premise (Annie needs more hours to complete the job)
    label = "entailment"
else:
    # the premise gives only an estimate for the number of hours Annie needs to complete the job
    # any number of hours greater than 0 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
