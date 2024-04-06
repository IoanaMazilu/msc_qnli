# Premise: Robin uploaded 35.0 pictures from her phone and 5.0 from her camera to facebook, and she sorted the pics into 5.0 different albums with the same amount of pics in each album.
# Hypothesis: 6.0 pictures were in each of the albums.
# Golden Label: contradiction

pictures_phone_premise = 35.0
pictures_camera_premise = 5.0
albums_premise = 5.0
pictures_per_album_hypothesis = 6.0

# the hypothesis talks about the number of pictures in each album, which are also referenced in the premise
# find the total number of pictures uploaded and the number of pictures per album from the premise
total_pictures_premise = pictures_phone_premise + pictures_camera_premise
pictures_per_album_premise = total_pictures_premise / albums_premise

if pictures_per_album_hypothesis != pictures_per_album_premise:
    # check if the number of pictures per album in the hypothesis contradicts the number of pictures per album in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

