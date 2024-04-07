# Premise: In a 100 m sprint race Kelly was given a 3 m head start by Abel.
# Hypothesis: In a less than 200 m sprint race Kelly was given a 3 m head start by Abel.
# Golden Label: entailment

race_length_premise = 100
race_length_hypothesis = 200
head_start_premise = 3
head_start_hypothesis = 3

# the hypothesis talks about the length of the race and the head start given to Kelly, which are also mentioned in the premise
if race_length_premise > race_length_hypothesis:
    # check if the length of the race in the premise contradicts the maximum length in the hypothesis
    label = "contradiction"
elif head_start_premise != head_start_hypothesis:
    # check if the head start given to Kelly in the premise contradicts the one in the hypothesis
    label = "contradiction"
else:
    # if neither the length of the race nor the head start contradicts the premise, we can infer entailment
    label = "entailment"

print(label)

