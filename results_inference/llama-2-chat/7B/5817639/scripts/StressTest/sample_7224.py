ob_length_premise = 6
ob_length_hypothesis = 6

# the hypothesis talks about the length of OB, referenced also in the premise
if ob_length_hypothesis <= ob_length_premise:
    # check if the hypothesis value contradicts the estimate of 'ob_length_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the length of OB, and the hypothesis does not contradict it
    label = "entailment"

print(label)
