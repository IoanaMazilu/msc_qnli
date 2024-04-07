# Premise: Albert borrowed a total of $5800 from Brian and Charlie.
# Hypothesis: Albert borrowed a total of $less than 5800 from Brian and Charlie.
# Golden Label: contradiction

borrowed_premise = 5800
borrowed_hypothesis = 5800

# the hypothesis talks about the total amount borrowed by Albert, referenced in the premise
if borrowed_hypothesis < borrowed_premise:
    # check if the hypothesis value contradicts the total amount borrowed by Albert in the premise
    label = "contradiction"
elif borrowed_hypothesis > borrowed_premise:
    # check if the hypothesis value contradicts the total amount borrowed by Albert in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

