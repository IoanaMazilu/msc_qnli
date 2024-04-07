# Premise: Joe drives 180 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Hypothesis: Joe drives less than 180 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Golden Label: contradiction

first_distance_premise = 180  # distance driven at 60 miles per hour
second_distance_premise = 120  # distance driven at 40 miles per hour

first_distance_hypothesis = 180  # distance driven at 60 miles per hour according to the hypothesis
second_distance_hypothesis = 120  # distance driven at 40 miles per hour according to the hypothesis

# the hypothesis refers to the distances driven at different speeds as mentioned in the premise
if first_distance_hypothesis >= first_distance_premise:
    # check if the distance driven at 60 miles per hour according to the hypothesis contradicts the premise
    label = "contradiction"
elif second_distance_hypothesis != second_distance_premise:
    # check if the distance driven at 40 miles per hour according to the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the distances driven at different speeds according to the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

