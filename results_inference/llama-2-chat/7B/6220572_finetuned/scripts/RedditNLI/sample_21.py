# the premise and hypothesis mention the percentage of children in need of government assistance
# the hypothesis also mentions the race of children, which is not mentioned in the premise
if percentage_of_children_premise!= percentage_of_children_hypothesis:
    # check if the percentage of children in need of government assistance in the hypothesis contradicts the percentage of children in need of government assistance in the premise
    label = "contradiction"
elif percentage_of_black_children_hypothesis!= 90:
    # check if the percentage of black children in need of government assistance in the hypothesis contradicts the percentage of black children in need of government assistance in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of children in need of government assistance
    # any estimate of the percentage in the hypothesis greater or equal to 'percentage_of_children_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
