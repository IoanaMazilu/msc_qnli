oa_premise = 2
ac_premise = 4
bd_premise = 6

oa_hypothesis = 2
ac_hypothesis = 4
bd_hypothesis = 6

# the hypothesis refers to the same conditions as the premise but with different values for OA
if oa_hypothesis <= oa_premise:
    # check if the value of 'oa_hypothesis' contradicts the value of OA in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
