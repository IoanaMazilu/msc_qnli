sailors_premise = 15
damaged_vessels_premise = 2

# define variables for the hypothesis
sailors_hypothesis = 15
damaged_vessels_hypothesis = 2

# compare the values of the variables
if sailors_hypothesis == sailors_premise and damaged_vessels_hypothesis == damaged_vessels_premise:
    # if the values of the variables are the same, there is no contradiction or entailment
    label = "neutral"
else:
    # if the values of the variables are different, check for contradiction or entailment
    if sailors_hypothesis!= sailors_premise:
        # if the number of slightly hurt sailors in the hypothesis differs from the premise, there is a contradiction
        label = "contradiction"
    elif damaged_vessels_hypothesis!= damaged_vessels_premise:
        # if the number of damaged vessels in the hypothesis differs from the premise, there is a contradiction
        label = "contradiction"
    else:
        # if there is no contradiction, we can infer entailment
        label = "entailment"

print(label)
