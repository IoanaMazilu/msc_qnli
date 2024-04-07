# Premise: Kamal will complete work in less than 40 days.
# Hypothesis: Kamal will complete work in 20 days.
# Golden Label: neutral

work_days_premise = 40
work_days_hypothesis = 20

# the hypothesis talks about the number of days Kamal will take to complete work, referenced also in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

