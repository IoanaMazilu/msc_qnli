invited_people_premise = 18.0
additional_people_premise = 12.0
people_per_table_premise = 3.0
tables_hypothesis = 10.0

# the hypothesis refers to the number of tables needed, which can be estimated from the premise
# compute the total number of people who showed up at the luncheon in the premise
total_people_premise = invited_people_premise + additional_people_premise

# compute the number of tables needed in the premise
tables_premise = total_people_premise / people_per_table_premise

if tables_hypothesis!= tables_premise:
    # check if the number of tables in the hypothesis contradicts the number of tables from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
