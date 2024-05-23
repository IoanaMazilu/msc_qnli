percentage_children_premise = 50
percentage_children_hypothesis = 50
percentage_black_children_premise = 90
percentage_black_children_hypothesis = 90

# the hypothesis and premise mention the percentage of children and black children that need government assistance
if percentage_children_premise!= percentage_children_hypothesis:
    # check if the percentage of children in the hypothesis contradicts the percentage of children in the premise
    label = "contradiction"
elif percentage_black_children_premise!= percentage_black_children_hypothesis:
    # check if the percentage of black children in the hypothesis contradicts the percentage of black children in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are identical
    label = "entailment"

print(label)