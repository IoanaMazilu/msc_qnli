invited_people_premise = 18.0
showed_up_people_premise = 12.0
tables_per_table_premise = 3.0
tables_needed_hypothesis = 10.0

# the hypothesis refers to the number of tables needed, which are also mentioned in the premise
# compute the total number of people from the premise
total_people_premise = invited_people_premise + showed_up_people_premise
# compute the total number of tables from the premise
total_tables_premise = total_people_premise / tables_per_table_premise
if total_tables_hypothesis!= total_tables_premise:
    # check if the number of tables in the hypothesis contradicts the number of tables from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
