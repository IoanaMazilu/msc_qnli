black_balloons_nancy_premise = 7.0
multiplier_mary_premise = 4.0
black_balloons_mary_hypothesis = 24.0

# the hypothesis refers to the number of black balloons Mary has, which is also mentioned in the premise
# compute the number of black balloons Mary has in the premise
black_balloons_mary_premise = black_balloons_nancy_premise * multiplier_mary_premise
if black_balloons_mary_hypothesis != black_balloons_mary_premise:
    # check if the number of black balloons Mary has in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
