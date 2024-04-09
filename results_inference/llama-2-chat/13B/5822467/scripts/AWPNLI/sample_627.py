tables_premise = 3.0
guests_per_table_premise = 12.0
total_guests_hypothesis = 37.0

# the hypothesis refers to the total number of guests, which is also mentioned in the premise
# compute the total number of guests that can be accommodated by the premise
total_guests_premise = guests_per_table_premise * tables_premise

if total_guests_hypothesis > total_guests_premise:
    # check if the total number of guests in the hypothesis contradicts the number of guests that can be accommodated by the premise
    label = "contradiction"
elif total_guests_hypothesis == total_guests_premise:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
else:
    # if the number of guests in the hypothesis is less than the number of guests that can be accommodated by the premise, we can infer entailment
    label = "entailment"

print(label)
