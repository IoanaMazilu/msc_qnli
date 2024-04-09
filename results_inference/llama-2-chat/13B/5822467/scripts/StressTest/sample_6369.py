paint_cans_premise = 4
paint_cans_hypothesis = 8
room_size_premise = 1/3

# the hypothesis talks about the number of cans of paint needed for one third of the room
if paint_cans_hypothesis <= paint_cans_premise:
    # check if the hypothesis value contradicts the estimate of 'paint_cans_premise'
    label = "contradiction"
elif paint_cans_hypothesis > room_size_premise * paint_cans_premise:
    # check if the hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the number of cans of paint needed
    # any number of cans less than 'paint_cans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
