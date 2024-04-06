# Premise: Mrs. Hilt ate 5.0 apples in hours.
# Hypothesis: She eats 3.6 apples per hour on average.
# Golden Label: contradiction

total_apples_premise = 5.0
average_apples_per_hour_hypothesis = 3.6

# the hypothesis mentions an average number of apples per hour, which is not explicitly mentioned in the premise
# since we don't have information about the number of hours in the premise, we can't calculate the average
# hence, no comparison can be made and the relation is neutral

label = "neutral"

print(label)

