save_days_premise = 80
save_days_hypothesis = 30

# the hypothesis talks about the number of days Lexi needed to save, referenced also in the premise
if save_days_hypothesis >= save_days_premise:
    # check if the hypothesis value contradicts the estimate of less than'save_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than'save_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
