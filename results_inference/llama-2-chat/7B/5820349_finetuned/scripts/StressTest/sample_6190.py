saving_days_premise = 80
saving_days_hypothesis = 30

# the hypothesis talks about the number of days Lexi needed to save for a vacation, also referenced in the premise
if saving_days_hypothesis >= saving_days_premise:
    # check if the hypothesis value contradicts the estimate of less than'saving_days_premise'
    label = "contradiction"
elif saving_days_hypothesis < saving_days_premise:
    # the premise gives only an estimate for the number of days
    # any number of days less than'saving_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
