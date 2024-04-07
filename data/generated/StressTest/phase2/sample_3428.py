# Premise: Craig had 200 apples.
# Hypothesis: Craig had 100 apples.
# Golden Label: contradiction

apples_premise = 200
apples_hypothesis = 100

# the hypothesis talks about the number of apples Craig had, which is also mentioned in the premise
if apples_hypothesis != apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

