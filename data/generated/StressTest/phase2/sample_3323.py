# Premise: Albert borrowed a total of $6000 from john and Charlie.
# Hypothesis: Albert borrowed a total of $3000 from john and Charlie.
# Golden Label: contradiction

borrowed_premise = 6000
borrowed_hypothesis = 3000

# the hypothesis refers to the total amount borrowed by Albert from John and Charlie
if borrowed_hypothesis > borrowed_premise:
    # check if the amount in the hypothesis contradicts the total amount borrowed according to the premise
    label = "contradiction"
elif borrowed_hypothesis < borrowed_premise:
    # check if the amount borrowed in the hypothesis is less than the amount stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

