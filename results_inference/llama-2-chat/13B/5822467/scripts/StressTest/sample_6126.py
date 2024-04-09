iceland_norway_visitors_premise = 31
iceland_norway_visitors_hypothesis = 41

# the hypothesis refers to the number of people who have visited both Iceland and Norway
if iceland_norway_visitors_hypothesis <= iceland_norway_visitors_premise:
    # check if the hypothesis value contradicts the estimate of 'iceland_norway_visitors_premise'
    label = "contradiction"
elif iceland_norway_visitors_hypothesis > iceland_norway_visitors_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the number of people who have visited neither country
    # any number of people less than 'iceland_norway_visitors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
