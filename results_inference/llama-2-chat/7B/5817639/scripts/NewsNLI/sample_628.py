experience_premise = 0
experience_hypothesis = 0

# the hypothesis mentions the lack of political experience of the military, which is also mentioned in the premise
if experience_hypothesis!= experience_premise:
    # check if the lack of political experience in the hypothesis contradicts the lack of political experience in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
