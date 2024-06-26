num_invited_premise = 18.0
num_showed_up_premise = 12.0
num_tables_premise = 3.0
num_tables_hypothesis = 10.0

# the hypothesis refers to the number of tables, which are also mentioned in the premise
# compute the total number of people from the premise
total_people_premise = num_invited_premise + num_showed_up_premise
if total_people_premise / num_tables_premise!= num_tables_hypothesis:
    # check if the number of tables in the hypothesis contradicts the number of tables from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
