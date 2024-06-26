cases_premise = 8
cases_hypothesis = 5

# the hypothesis talks about the number of boxes of cigarettes in one case, which is also mentioned in the premise
if cases_hypothesis >= cases_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
