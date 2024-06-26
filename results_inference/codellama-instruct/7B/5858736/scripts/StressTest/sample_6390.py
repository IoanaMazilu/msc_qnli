sacha_speed_premise = 6
sacha_speed_hypothesis = 1
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

if sacha_speed_hypothesis <= sacha_speed_premise:
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
