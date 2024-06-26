# define variables with representative names for the numerical entities in both inputs
percentage_children_assistance_premise = 50
percentage_black_children_assistance_premise = 90
percentage_children_assistance_hypothesis = 50
percentage_black_children_assistance_hypothesis = 90

# extract all quantities as valid numbers (integers or floats)

# use brief comments to explain what comparison you do between the defined variables
if percentage_children_assistance_hypothesis!= percentage_children_assistance_premise:
    # check if the percentage of children in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif percentage_black_children_assistance_hypothesis!= percentage_black_children_assistance_premise:
    # check if the percentage of black children in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
