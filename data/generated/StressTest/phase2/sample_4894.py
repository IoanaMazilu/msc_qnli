# Premise: Jane can make a handcrafted drum in less than 6 weeks.
# Hypothesis: Jane can make a handcrafted drum in 4 weeks.
# Golden Label: neutral

drum_creation_premise = 6
drum_creation_hypothesis = 4

# the hypothesis talks about the time Jane needs to create a handcrafted drum, mentioned also in the premise
if drum_creation_hypothesis >= drum_creation_premise:
    # check if the 'drum_creation_hypothesis' contradicts the premise estimate of less than 'drum_creation_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the creation time
    # any creation time less than 'drum_creation_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

