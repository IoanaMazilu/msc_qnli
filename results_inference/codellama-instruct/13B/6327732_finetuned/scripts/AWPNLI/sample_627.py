tables_premise = 3.0
guests_per_table_premise = 12.0
total_guests_premise = tables_premise * guests_per_table_premise

guests_hypothesis = 37.0

if guests_hypothesis > total_guests_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
