# define variables for the numerical entities in the premise and hypothesis
T_premise = 5/9 * (K-32)
T_hypothesis = more than 4/9 * (K-32)
K_premise = 32

# extract the numerical values from the premise and hypothesis
T_premise_value = float(T_premise)
T_hypothesis_value = float(T_hypothesis)

# compare the values of T in the premise and hypothesis
if T_premise_value <= T_hypothesis_value:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif T_hypothesis_value!= K_premise:
    # the hypothesis value contradicts the value of K reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
