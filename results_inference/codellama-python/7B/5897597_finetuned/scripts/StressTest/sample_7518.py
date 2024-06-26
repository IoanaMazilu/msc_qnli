boys_percentage_premise = 30
boys_percentage_hypothesis = 10

# the hypothesis refers to the percentage of boys in the total school population, mentioned in the premise
if boys_percentage_premise <= boys_percentage_hypothesis:
    # check if the estimate of 'boys_percentage_hypothesis' contradicts the percentage of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
