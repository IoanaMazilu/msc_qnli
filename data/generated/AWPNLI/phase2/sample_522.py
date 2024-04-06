# Premise: Mrs. Hilt ate 5.0 apples in 3 hours.
# Hypothesis: She eats 1.66666666667 apples per hour on average.
# Golden Label: entailment

apples_premise = 5.0
hours_premise = 3
apples_per_hour_hypothesis = 1.66666666667

# The hypothesis refers to the average number of apples eaten per hour, which can be computed from the premise
# compute the average number of apples eaten per hour in the premise
apples_per_hour_premise = apples_premise / hours_premise
if apples_per_hour_hypothesis != apples_per_hour_premise:
    # check if the number of apples per hour in the hypothesis contradicts the number of apples per hour from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

