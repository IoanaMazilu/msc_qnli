# Premise: Two car bombs explode near a police station outside of Baghdad's Green Zone, killing seven police officers and wounding about 60 others.
# Hypothesis: A pair of car bombs explode near government offices in Baghdad.
# Golden Label: neutral

car_bombs_premise = 2
car_bombs_hypothesis = 2

# the hypothesis talks about the location of the bombing which is not specific enough to compare with the premise
# the hypothesis cannot be fully entailed from the premise, since the detailed location is not specified.
label = "neutral"

print(label)

