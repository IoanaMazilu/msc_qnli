# Premise: Trijicon has a $660 million contract for the U.S. Marine Corps and the U.S. Army, according to Turner.
# Hypothesis: Trijicon has a $660 million contract for Marine Corps, Army, defense official says.
# Golden Label: entailment

contract_value_premise = 660000000
contract_value_hypothesis = 660000000

# the hypothesis mentions the contract value for the Marine Corps and Army, which is also mentioned in the premise
if contract_value_hypothesis != contract_value_premise:
    # check if the contract value from the hypothesis contradicts the contract value mentioned in the premise
    label = "contradiction"
else:
    # if the contract value from the hypothesis does not contradict the contract value in the premise, we can infer entailment
    label = "entailment"

print(label)

