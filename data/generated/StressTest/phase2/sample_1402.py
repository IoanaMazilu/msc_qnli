# Premise: What is the share of Sravan, if Sreedhar alone can do the work in more than 25 days?
# Hypothesis: What is the share of Sravan, if Sreedhar alone can do the work in 75 days?
# Golden Label: neutral

work_days_premise = 25
work_days_hypothesis = 75

# the hypothesis talks about the number of days Sreedhar alone can do the work
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Sreedhar alone can do the work
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

