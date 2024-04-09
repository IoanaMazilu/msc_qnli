percentage_children_needing_assistance_premise = 50
percentage_black_children_needing_assistance_premise = 90
percentage_children_needing_assistance_hypothesis = 50
percentage_black_children_needing_assistance_hypothesis = 90

# the hypothesis and premise mention the percentage of children and black children that need government assistance
if percentage_children_needing_assistance_hypothesis!= percentage_children_needing_assistance_premise:
    # check if the percentage of children needing assistance in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif percentage_black_children_needing_assistance_hypothesis!= percentage_black_children_needing_assistance_premise:
    # check if the percentage of black children needing assistance in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
