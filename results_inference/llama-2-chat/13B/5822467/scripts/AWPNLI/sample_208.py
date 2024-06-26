premise_pizzas = 21.0
premise_slices_per_pizza = 8.0
hypothesis_slices = 168.0

# extract numerical values from the premise
premise_total_slices = premise_slices_per_pizza * premise_pizzas

# compare the total number of slices in the hypothesis to the total number of slices in the premise
if hypothesis_slices!= premise_total_slices:
    # if the number of slices in the hypothesis contradicts the number of slices in the premise, label as contradiction
    label = "contradiction"
else:
    # if the number of slices in the hypothesis and premise are the same, label as entailment
    label = "entailment"

print(label)
