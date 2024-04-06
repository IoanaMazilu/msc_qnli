# Premise: Wendy uploaded 79.0 pictures to Facebook and she put 44.0 pics into 1.0 album and put the rest into 5.0 different albums.
# Hypothesis: 11.0 pictures were in each album.
# Golden Label: contradiction

uploaded_pictures_premise = 79.0
one_album_pictures_premise = 44.0
other_albums_premise = 5.0
pictures_each_album_hypothesis = 11.0

# the hypothesis refers to the number of pictures in each album, which is also mentioned in the premise
# compute the number of pictures in other albums from the premise
other_album_pictures_premise = uploaded_pictures_premise - one_album_pictures_premise
pictures_each_other_album_premise = other_album_pictures_premise / other_albums_premise
if pictures_each_album_hypothesis != pictures_each_other_album_premise:
    # check if the number of pictures in each album from the hypothesis contradicts the number of pictures in each album from the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate does not contradict the premise value, we can infer entailment
    label = "entailment"    

print(label)

