germs_premise = 43200000
germs_hypothesis = 43200000 + 10000

# the hypothesis talks about the number of germs in a lab, referenced also in the premise
if germs_hypothesis <= germs_premise:
    # check if the hypothesis value contradicts the estimate of 'germs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of germs
    # any number of germs greater than 'germs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
