# Premise: Twenty-two of the dead were U.S. Navy personnel, the Pentagon said.
# Hypothesis: 17 were Navy SEALs.
# Golden Label: neutral

dead_personnel_premise = 22
navy_seals_hypothesis = 17

# the hypothesis mentions a number of Navy SEALs, which is included in the total number of dead U.S. Navy personnel stated in the premise
if navy_seals_hypothesis > dead_personnel_premise:
    # check if the number of Navy SEALs in the hypothesis contradicts (is greater than) the total number of dead personnel in the premise
    label = "contradiction"
else:
    # if the number of Navy SEALs is less than or equal to the total number of dead personnel, it does not contradict the premise, but it is not sufficient to entail the premise either
    label = "neutral"

print(label)

