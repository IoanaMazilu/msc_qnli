# Premise: Marlee has 3.0 tables for her Halloween party and each table will hold 12.0 guests.
# Hypothesis: She can invite 36.0 guests.
# Golden Label: entailment

tables_premise = 3.0
guests_per_table_premise = 12.0
total_guests_hypothesis = 36.0

# the hypothesis refers to the number of guests, which is also mentioned in the premise
# compute the total number of guests that the tables can hold in the premise
total_guests_premise = tables_premise * guests_per_table_premise
if total_guests_hypothesis != total_guests_premise:
    # check if the number of guests in the hypothesis contradicts the number of guests from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
