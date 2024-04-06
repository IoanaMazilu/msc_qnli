# Premise: Two senior administration officials told CNN that U.S. authorities had intelligence that they shared with the Russians.
# Hypothesis: Two U.S. officials tell CNN that information was shared with the Russians.
# Golden Label: entailment

officials_premise = 2
officials_hypothesis = 2

# the hypothesis mentions the number of U.S. officials who shared information with the Russians, which is also mentioned in the premise
if officials_hypothesis != officials_premise:
    # check if the number of officials in the hypothesis contradicts the number of officials reported in the premise
    label = "contradiction"
else:
    # if the number of officials in the hypothesis does not contradict the number of officials in the premise, we can infer entailment
    label = "entailment"

print(label)

