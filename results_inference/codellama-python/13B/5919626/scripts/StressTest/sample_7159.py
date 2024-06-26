age_sandy_premise = 38
age_sandy_hypothesis = 38
years_premise = 4
years_hypothesis = 6

# the hypothesis talks about the number of years after which Sandy's age will be 38
# the premise gives an estimate for the number of years after which Sandy's age will be 38
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years after which Sandy's age will be 38
    # any number of years greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
