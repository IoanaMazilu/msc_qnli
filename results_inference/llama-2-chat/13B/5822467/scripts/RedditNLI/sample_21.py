# define variables with representative names for the numerical entities in both inputs
percentage_of_children_premise = 50
percentage_of_black_children_premise = 90
percentage_of_children_hypothesis = 50
percentage_of_black_children_hypothesis = 90

# extract all quantities as valid numbers (integers or floats)
premise_quantities = [percentage_of_children_premise, percentage_of_black_children_premise]
hypothesis_quantities = [percentage_of_children_hypothesis, percentage_of_black_children_hypothesis]

# compare the quantities in the premise and hypothesis
comparison_labels = []
for premise_quantity, hypothesis_quantity in zip(premise_quantities, hypothesis_quantities):
    if hypothesis_quantity > premise_quantity:
        comparison_labels.append("entailment")
    elif hypothesis_quantity < premise_quantity:
        comparison_labels.append("contradiction")
    else:
        comparison_labels.append("neutral")

# print the comparison labels
print("Comparison labels:", comparison_labels)
