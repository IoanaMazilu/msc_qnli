# Premise: Each of the 59 members in Mount school class is required to sign up for a minimum of one and a maximum of three academic clubs.
# Hypothesis: Each of the less than 59 members in Mount school class is required to sign up for a minimum of one and a maximum of three academic clubs.
# Golden Label: contradiction

members_premise = 59
members_hypothesis = 59

# the hypothesis refers to the number of members in the school class mentioned in the premise
if members_hypothesis >= members_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis number does not contradict the premise number, we can infer entailment
    label = "entailment"

print(label)

