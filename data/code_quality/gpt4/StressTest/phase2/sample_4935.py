indu_leave_premise = 7
indu_leave_hypothesis = 5

# the hypothesis talks about the number of days Indu leaves before the work is finished, which is also mentioned in the premise
if indu_leave_premise < indu_leave_hypothesis:
    # check if the number of days mentioned in the premise contradicts the estimate of more than 'indu_leave_hypothesis'
    label = "contradiction"
elif indu_leave_premise > indu_leave_hypothesis:
    # check if the number of days mentioned in the premise is greater than 'indu_leave_hypothesis'
    # if it is, then the premise entails the hypothesis
    label = "entailment"
else:
    # if the number of days mentioned in the premise is equal to 'indu_leave_hypothesis', then it's a neutral case
    label = "neutral"

print(label)
