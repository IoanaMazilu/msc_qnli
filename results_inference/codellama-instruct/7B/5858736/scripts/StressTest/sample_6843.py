sacha_speed_premise = 7
sacha_speed_hypothesis = 4
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

if sacha_speed_hypothesis <= sacha_speed_premise:
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
