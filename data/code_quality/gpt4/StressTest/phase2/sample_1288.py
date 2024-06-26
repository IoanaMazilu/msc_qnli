track_length_premise = 700
track_length_hypothesis = 400
speed_mona_premise = 18
speed_sona_premise = 36
speed_mona_hypothesis = 18
speed_sona_hypothesis = 36

# the hypothesis refers to the circular track length and the speed of Mona and Sona mentioned in the premise
if track_length_hypothesis >= track_length_premise:
    # check if the hypothesis value contradicts the estimate of less than 'track_length_premise'
    label = "contradiction"
elif speed_mona_hypothesis != speed_mona_premise or speed_sona_hypothesis != speed_sona_premise:
    # check if the speed of Mona or Sona in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the track length
    # any track length less than 'track_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
