kiran_bineesh_diff_premise = 7
kiran_bineesh_diff_hypothesis = 7

# the hypothesis refers to the difference in ages between Kiran and Bineesh mentioned in the premise
if kiran_bineesh_diff_hypothesis >= kiran_bineesh_diff_premise:
    # check if the hypothesis value contradicts the estimate of 'kiran_bineesh_diff_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
