# Premise: Lexi needed to save for less than 80 days to afford a vacation at the job that paid her $125 per day.
# Hypothesis: Lexi needed to save for 30 days to afford a vacation at the job that paid her $125 per day.
# Golden Label: neutral

saving_days_premise = 80
saving_days_hypothesis = 30
salary_per_day = 125

# the hypothesis talks about the number of days Lexi needed to save from her job that is also referenced in the premise
if saving_days_hypothesis >= saving_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'saving_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of saving days
    # any number of days less than 'saving_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

