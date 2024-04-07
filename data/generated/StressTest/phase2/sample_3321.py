# Premise: Albert borrowed a total of $6000 from john and Charlie.
# Hypothesis: Albert borrowed a total of $more than 4000 from john and Charlie.
# Golden Label: entailment

borrowed_premise = 6000
borrowed_hypothesis = 4000

# the hypothesis refers to the amount borrowed by Albert from John and Charlie
if borrowed_hypothesis >= borrowed_premise:
    # check if the hypothesis value contradicts the premise amount
    label = "contradiction"
elif borrowed_hypothesis > borrowed_premise:
    # check if the hypothesis value contradicts the premise amount
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

