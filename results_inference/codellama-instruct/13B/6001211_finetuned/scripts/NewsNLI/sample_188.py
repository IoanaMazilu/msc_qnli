parole_denied_premise = 17
parole_denied_hypothesis = 17

# the hypothesis mentions the number of times Susan Atkins has been denied parole, which is also mentioned in the premise
if parole_denied_hypothesis!= parole_denied_premise:
    # check if the number of times parole was denied in the hypothesis contradicts the number of times reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
