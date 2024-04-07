# Premise: Mona and Sona go around a circular track of length 400 m on a bike at speeds of 18 kmph and 36 kmph.
# Hypothesis: Mona and Sona go around a circular track of length less than 400 m on a bike at speeds of 18 kmph and 36 kmph.
# Golden Label: contradiction

track_length_premise = 400
track_length_hypothesis = 400
mona_speed_premise = 18
mona_speed_hypothesis = 18
sona_speed_premise = 36
sona_speed_hypothesis = 36

# the hypothesis refers to the track length and the speeds of Mona and Sona mentioned in the premise
if track_length_hypothesis >= track_length_premise:
    # check if the track length in the hypothesis contradicts the track length in the premise
    label = "contradiction"
elif mona_speed_hypothesis != mona_speed_premise or sona_speed_hypothesis != sona_speed_premise:
    # check if the speeds of Mona or Sona in the hypothesis contradict the speeds in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

