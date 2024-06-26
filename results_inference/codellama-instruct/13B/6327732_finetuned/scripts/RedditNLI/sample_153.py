# define variables for the numerical entities in the premise and hypothesis
premise_rate = 100
hypothesis_rate = 25

# check if the rate in the hypothesis contradicts the rate in the premise
if hypothesis_rate < premise_rate:
    label = "contradiction"
else:
    label = "neutral"

print(label)
