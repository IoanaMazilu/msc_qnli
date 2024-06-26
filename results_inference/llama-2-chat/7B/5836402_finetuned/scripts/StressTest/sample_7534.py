leo_gain_premise = 50
leo_gain_hypothesis = 10

# the hypothesis refers to the weight gain of Leo, mentioned in the premise
if leo_gain_hypothesis >= leo_gain_premise:
    # check if the hypothesis value contradicts the estimate of less than 'leo_gain_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise estimate, we can infer entailment
    label = "entailment"

print(label)
