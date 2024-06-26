# define variables for the numerical entities in the premise and hypothesis
premise_speed = 1
hypothesis_speed = 2
premise_hours = 3
hypothesis_hours = 5

# check if the hypothesis value contradicts the premise value
if hypothesis_speed <= premise_speed:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis_hours < premise_hours:
    # the hypothesis value is less than the premise value
    label = "entailment"
else:
    # the hypothesis value is greater than the premise value
    label = "neutral"

print(label)
