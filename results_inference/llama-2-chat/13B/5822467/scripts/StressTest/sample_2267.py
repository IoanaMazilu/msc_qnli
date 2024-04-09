andy_gloves_premise = 20
andy_gloves_hypothesis = float(input("Enter the number of pairs of matched gloves Andy has: "))

# the hypothesis refers to the number of pairs of gloves owned by Andy
if andy_gloves_premise <= andy_gloves_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'andy_gloves_premise'
    label = "contradiction"
elif andy_gloves_hypothesis > andy_gloves_premise:
    # check if the number of pairs of gloves in the hypothesis contradicts the number of pairs of gloves reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
