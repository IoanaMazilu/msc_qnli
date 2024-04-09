tables_premise = 3.0
guests_per_table_premise = 12.0
total_guests_hypothesis = 37.0

# the hypothesis refers to the total number of guests, which can be calculated from the premise
# compute the total number of guests that the tables can hold in the premise
total_guests_premise = tables_premise * guests_per_table_premise
if total_guests_hypothesis!= total_guests_premise:
    # check if the total number of guests in the hypothesis contradicts the total number of guests from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
