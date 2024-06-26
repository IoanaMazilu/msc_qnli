petrol_spent_premise = 60
petrol_spent_hypothesis = 30

# the hypothesis talks about the percentage of income spent on petrol, which is also mentioned in the premise
if petrol_spent_hypothesis >= petrol_spent_premise:
    # check if the hypothesis value contradicts the estimate of less than 'petrol_spent_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of income spent on petrol
    # any percentage less than 'petrol_spent_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
