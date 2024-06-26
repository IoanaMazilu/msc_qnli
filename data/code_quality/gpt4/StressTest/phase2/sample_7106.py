hours_normal_pay_premise = 30
hours_normal_pay_hypothesis = 30

# The hypothesis talks about the hours Harry is paid x dollars, which is also referenced in the premise
if hours_normal_pay_hypothesis >= hours_normal_pay_premise:
    # Check if the hypothesis value contradicts the premise which states less than 'hours_normal_pay_premise'
    label = "contradiction"
else:
    # The premise gives an exact number of hours for which Harry is paid x dollars
    # Any number of hours less than 'hours_normal_pay_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
