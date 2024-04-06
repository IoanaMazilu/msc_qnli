# Premise: At least 851 children living near a plant in northwestern China's Shaanxi province were found to have excessive lead levels in their blood, according to the Xinhua news agency.
# Hypothesis: In Hunan province, 1300 children near another plant were poisoned.
# Golden Label: neutral

children_with_lead_premise = 851
children_poisoned_hypothesis = 1300

# the hypothesis mentions the number of children poisoned in Hunan province, which is a different location than mentioned in the premise (Shaanxi province)
# hence, the hypothesis is not contradicting the premise, but also it cannot be fully and explicitly entailed from the premise 
label = "neutral"

print(label)

