# Premise: CERN has now grown to include 20 member states and enjoys the active participation of many other countries world-wide.
# Hypothesis: CERN has 20 member states.
# Golden Label: entailment

member_states_premise = 20
member_states_hypothesis = 20

# the hypothesis talks about the number of member states of CERN which is also mentioned in the premise
if member_states_hypothesis != member_states_premise:
    # check if the number of member states in the hypothesis contradicts the number of member states from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

