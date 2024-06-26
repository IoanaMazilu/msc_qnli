# define variables with representative names for the numerical entities in both inputs
shelf_capacity_premise = 4.0
number_of_cds_premise = 4.0
shelves_needed_hypothesis = 2.0
number_of_cds_hypothesis = 8.0

# extract all quantities as valid numbers (integers or floats)
shelf_capacity_premise = float(shelf_capacity_premise)
number_of_cds_premise = float(number_of_cds_premise)
shelves_needed_hypothesis = float(shelves_needed_hypothesis)
number_of_cds_hypothesis = float(number_of_cds_hypothesis)

# compare the variables
if shelves_needed_hypothesis > shelf_capacity_premise:
    # the hypothesis implies that more shelves are needed than what the premise states
    label = "contradiction"
elif number_of_cds_hypothesis > number_of_cds_premise:
    # the hypothesis implies that more CDs can fit on the shelf than what the premise states
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
