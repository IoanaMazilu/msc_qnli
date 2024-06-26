# define variables for the numerical entities in the premise
rupee_premise = 65.36
sensex_premise = 17685.58
nifty_premise = 282.50

# define variables for the numerical entities in the hypothesis
rupee_hypothesis = 68.19
sensex_hypothesis = 17685.58
nifty_hypothesis = 282.50

# check if the rupee value in the hypothesis contradicts the premise value
if rupee_hypothesis < rupee_premise:
    label = "contradiction"
else:
    # check if the sensex value in the hypothesis contradicts the premise value
    if sensex_hypothesis > sensex_premise:
        label = "contradiction"
    else:
        # check if the nifty value in the hypothesis contradicts the premise value
        if nifty_hypothesis > nifty_premise:
            label = "contradiction"
        else:
            # if the values in the hypothesis do not contradict the premise values, we can infer entailment
            label = "entailment"

print(label)
