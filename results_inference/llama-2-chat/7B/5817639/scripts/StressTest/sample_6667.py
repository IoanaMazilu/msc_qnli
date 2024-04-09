days_work_premise = 40
days_work_hypothesis = 20

# the hypothesis talks about the number of days Kamal will take to complete work, referenced also in the premise
if days_work_hypothesis <= days_work_premise:
    # check if the hypothesis value contradicts the estimate of less than 'days_work_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'days_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
