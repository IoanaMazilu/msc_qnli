invited_people_premise = 18.0
additional_people_premise = 12.0
 tables_premise = 3.0
tables_hypothesis = 10.0

# the hypothesis refers to the number of tables, which are not mentioned in the premise
# compute the total number of tables needed from the premise
tables_needed_premise = additional_people_premise / tables_premise
if tables_needed_hypothesis!= tables_needed_premise:
    # check if the number of tables in the hypothesis contradicts the number of tables needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
