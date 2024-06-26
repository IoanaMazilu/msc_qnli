season_2019 = 2019
season_2019_hypothesis = 100

# the hypothesis talks about the number of seasons the NHL has been around for, which is also mentioned in the premise
if season_2019!= season_2019_hypothesis:
    # check if the number of seasons the NHL has been around for in the hypothesis contradicts the number of seasons in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
