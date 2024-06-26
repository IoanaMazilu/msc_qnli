police_premise = 21
demonstrator_premise = 1
arrested_premise = 5
hurt_premise = 21

# define variables for the hypothesis
arrested_hypothesis = 5
hurt_hypothesis = 21
protester_hypothesis = 1

# compare the variables
if arrested_hypothesis == arrested_premise and hurt_hypothesis == hurt_premise and protester_hypothesis == demonstrator_premise:
    # if all the values are the same, the hypothesis is neutral
    label = "neutral"
elif arrested_hypothesis!= arrested_premise or hurt_hypothesis!= hurt_premise or protester_hypothesis!= demonstrator_premise:
    # if any of the values are different, the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if all the values are different, the hypothesis does not entail the premise
    label = "neutral"

print(label)
