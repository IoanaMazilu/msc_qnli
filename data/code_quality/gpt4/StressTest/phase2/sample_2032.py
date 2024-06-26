days_walked_premise = 6
days_walked_hypothesis = 3

# the hypothesis talks about the number of days Jisha walked, referenced also in the premise
if days_walked_hypothesis >= days_walked_premise:
    # check if the hypothesis value contradicts the estimate of less than 'days_walked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'days_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
