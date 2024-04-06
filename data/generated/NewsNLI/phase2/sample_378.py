# Premise: Two were U.S. military personnel, and the third was Polish, a U.S. defense official said.
# Hypothesis: 2 were U.S. military personnel, and the third was Polish, a source says.
# Golden Label: entailment

us_military_personnel_premise = 2
us_military_personnel_hypothesis = 2
polish_personnel_premise = 1
polish_personnel_hypothesis = 1

# the hypothesis mentions the number of U.S. military personnel and Polish personnel, which are also mentioned in the premise
if us_military_personnel_hypothesis != us_military_personnel_premise:
    # check if the number of U.S. military personnel in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif polish_personnel_hypothesis != polish_personnel_premise:
    # check if the number of Polish personnel from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

