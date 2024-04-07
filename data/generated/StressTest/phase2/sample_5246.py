# Premise: In a 100 m sprint race Kelly was given a 3 m head start by Abel.
# Hypothesis: In a less than 100 m sprint race Kelly was given a 3 m head start by Abel.
# Golden Label: contradiction

race_distance_premise = 100
race_distance_hypothesis = 100
head_start_premise = 3
head_start_hypothesis = 3

# the hypothesis refers to the race distance and head start mentioned in the premise
if head_start_hypothesis != head_start_premise:
    # check if the head start in the hypothesis contradicts the head start reported in the premise
    label = "contradiction"
elif race_distance_hypothesis >= race_distance_premise:
    # check if the race distance in the hypothesis contradicts the phrase 'less than 100 m' in the hypothesis
    label = "contradiction"
else:
    # the premise gives only the exact distance of the race, but the hypothesis refers to a shorter race
    # so it's consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

