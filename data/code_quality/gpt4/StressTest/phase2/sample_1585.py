advances_premise = 30000
advances_hypothesis = 20000

# the hypothesis refers to the amount Sravan advances after 8 months, mentioned in the premise
if advances_hypothesis >= advances_premise:
    # check if the hypothesis value contradicts the estimate of less than 'advances_premise'
    label = "contradiction"
elif advances_hypothesis < advances_premise:
    # if the hypothesis value is less than the premise value and does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
