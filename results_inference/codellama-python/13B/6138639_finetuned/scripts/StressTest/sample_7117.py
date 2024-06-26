germs_premise = 30 ** 6
germs_hypothesis = 10 ** 6

# the hypothesis talks about the number of germs in the biology lab, referenced also in the premise
if germs_hypothesis >= germs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'germs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of germs
    # any number of germs less than 'germs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
