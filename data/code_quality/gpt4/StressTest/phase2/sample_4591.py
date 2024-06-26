borrowed_years_premise = 8
borrowed_years_hypothesis = 4

# the hypothesis refers to the number of years Arun borrowed a sum on S, which is also mentioned in the premise
if borrowed_years_hypothesis >= borrowed_years_premise:
    # check if the number of years in the hypothesis contradicts the estimate of less than 'borrowed_years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'borrowed_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
