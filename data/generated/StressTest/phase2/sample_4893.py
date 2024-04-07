# Premise: Jane can make a handcrafted drum in 4 weeks.
# Hypothesis: Jane can make a handcrafted drum in less than 6 weeks.
# Golden Label: entailment

drum_make_time_premise = 4
drum_make_time_hypothesis = 6

# the hypothesis refers to the time Jane needs to make a drum, also mentioned in the premise
if drum_make_time_premise > drum_make_time_hypothesis:
    # check if the time in the premise contradicts the estimate of less than 'drum_make_time_hypothesis'
    label = "contradiction"
elif drum_make_time_premise == drum_make_time_hypothesis:
    # if the time in the premise is the same as the one estimated in the hypothesis, we can't infer entailment because the hypothesis specifically mentions 'less than'
    label = "contradiction"
else:
    # if the time in the premise is less than the one estimated in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

