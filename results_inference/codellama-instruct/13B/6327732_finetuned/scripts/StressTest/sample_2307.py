# define variables for the numerical entities in the premise and hypothesis
premise_speed = 10
hypothesis_speed = 20
premise_hours = 3
hypothesis_hours = 5

# check if the hypothesis value contradicts the premise value
if hypothesis_speed <= premise_speed:
    # the hypothesis value is less than or equal to the premise value, which contradicts the idea of doubling the speed
    label = "contradiction"
elif hypothesis_hours >= premise_hours:
    # the hypothesis value is greater than or equal to the premise value, which contradicts the idea of cleaning the house in less than 5 hours
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise values, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
