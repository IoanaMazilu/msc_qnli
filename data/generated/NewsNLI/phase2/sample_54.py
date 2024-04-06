# Premise: It all started when a group of 10 physicians from across the country emailed a letter to Columbia University expressing disapproval that Oz is on the faculty.
# Hypothesis: Ten physicians across the country have banded together to tell Columbia they think having Oz on faculty is unacceptable.
# Golden Label: neutral

physicians_premise = 10
physicians_hypothesis = 10

# the hypothesis mentions the number of physicians who wrote to Columbia, which is also mentioned in the premise
if physicians_hypothesis != physicians_premise:
    # check if the number of physicians in the hypothesis contradicts the number of physicians in the premise
    label = "contradiction"
else:
    # if the number of physicians in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

