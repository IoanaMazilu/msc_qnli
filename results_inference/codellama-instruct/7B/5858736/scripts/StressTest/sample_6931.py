age_sandy_premise = 2
age_sandy_hypothesis = 6

# the hypothesis talks about the age of Sandy, referenced also in the premise
if age_sandy_hypothesis <= age_sandy_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_sandy_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Sandy
    # any number of years greater than 'age_sandy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
