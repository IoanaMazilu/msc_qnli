y = 9
b = 5

# the premise states the constant speed of Sacha and Bruno
# the hypothesis states a constant speed of Sacha more than 9 meters per second and a constant speed of Bruno equal to 5 meters per second

# compute the constant speed of Sacha in the hypothesis
speed_sacha_hypothesis = 9

# compute the constant speed of Bruno in the hypothesis
speed_bruno_hypothesis = 5

# check if the constant speed of Sacha in the hypothesis contradicts the constant speed of Sacha in the premise
if speed_sacha_hypothesis <= speed_sacha_premise:
    label = "contradiction"
elif speed_bruno_hypothesis!= speed_bruno_premise:
    # check if the constant speed of Bruno in the hypothesis contradicts the constant speed of Bruno in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
