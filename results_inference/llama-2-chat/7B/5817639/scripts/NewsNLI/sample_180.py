rape_premise = 0
rape_hypothesis = 0

# the premise mentions the increase in rapes of girls under 17, which is also referenced in the hypothesis
if rape_hypothesis!= rape_premise:
    # check if the number of rapes in the hypothesis contradicts the number of rapes in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
