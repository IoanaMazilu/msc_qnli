# define variables for the numerical entities in the premise and hypothesis
premise_speed = 10
hypothesis_speed = 20
premise_hours = 5
hypothesis_hours = 3

# check if the hypothesis value contradicts the premise value
if hypothesis_speed <= premise_speed:
    # the hypothesis value is less than or equal to the premise value, which contradicts the premise
    label = "contradiction"
elif hypothesis_hours >= premise_hours:
    # the hypothesis value is greater than or equal to the premise value, which entails the premise
    label = "entailment"
else:
    # the hypothesis value is between the premise value and the premise estimate, which is neutral
    label = "neutral"

print(label)
