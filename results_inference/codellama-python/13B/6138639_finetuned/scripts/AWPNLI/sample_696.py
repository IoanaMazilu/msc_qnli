invited_people_premise = 18.0
more_people_premise = 12.0
tables_per_person_premise = 3.0
tables_hypothesis = 10.0

# the hypothesis refers to the number of tables, which can be inferred from the premise
# compute the total number of tables in the premise
total_tables_premise = invited_people_premise + more_people_premise
total_tables_premise = total_tables_premise * tables_per_person_premise
if tables_hypothesis!= total_tables_premise:
    # check if the number of tables in the hypothesis contradicts the number of tables from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
