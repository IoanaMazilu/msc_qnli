percentage_children_premise = 50
percentage_black_children_premise = 90
percentage_children_hypothesis = 50
percentage_black_children_hypothesis = 90

# the hypothesis and premise mention the percentage of children and black children needing government assistance
if percentage_children_premise != percentage_children_hypothesis or percentage_black_children_premise != percentage_black_children_hypothesis:
    # check if the percentages in the hypothesis contradict the percentages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
