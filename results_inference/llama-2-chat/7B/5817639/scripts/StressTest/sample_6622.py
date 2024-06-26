# define variables for the premise and hypothesis
premise_people = 7
hypothesis_people = 4

# compare the number of people in the hypothesis to the premise
if hypothesis_people < premise_people:
    # check if the number of people in the hypothesis contradicts the premise
    label = "contradiction"
elif hypothesis_people == premise_people:
    # if the number of people in the hypothesis matches the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of people in the hypothesis is greater than the premise, it is neutral
    label = "neutral"

print(label)
