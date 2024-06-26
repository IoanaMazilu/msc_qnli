stretch_time_premise = 78
stretch_time_hypothesis = 18

# the hypothesis talks about the time Jim takes to stretch, which is also mentioned in the premise
if stretch_time_hypothesis >= stretch_time_premise:
    # check if the hypothesis value contradicts the estimate of less than'stretch_time_premise'
    label = "contradiction"
elif stretch_time_hypothesis < stretch_time_premise:
    # if the hypothesis value is less than the premise, it is consistent with the premise
    # but we cannot infer entailment since the hypothesis does not provide a specific time for catching up
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise, it is consistent with the premise
    # but we cannot infer entailment since the hypothesis does not provide a specific time for catching up
    label = "neutral"

print(label)
