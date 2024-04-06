# Premise: -- At least seven civilians died in a U.S. airstrike on an ISIS-controlled oilfield near the city of Khusham, the London-based Syrian Observatory for Human Rights said.
# Hypothesis: U.S. airstrikes kill at least 10 civilians, Syrian Observatory for Human Rights says.
# Golden Label: neutral

civilians_died_premise = 7
civilians_died_hypothesis = 10

# the hypothesis mentions the number of civilians died in a U.S. airstrike, which is also referenced in the premise
if civilians_died_hypothesis > civilians_died_premise:
    # check if the number of civilians died in the hypothesis contradicts the number of civilians died reported in the premise
    label = "contradiction"
else:
    # if the number of civilians died in the hypothesis does not contradict the number reported in the premise, we can infer entailment
    label = "entailment"

print(label)

