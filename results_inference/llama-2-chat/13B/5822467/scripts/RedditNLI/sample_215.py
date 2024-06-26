premise = "U.S Job loss: Worst in 34 years."
hypothesis = "U.S. January Job Losses Worst in 34 Years."

# define variables with representative names for the numerical entities in both inputs
losses_premise = 34
losses_hypothesis = 34

# extract all quantities as valid numbers (integers or floats)
if losses_premise!= losses_hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
elif losses_hypothesis < losses_premise:
    # check if the estimated number of years in the hypothesis contradicts the premise estimate of "worst in 34 years"
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any estimate of the number of years in the hypothesis greater or equal to the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
