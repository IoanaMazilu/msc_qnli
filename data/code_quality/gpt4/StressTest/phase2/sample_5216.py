boys_percentage_premise = 50
boys_percentage_hypothesis = 10

# the hypothesis talks about the percentage of boys in the total school population, referenced also in the premise
if boys_percentage_hypothesis != boys_percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
