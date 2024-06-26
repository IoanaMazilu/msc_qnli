max_hours_worked_premise = 60

# the hypothesis talks about the maximum number of hours Mary works, which is also referenced in the premise
# there is no explicit numerical value in the hypothesis, but it suggests that the number is more than 60 hours
if max_hours_worked_premise < 60:
    # check if the premise value contradicts the estimate of more than 60 hours in the hypothesis
    label = "contradiction"
else:
    # if 'max_hours_worked_premise' does not contradict the estimate of the hypothesis, we can infer entailment
    label = "entailment"

print(label)
