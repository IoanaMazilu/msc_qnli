pictures_monday_premise = 79.0
pictures_tuesday_premise = 44.0
albums_premise = 5.0
pictures_each_album_hypothesis = 20.1

# the hypothesis refers to the number of pictures in each album, which are also mentioned in the premise
# compute the total number of pictures and the average number of pictures in each album in the premise
total_pictures_premise = pictures_monday_premise + pictures_tuesday_premise
pictures_each_album_premise = total_pictures_premise / albums_premise

if pictures_each_album_hypothesis != pictures_each_album_premise:
    # check if the number of pictures in each album in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
