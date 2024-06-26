# define variables for the numerical entities in the premise and hypothesis
premise_civilians_killed = 200000
premise_alleged_war_crimes = 5

hypothesis_civilians_killed = 200000

# the hypothesis talks about the number of civilians killed in the air attack, which is also mentioned in the premise
if hypothesis_civilians_killed!= premise_civilians_killed:
    # check if the number of civilians killed in the hypothesis contradicts the number of civilians killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
