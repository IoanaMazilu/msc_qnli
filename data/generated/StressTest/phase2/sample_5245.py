# Premise: In a less than 200 m sprint race Kelly was given a 3 m head start by Abel.
# Hypothesis: In a 100 m sprint race Kelly was given a 3 m head start by Abel.
# Golden Label: neutral

race_length_premise = 200
race_length_hypothesis = 100
head_start_premise = 3
head_start_hypothesis = 3

# the hypothesis refers to the length of a race and the head start given to Kelly, as mentioned in the premise
if race_length_hypothesis > race_length_premise:
    # check if the length of race in hypothesis contradicts the length of race in premise
    label = "contradiction"
elif head_start_hypothesis != head_start_premise:
    # check if the head start given in hypothesis contradicts the head start given in premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

