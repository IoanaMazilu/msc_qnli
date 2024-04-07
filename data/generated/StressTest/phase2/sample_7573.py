# Premise: If Fred walks at a constant speed of less than 7 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Hypothesis: If Fred walks at a constant speed of 2 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Golden Label: neutral

fred_speed_premise = 7
fred_speed_hypothesis = 2
sam_speed_premise = 5
sam_speed_hypothesis = 5

# the hypothesis describes the walking speeds of Fred and Sam, which are also mentioned in the premise
# check if the speeds in the hypothesis contradict the ones in the premise
if fred_speed_hypothesis >= fred_speed_premise:
    label = "contradiction"
elif sam_speed_hypothesis != sam_speed_premise:
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

