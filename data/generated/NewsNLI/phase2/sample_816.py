# Premise: Nearly two-thirds (62 %) said they oppose U.S.-led efforts to fight terrorism.
# Hypothesis: Nearly two-thirds (63 %) expressed disapproval of the raid.
# Golden Label: neutral

oppose_efforts_premise = 0.62
disapproval_raid_hypothesis = 0.63

# the hypothesis mentions the percentage of disapproval for a particular event (raid), which is not specifically mentioned in the premise
# the premise refers to the overall opposition to U.S.-led efforts to fight terrorism, which could include the raid, but it's not explicitly stated
# hence, we cannot directly compare the two percentages as they refer to slightly different contexts

label = "neutral"

print(label)

