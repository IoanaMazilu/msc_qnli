greatest_athletics_career_premise = "more than a decade ago"
greatest_athletics_career_hypothesis = "eighteen gold medals and set 21 world records"

# the hypothesis talks about the number of gold medals and world records won by Carl Lewis, which is also mentioned in the premise
if greatest_athletics_career_hypothesis == greatest_athletics_career_premise:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
