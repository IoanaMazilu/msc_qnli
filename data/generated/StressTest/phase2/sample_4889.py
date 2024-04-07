# Premise: Tom drives from town W to town B, driving at a constant speed of 60 miles per hour.
# Hypothesis: Tom drives from town W to town B, driving at a constant speed of 40 miles per hour.
# Golden Label: contradiction

speed_premise = 60
speed_hypothesis = 40

# the hypothesis talks about the speed at which Tom drives from town W to town B, referenced also in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

