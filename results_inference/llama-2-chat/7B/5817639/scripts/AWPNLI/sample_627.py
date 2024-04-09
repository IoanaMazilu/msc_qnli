guests_premise = 12.0
tables_premise = 3.0
guests_hypothesis = 37.0

# compare the number of guests in the hypothesis to the number of guests in the premise
if guests_hypothesis >= guests_premise:
    # check if the number of guests in the hypothesis contradicts the number of guests in the premise
    label = "contradiction"
elif tables_hypothesis!= tables_premise:
    # check if the number of tables in the hypothesis contradicts the number of tables in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
