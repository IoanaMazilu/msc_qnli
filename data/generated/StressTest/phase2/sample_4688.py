# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 72, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 42, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

initial_avg_shirts_premise = 72
initial_avg_shirts_hypothesis = 42
added_shirts_each = 12

# The hypothesis refers to the average number of shirts initially owned by the three persons, and the number of shirts they purchased, both mentioned in the premise
if initial_avg_shirts_hypothesis != initial_avg_shirts_premise:
    # Check if the initial average number of shirts in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif added_shirts_each != 12:
    # Check if the number of shirts each person purchased in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

