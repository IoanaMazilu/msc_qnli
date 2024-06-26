men_employed_premise = 700
men_employed_hypothesis = 100
highway_len_premise = highway_len_hypothesis = 2
days_premise = days_hypothesis = 50
hours_worked_premise = hours_worked_hypothesis = 8

# the hypothesis refers to the same work details mentioned in the premise
if men_employed_hypothesis >= men_employed_premise:
    # check if the number of men employed in the hypothesis contradicts the number of men employed in the premise
    label = "contradiction"
elif highway_len_hypothesis != highway_len_premise or days_hypothesis != days_premise or hours_worked_hypothesis != hours_worked_premise:
    # check if the work details (highway length, number of days or hours worked) in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and details do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
