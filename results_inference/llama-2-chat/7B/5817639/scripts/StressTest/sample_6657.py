bet_distance_premise = 60
bet_distance_hypothesis = 80

# the hypothesis talks about the average speed of two drivers, referenced also in the premise
if bet_distance_hypothesis <= bet_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'bet_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance driven by Tom before Karen wins the bet
    # any distance driven by Tom consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
