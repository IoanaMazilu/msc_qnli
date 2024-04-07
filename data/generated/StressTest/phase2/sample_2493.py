# Premise: Aarti had prior experience in that route and mentioned that the speed of stream was 4 kmph.
# Hypothesis: Aarti had prior experience in that route and mentioned that the speed of stream was more than 2 kmph.
# Golden Label: entailment

stream_speed_premise = 4
stream_speed_hypothesis = 2

# the hypothesis refers to the speed of stream mentioned by Aarti in the premise
if stream_speed_premise < stream_speed_hypothesis:
    # check if the 'stream_speed_hypothesis' contradicts the speed of stream in the premise
    label = "contradiction"
elif stream_speed_premise == stream_speed_hypothesis:
    # check if the speed of stream in the hypothesis is equal to the speed of stream in the premise
    # in this case, the hypothesis cannot be fully and explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value do not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

