# Premise: Robin uploaded 35.0 pictures from her phone and 5.0 from her camera to facebook, and she sorted the pics into 5.0 different albums with the same amount of pics in each album.
# Hypothesis: 8.0 pictures were in each of the albums.
# Golden Label: entailment

phone_pictures_premise = 35.0
camera_pictures_premise = 5.0
albums_premise = 5.0
pictures_per_album_hypothesis = 8.0

# the hypothesis refers to the number of pictures per album, which is also mentioned in the premise
# compute the total number of pictures in the premise
total_pictures_premise = phone_pictures_premise + camera_pictures_premise
# compute the number of pictures per album in the premise
pictures_per_album_premise = total_pictures_premise / albums_premise

if pictures_per_album_hypothesis != pictures_per_album_premise:
    # check if the number of pictures per album in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

