# Premise: Martha has 6 dogs and 4 cats.
# Hypothesis: Martha has 3 dogs and 4 cats.
# Golden Label: contradiction

dogs_premise = 6
cats_premise = 4
dogs_hypothesis = 3
cats_hypothesis = 4

# the hypothesis refers to the number of dogs and cats Martha has, as stated in the premise
if dogs_hypothesis > dogs_premise:
    # check if the number of dogs in the hypothesis contradicts the number of dogs in the premise
    label = "contradiction"
elif cats_hypothesis != cats_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, then it's either entailment or neutral
    if dogs_hypothesis == dogs_premise:
        # if the number of dogs in the hypothesis is equal to the number of dogs in the premise, then it's entailment
        label = "entailment"
    else:
        # otherwise, it's neutral
        label = "neutral"

print(label)

