# define variables for the numerical entities in the premise and hypothesis
premise_temperature = 40
hypothesis_temperature = 40

# check if the temperature in the hypothesis contradicts the temperature reported in the premise
if hypothesis_temperature!= premise_temperature:
    label = "contradiction"
else:
    label = "neutral"

print(label)
