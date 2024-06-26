total_premise = 4320
total_hypothesis = 6320
ratio = [2, 4, 6]

# The hypothesis refers to the total amount mentioned in the premise
# and the distribution ratio among John, Jose & Binoy.
if total_hypothesis != total_premise:
    # check if the total in the hypothesis contradicts the total amount stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
