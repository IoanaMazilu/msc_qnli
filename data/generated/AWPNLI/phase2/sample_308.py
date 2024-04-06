# Premise: A company invited 18.0 people to a luncheon, but 12.0 of them didn't show up, and the tables they had held 3.0 people each.
# Hypothesis: They need 2.0 tables.
# Golden Label: entailment

people_invited_premise = 18.0
people_absent_premise = 12.0
table_capacity_premise = 3.0
tables_needed_hypothesis = 2.0

# the hypothesis talks about the number of tables needed, which can be computed from the premise
# compute the number of people who showed up
people_present_premise = people_invited_premise - people_absent_premise

# compute the number of tables needed
tables_needed_premise = people_present_premise / table_capacity_premise
if tables_needed_hypothesis != tables_needed_premise:
    # check if the number of tables in the hypothesis contradicts the number of tables computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

