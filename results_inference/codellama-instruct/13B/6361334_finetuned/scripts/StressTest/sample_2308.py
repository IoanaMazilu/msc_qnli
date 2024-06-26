# define variables for the numerical entities in the premise and hypothesis
premise_speed = 1
hypothesis_speed = 2
premise_hours = 5
hypothesis_hours = 3

# check if the hypothesis value contradicts the premise value
if hypothesis_speed!= premise_speed:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis_hours <= premise_hours:
    # the hypothesis value does not contradict the premise value, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value does not contradict the premise value and can be explicitly entailed from the premise
    label = "entailment"

print(label)
