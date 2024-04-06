# Premise: Never forget the USA is the best in everything... except for the part where 50% of children and 90% of black children need government assistance to eat.
# Hypothesis: The US is quickly becoming a 3rd world country. 50% of all children and 90% of black children need government assistance to eat.
# Golden Label: entailment

percentage_children_premise = 50
percentage_black_children_premise = 90
percentage_children_hypothesis = 50
percentage_black_children_hypothesis = 90

# the hypothesis and premise mention the percentage of children and black children who need government assistance to eat
if percentage_children_premise != percentage_children_hypothesis:
    # check if the percentage of children in the hypothesis contradicts the percentage of children in the premise
    label = "contradiction"
elif percentage_black_children_premise != percentage_black_children_hypothesis:
    # check if the percentage of black children in the hypothesis contradicts the percentage of black children in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but the premise does not entail the claim about the US becoming a 3rd world country
    label = "neutral"

print(label)

