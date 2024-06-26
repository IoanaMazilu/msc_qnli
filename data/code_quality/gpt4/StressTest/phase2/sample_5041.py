height_empire_premise = 864
height_petronas_premise = 472
height_empire_hypothesis = 464
height_petronas_hypothesis = 472

# the hypothesis refers to the heights of the two buildings mentioned in the premise
if height_empire_premise < height_empire_hypothesis:
    # check if the height of Empire State Building in the hypothesis contradicts the maximum height given in the premise
    label = "contradiction"
elif height_petronas_premise != height_petronas_hypothesis:
    # check if the height of Petronas Towers in the hypothesis contradicts the height given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
