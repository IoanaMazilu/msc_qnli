days_premise = 35
days_hypothesis = 25

# the hypothesis refers to the number of days Sreedhar and Sravan can do a work, which is also mentioned in the premise
if days_hypothesis >= days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)