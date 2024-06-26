bread_dinner_premise = 140
bread_dinner_hypothesis = 240

# the hypothesis talks about the amount of bread eaten by Cara for dinner, referenced also in the premise
if bread_dinner_hypothesis <= bread_dinner_premise:
    # check if the hypothesis value contradicts the estimate of more than 'bread_dinner_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of bread eaten
    # any amount of bread greater than 'bread_dinner_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
