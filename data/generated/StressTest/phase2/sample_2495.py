# Premise: Aarti had prior experience in that route and mentioned that the speed of stream was 4 kmph.
# Hypothesis: Aarti had prior experience in that route and mentioned that the speed of stream was 6 kmph.
# Golden Label: contradiction

stream_speed_premise = 4
stream_speed_hypothesis = 6

# the hypothesis talks about the speed of a stream, referenced also in the premise
if stream_speed_hypothesis != stream_speed_premise:
    # check if the speed of the stream in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis matches the speed mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

