tables_premise = 3.0
guests_per_table_premise = 12.0
guests_hypothesis = 37.0

# the hypothesis refers to the number of guests, which are also mentioned in the premise
# compute the total number of guests from the premise
total_guests_premise = tables_premise * guests_per_table_premise
if guests_hypothesis > total_guests_premise:
    # check if the number of guests in the hypothesis exceeds the total number of guests from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not exceed the premise values, we can infer entailment
    label = "entailment"

print(label)
