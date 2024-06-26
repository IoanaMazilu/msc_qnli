diane_paint_premise = 1
diane_paint_hypothesis = 0.5
room_size_premise = 1/3

# the hypothesis refers to the amount of paint found and the size of the room
if diane_paint_hypothesis <= room_size_premise:
    # check if the hypothesis value contradicts the estimate of 'room_size_premise'
    label = "contradiction"
elif diane_paint_premise!= room_size_premise:
    # check if the amount of paint found in the premise contradicts the amount of paint needed to paint the room
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
