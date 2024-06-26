invited_people_premise = 18.0
absent_people_premise = 12.0
table_capacity_premise = 3.0
needed_tables_hypothesis = 5.0

# the hypothesis refers to the number of tables needed, which can be calculated from the number of people and table capacity mentioned in the premise
# calculate the number of people who showed up
showed_up_people_premise = invited_people_premise - absent_people_premise

# find the number of tables needed from the premise
needed_tables_premise = showed_up_people_premise / table_capacity_premise

if needed_tables_hypothesis != needed_tables_premise:
    # check if the number of tables needed in the hypothesis contradicts the calculated number of tables from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
