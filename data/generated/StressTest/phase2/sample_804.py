# Premise: Chang Li has pet cockroaches that multiply at the same rate every week. The first week he had 5, the next week he had 10, the second week he had 20, and the fourth week he had 80.
# Hypothesis: Chang Li has pet cockroaches that multiply at the same rate every week. The first week he had less than 7, the next week he had 10, the second week he had 20, and the fourth week he had 80.
# Golden Label: entailment

first_week_premise = 5
second_week_premise = 10
third_week_premise = 20
fourth_week_premise = 80

first_week_hypothesis = 7
second_week_hypothesis = 10
third_week_hypothesis = 20
fourth_week_hypothesis = 80

# the hypothesis refers to the number of Li's pet cockroaches in the first, second, third, and fourth weeks, also mentioned in the premise
if first_week_premise >= first_week_hypothesis:
    # check if the estimate of 'first_week_hypothesis' contradicts the number of cockroaches in the first week reported in the premise
    label = "contradiction"
elif second_week_hypothesis != second_week_premise or third_week_hypothesis != third_week_premise or fourth_week_hypothesis != fourth_week_premise:
    # check if the number of cockroaches in the second, third, and fourth weeks in the hypothesis contradicts the number of cockroaches in the second, third, and fourth weeks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

