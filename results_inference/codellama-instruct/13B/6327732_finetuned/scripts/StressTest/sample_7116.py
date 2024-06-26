germs_premise = 4.32 * 10 ** 6
germs_hypothesis = 4.32 * 10 ** 30

# the hypothesis talks about the number of germs in the biology lab, referenced also in the premise
if germs_hypothesis >= germs_premise:
    # check if the hypothesis value contradicts the estimate of more than 'germs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of germs
    # any number of germs less than 'germs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
