grant_premise = 4.5e6
grant_hypothesis = 4.5e6

# the hypothesis mentions the value of the grant for Palestinian football, which is also mentioned in the premise
if grant_hypothesis != grant_premise:
    # check if the grant value in the hypothesis contradicts the grant value reported in the premise
    label = "contradiction"
else:
    # if the grant value in the hypothesis does not contradict the grant value in the premise, we can infer entailment
    label = "entailment"

print(label)
