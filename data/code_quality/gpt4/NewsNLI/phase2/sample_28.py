earning_premise = 29.3
earning_hypothesis = 29.3

# the hypothesis mentions the earnings of The Lion King 3D, which is also mentioned in the premise
if earning_hypothesis != earning_premise:
    # check if the earnings in the hypothesis contradicts the earnings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis earnings do not contradict the premise earnings, we can infer entailment
    label = "entailment"

print(label)
