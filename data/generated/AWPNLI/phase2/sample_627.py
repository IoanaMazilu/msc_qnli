# Premise: Marlee has 3.0 tables for her Halloween party and each table will hold 12.0 guests.
# Hypothesis: She can invite 37.0 guests.
# Golden Label: contradiction

tables_premise = 3.0
guests_per_table_premise = 12.0
total_guests_hypothesis = 37.0

# the hypothesis implies a total number of guests, which can be estimated in the premise
# compute the total number of guests in the premise
total_guests_premise = tables_premise * guests_per_table_premise
if total_guests_hypothesis != total_guests_premise:
    # check if the number of guests in the hypothesis contradicts the number of guests from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

