tables_premise = 3.0
guests_per_table_premise = 12.0
invitees_hypothesis = 37.0

# the hypothesis refers to the number of guests, which is related to the number of tables and guests per table in the premise
# compute the total number of guests that can be invited in the premise
total_guests_premise = tables_premise * guests_per_table_premise
if invitees_hypothesis!= total_guests_premise:
    # check if the number of guests in the hypothesis contradicts the number of guests that can be invited from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
