essential_premise_hours_premise: 85
essential_hypothesis_hours_hypothesis: 15

# the hypothesis talks about the time Dan needs to do a job, referenced also in the premise
if essential_hypothesis_hours_hypothesis <= essential_premise_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'essential_premise_hours_premise' hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time less than 'essential_premise_hours_premise' hours is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
