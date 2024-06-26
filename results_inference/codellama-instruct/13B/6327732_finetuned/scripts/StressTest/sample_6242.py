# define variables for the numerical entities in the premise
ratio_premise = 144
ratio_hypothesis = 244
bc_premise = 13
bc_hypothesis = 13

# check if the ratio in the hypothesis contradicts the ratio in the premise
if ratio_hypothesis!= ratio_premise:
    label = "contradiction"
# check if the value of BC in the hypothesis contradicts the value of BC in the premise
elif bc_hypothesis!= bc_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
