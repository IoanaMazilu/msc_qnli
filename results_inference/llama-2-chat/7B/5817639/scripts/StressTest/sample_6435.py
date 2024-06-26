jill_wage_premise = 6.0
jill_wage_hypothesis = 75

# the hypothesis talks about the tip rate, which is also referred to in the premise
if jill_wage_hypothesis >= jill_wage_premise * 1.35:
    # check if the hypothesis value contradicts the estimate of 'jill_wage_premise' multiplied by the standard tip rate
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip rate
    # any tip rate greater than 'jill_wage_premise' multiplied by 1.35 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
