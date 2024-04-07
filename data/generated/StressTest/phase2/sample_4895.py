# Premise: Jane can make a handcrafted drum in 4 weeks.
# Hypothesis: Jane can make a handcrafted drum in more than 4 weeks.
# Golden Label: contradiction

drum_making_time_premise = 4
drum_making_time_hypothesis = 4

# the hypothesis talks about the time Jane needs to make a handcrafted drum, which is also referenced in the premise
if drum_making_time_hypothesis != drum_making_time_premise:
    # check if the hypothesis value contradicts the exact time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

