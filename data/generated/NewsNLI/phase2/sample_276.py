# Premise: Jutting 35 meters out the side of a cliff on Jasper National Park's Icefields Parkway, the glass-floored observation walkway hangs 280 meters above Sunwapta Canyon.
# Hypothesis: Canada's new Glacier Skywalk hangs 280 meters above Sunwapta Canyon in Jasper National Park.
# Golden Label: neutral

observation_walkway_height_premise = 280
observation_walkway_height_hypothesis = 280

# the hypothesis mentions the height of the observation walkway in Jasper National Park, which is also mentioned in the premise
if observation_walkway_height_hypothesis != observation_walkway_height_premise:
    # check if the height of the observation walkway in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # if the height of the observation walkway in the hypothesis does not contradict the height in the premise, we can infer entailment
    label = "entailment"

print(label)

