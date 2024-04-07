# Premise: If Fred walks at a constant speed of 5 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Hypothesis: If Fred walks at a constant speed of less than 5 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Golden Label: contradiction

fred_speed_premise = 5
fred_speed_hypothesis = 5
sam_speed_premise = 5
sam_speed_hypothesis = 5

# the hypothesis and premise both talk about the speeds of Fred and Sam
# first, we compare Fred's speed in both the premise and hypothesis
if fred_speed_hypothesis >= fred_speed_premise:
    # check if Fred's speed in the hypothesis contradicts the premise
    label = "contradiction"
# next, we compare Sam's speed in both the premise and hypothesis
elif sam_speed_hypothesis != sam_speed_premise:
    # check if Sam's speed in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

