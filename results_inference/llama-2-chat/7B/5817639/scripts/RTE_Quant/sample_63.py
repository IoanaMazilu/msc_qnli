cern_member_states_premise = 20
cern_member_states_hypothesis = 20

# the hypothesis talks about the number of member states of CERN, which is also mentioned in the premise
if cern_member_states_hypothesis == cern_member_states_premise:
    # if the hypothesis and premise values match, we can infer entailment
    label = "entailment"
elif cern_member_states_hypothesis < cern_member_states_premise:
    # if the hypothesis value is less than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values do not match or are equal, we can infer neutrality
    label = "neutral"

print(label)
