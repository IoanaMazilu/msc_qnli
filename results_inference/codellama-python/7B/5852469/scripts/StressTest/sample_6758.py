tom_p_premise = 8
tom_p_hypothesis = 6

# the hypothesis talks about the number of P. Tom goes after, referenced also in the premise
if tom_p_hypothesis <= tom_p_premise:
    # check if the hypothesis value contradicts the estimate of more than 'tom_p_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P. Tom goes after
    # any number of P. greater than 'tom_p_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
