paint_premise = 2
paint_hypothesis = 1
room_size_premise = 1/3

# the hypothesis refers to the amount of paint needed to paint one third of the room
if paint_hypothesis <= room_size_premise:
    # check if the hypothesis value contradicts the estimate of less than 2 cans needed to paint one third of the room
    label = "contradiction"
elif paint_hypothesis!= paint_premise:
    # check if the amount of paint in the hypothesis contradicts the amount of paint reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer neutrality
    label = "neutral"

print(label)
