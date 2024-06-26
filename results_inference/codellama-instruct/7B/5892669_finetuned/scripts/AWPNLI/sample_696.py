invited_people_premise = 18.0
additional_people_premise = 12.0
table_capacity_premise = 3.0
needed_tables_hypothesis = 10.0

# the hypothesis refers to the number of tables needed, which can be inferred from the premise
# compute the total number of people who showed up in the premise
total_people_premise = invited_people_premise + additional_people_premise
# compute the number of tables needed in the premise
tables_needed_premise = total_people_premise / table_capacity_premise
if needed_tables_hypothesis!= tables_needed_premise:
    # check if the number of tables needed in the hypothesis contradicts the number of tables needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
