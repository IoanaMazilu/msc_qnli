# Premise: Wendy uploaded 79.0 pictures to Facebook on Monday and she uploaded 44.0 pictures to Facebook on Tuesday, then split all the pictures into 5.0 different albums.
# Hypothesis: 24.6 pictures were in each album.
# Golden Label: entailment

uploaded_pictures_monday_premise = 79.0
uploaded_pictures_tuesday_premise = 44.0
pictures_per_album_hypothesis = 24.6
albums_premise = 5.0

# the hypothesis refers to the number of pictures per album, which is also referenced in the premise
# compute the total number of pictures from the premise
total_pictures_premise = uploaded_pictures_monday_premise + uploaded_pictures_tuesday_premise

# compute the average number of pictures per album from the premise
average_pictures_per_album_premise = total_pictures_premise / albums_premise

if pictures_per_album_hypothesis != average_pictures_per_album_premise:
    # check if the number of pictures per album in the hypothesis contradicts the number of pictures per album from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

