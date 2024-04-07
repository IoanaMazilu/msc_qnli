# Premise: Jack walks in a straight line toward Christina at a constant speed of 5 feet per second and Christina walks in a straight line toward Jack at a constant speed of 3 feet per second.
# Hypothesis: Jack walks in a straight line toward Christina at a constant speed of less than 5 feet per second and Christina walks in a straight line toward Jack at a constant speed of 3 feet per second.
# Golden Label: contradiction

speed_jack_premise = 5
speed_jack_hypothesis = 5
speed_christina_premise = 3
speed_christina_hypothesis = 3

# the hypothesis refers to the speed of Jack and Christina walking towards each other, mentioned in the premise
if speed_jack_hypothesis >= speed_jack_premise:
    # check if the estimate of 'speed_jack_hypothesis' contradicts the speed of Jack in the premise
    label = "contradiction"
elif speed_christina_hypothesis != speed_christina_premise:
    # check if the speed of Christina in the hypothesis contradicts the speed of Christina reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

