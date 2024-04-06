# Premise: Bail had already been set at $5 million on five murder charges related to the grisly discovery of the bodies at his home in Cleveland.
# Hypothesis: Bail for Anthony Sowell set at $1 million on rape charges.
# Golden Label: neutral

bail_premise = 5000000
bail_hypothesis = 1000000

# the hypothesis mentions the bail amount for charges, which is also mentioned in the premise
# however, the hypothesis refers to a different type of charge and a different bail amount
if bail_hypothesis == bail_premise:
    # check if the bail amount in the hypothesis matches the bail amount reported in the premise
    label = "entailment"
elif bail_hypothesis != bail_premise:
    # check if the bail amount from the hypothesis contradicts the bail amount in the premise
    label = "contradiction"
else:
    # if the hypothesis bail amount does not contradict the premise bail amount, we can infer neutrality
    label = "neutral"

print(label)

