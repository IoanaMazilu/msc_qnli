experience_premise = 0
experience_hypothesis = 0

# the hypothesis mentions the political experience of the military, which is also mentioned in the premise
if experience_hypothesis!= experience_premise:
    # check if the political experience in the hypothesis contradicts the political experience reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
