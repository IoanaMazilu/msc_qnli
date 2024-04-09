# define variables for the premise and hypothesis
premise_T = 105
hypothesis_T = 5/9 * (K - 32)

# compare the values of T in the premise and hypothesis
if hypothesis_T >= premise_T:
    # check if the hypothesis value contradicts the estimate of T in the premise
    label = "contradiction"
elif hypothesis_T < premise_T:
    # check if the hypothesis value entails the estimate of T in the premise
    label = "entailment"
else:
    # if the hypothesis value is neutral with respect to the estimate of T in the premise, we can infer neutrality
    label = "neutral"

print(label)
