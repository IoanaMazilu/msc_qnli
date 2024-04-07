# Premise: Zane can make a similar handcrafted drum in 6 weeks.
# Hypothesis: Zane can make a similar handcrafted drum in 4 weeks.
# Golden Label: contradiction

time_to_make_drum_premise = 6
time_to_make_drum_hypothesis = 4

# the hypothesis refers to the time Zane takes to make a drum, which is also specified in the premise
if time_to_make_drum_hypothesis > time_to_make_drum_premise:
    # check if the time estimate in the hypothesis contradicts the time specified in the premise
    label = "contradiction"
else:
    # the premise specifies an exact time for making the drum
    # any time less than or equal to 'time_to_make_drum_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

