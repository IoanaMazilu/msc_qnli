# Premise: But two senior National Transitional Council spokesmen said the report was unconfirmed and a third reportedly denied the claim.
# Hypothesis: Two NTC spokesmen say the report is not confirmed ; a third denies it.
# Golden Label: neutral

ntc_spokesmen_premise = 2
ntc_spokesmen_hypothesis = 2
third_spokesman_premise = 1
third_spokesman_hypothesis = 1

# the hypothesis mentions the number of NTC spokesmen and their statements, which are also mentioned in the premise
if ntc_spokesmen_hypothesis != ntc_spokesmen_premise:
    # check if the number of NTC spokesmen in the hypothesis contradicts the number of NTC spokesmen reported in the premise
    label = "contradiction"
elif third_spokesman_hypothesis != third_spokesman_premise:
    # check if the third spokesman from the hypothesis contradicts the third spokesman in the premise
    label = "contradiction"
else:
    # if the hypothesis values and statements do not contradict the premise values and statements, we can infer entailment
    label = "entailment"

print(label)

