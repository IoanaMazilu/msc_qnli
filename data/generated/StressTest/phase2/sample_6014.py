# Premise: Assuming that Karen drives at an average speed of 60 mph and Tom drives at an average speed of 45 mph, how many E miles will Tom drive before Karen wins the bet?
# Hypothesis: Assuming that Karen drives at an average speed of 20 mph and Tom drives at an average speed of 45 mph, how many E miles will Tom drive before Karen wins the bet?
# Golden Label: contradiction

karen_speed_premise = 60
karen_speed_hypothesis = 20
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis talks about Karen's and Tom's driving speeds, referenced also in the premise
if karen_speed_hypothesis != karen_speed_premise or tom_speed_hypothesis != tom_speed_premise:
    # check if the driving speeds in the hypothesis contradict the driving speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates are equal to the premise ones, we can infer entailment
    label = "entailment"

print(label)

