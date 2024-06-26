germs_premise = 360000
germs_hypothesis = 80000000

# the hypothesis talks about the number of germs in the biology lab, referenced also in the premise
if germs_hypothesis <= germs_premise:
    # check if the hypothesis value contradicts the number of germs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of germs
    # any number of germs greater than 'germs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
