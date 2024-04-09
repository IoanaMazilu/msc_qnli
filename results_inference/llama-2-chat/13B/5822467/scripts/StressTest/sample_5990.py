mpg_premise = 32
mpg_hypothesis = 82

# the hypothesis refers to the fuel efficiency of Dan's car, mentioned in the premise
if mpg_premise <= mpg_hypothesis:
    # check if the estimate of'mpg_hypothesis' contradicts the fuel efficiency reported in the premise
    label = "contradiction"
elif mpg_hypothesis!= mpg_premise:
    # check if the fuel efficiency in the hypothesis contradicts the fuel efficiency reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
