# Premise: The magnitude-9 quake sent walls of water slamming into the country's Pacific shores, sweeping away whole villages and leaving more than 27,000 dead or missing.
# Hypothesis: The quake has left more than 13,000 dead and 14,000 missing.
# Golden Label: neutral

total_casualties_premise = 27000
dead_hypothesis = 13000
missing_hypothesis = 14000
total_casualties_hypothesis = dead_hypothesis + missing_hypothesis

# the hypothesis mentions the total number of casualties due to the quake, which is also referenced in the premise
if total_casualties_hypothesis != total_casualties_premise:
    # check if the total casualties in the hypothesis contradicts the total casualties reported in the premise
    label = "contradiction"
else:
    # if the total casualties in the hypothesis do not contradict the total casualties in the premise, we can infer entailment
    label = "entailment"

print(label)

