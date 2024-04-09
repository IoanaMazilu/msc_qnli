# define variables with representative names for the numerical entities in both inputs
consumable_premise = 60
clothes_transport_premise = 50
remaining_premise = 40

# extract all quantities as valid numbers (integers or floats)
consumable_hypothesis = float(input("Enter the percentage of monthly salary spent on consumable items (hypothesis): "))
clothes_transport_hypothesis = float(input("Enter the percentage of remaining monthly salary spent on clothes and transport (hypothesis): "))

# compare the variables
if consumable_hypothesis > consumable_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif clothes_transport_hypothesis > clothes_transport_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
