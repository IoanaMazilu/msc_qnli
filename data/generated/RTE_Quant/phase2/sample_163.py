# Premise: In 2003, Yunus brought the microcredit revolution to the streets of Bangladesh to support more than 50,000 beggars, whom the Grameen Bank respectfully calls Struggling Members.
# Hypothesis: Yunus supported more than 50,000 Struggling Members.
# Golden Label: entailment

year_premise = 2003
supported_members_premise = 50000
supported_members_hypothesis = 50000

# the hypothesis talks about the number of supported members which is also mentioned in the premise
if supported_members_hypothesis != supported_members_premise:
    # check if the number of supported members in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of supported members in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

