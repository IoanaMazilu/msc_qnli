# Premise: The 16 NATO members and the 14 countries which used to form the rival Warsaw Pact agreed that there would be significantly less equipment permitted in the area of application in Europe than there was under the original treaty.
# Hypothesis: The NATO has 16 members.
# Golden Label: entailment

nato_members_premise = 16
nato_members_hypothesis = 16

# the hypothesis talks about the number of NATO members, which is also mentioned in the premise
if nato_members_hypothesis != nato_members_premise:
    # check if the number of NATO members in the hypothesis contradicts the number of NATO members from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

