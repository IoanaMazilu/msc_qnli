percentage_children_premise = 50
percentage_black_children_premise = 90
percentage_children_hypothesis = 50
percentage_black_children_hypothesis = 90

# the hypothesis and premise mention the percentage of children and black children who need government assistance to eat
if percentage_children_premise!= percentage_children_hypothesis:
    # check if the percentage of children in the hypothesis contradicts the percentage of children in the premise
    label = "contradiction"
elif percentage_black_children_premise!= percentage_black_children_hypothesis:
    # check if the percentage of black children in the hypothesis contradicts the percentage of black children in the premise
    label = "contradiction"
else:
    # the premise gives only estimates for the percentage of children and black children who need government assistance to eat
    # any estimate of the percentage in the hypothesis greater or equal to 'percentage_children_premise' and 'percentage_black_children_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
