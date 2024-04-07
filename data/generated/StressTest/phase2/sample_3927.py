# Premise: For dinner, Sue ate 360 grams of fruit which was five times as much fruit as she ate for lunch, and three times as much fruit as she ate for breakfast.
# Hypothesis: For dinner, Sue ate less than 460 grams of fruit which was five times as much fruit as she ate for lunch, and three times as much fruit as she ate for breakfast.
# Golden Label: entailment

fruit_dinner_premise = 360
fruit_dinner_hypothesis = 460

# the hypothesis talks about the amount of fruit Sue ate for dinner, which is also mentioned in the premise
if fruit_dinner_hypothesis <= fruit_dinner_premise:
    # check if the hypothesis value contradicts the amount of fruit Sue ate for dinner in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

