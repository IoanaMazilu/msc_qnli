# Premise: Mona and Sona go around a circular track of length 400 m on a bike at speeds of 18 kmph and 36 kmph.
# Hypothesis: Mona and Sona go around a circular track of length less than 700 m on a bike at speeds of 18 kmph and 36 kmph.
# Golden Label: entailment

track_length_premise = 400
track_length_hypothesis = 700
mona_speed_premise = 18
mona_speed_hypothesis = 18
sona_speed_premise = 36
sona_speed_hypothesis = 36

# the hypothesis refers to the track length and speeds of Mona and Sona mentioned in the premise
if track_length_premise >= track_length_hypothesis:
    # check if the track length in the premise contradicts the estimate of 'track_length_hypothesis'
    label = "contradiction"
elif mona_speed_premise != mona_speed_hypothesis or sona_speed_premise != sona_speed_hypothesis:
    # check if the speed of Mona or Sona in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

