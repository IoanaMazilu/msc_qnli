leo_gain_premise = 10
leo_gain_hypothesis = 20
percentage_difference = 50

# the hypothesis mentions a weight gain condition for Leo that is also referred in the premise
if not (leo_gain_hypothesis > leo_gain_premise):
    # check if the hypothesis contradicts the premise by proposing a weight gain for Leo that is less than or equal to 'leo_gain_premise'
    label = "contradiction"
elif leo_gain_hypothesis == leo_gain_premise:
    # if the weight gain in the hypothesis is equal to 'leo_gain_premise', we can infer entailment
    label = "entailment"
else:
    # any weight gain for Leo greater than 'leo_gain_premise' will not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
