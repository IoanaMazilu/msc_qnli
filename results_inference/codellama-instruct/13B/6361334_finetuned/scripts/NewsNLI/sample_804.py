# define variables for the number of bombs in Karbala and Baghdad
bombs_karbala = 2
bombs_baghdad = 1

# check if the number of bombs in Karbala contradicts the number of bombs in the premise
if bombs_karbala!= 2:
    label = "contradiction"
# check if the number of bombs in Baghdad contradicts the number of bombs in the premise
elif bombs_baghdad!= 1:
    label = "contradiction"
# if the number of bombs in both locations do not contradict the premise, we can infer neutrality
else:
    label = "neutral"

print(label)
