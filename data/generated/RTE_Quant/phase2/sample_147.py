# Premise: The expulsion of Albanians, which has distracted NATO with a parallel relief operation, has only served to harden the resolve of NATO's 19 members, who are now willing to approve attacks on more sensitive targets, like Milosevic's homes and Yugoslavia's state-run television.
# Hypothesis: NATO has 16 members.
# Golden Label: neutral

nato_members_premise = 19
nato_members_hypothesis = 16

# the hypothesis talks about the number of NATO members which is also mentioned in the premise
if nato_members_hypothesis != nato_members_premise:
    # check if the number of NATO members in the hypothesis contradicts the number of NATO members from the premise
    label = "contradiction"
else:
    # if the number of NATO members in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

