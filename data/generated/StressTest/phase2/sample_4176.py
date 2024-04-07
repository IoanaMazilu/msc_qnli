# Premise: If Burj Khalifa stands at 830 meters high and Sears stands at 527 meters high, how much higher is Burj Khalifa than Sears?
# Hypothesis: If Burj Khalifa stands at more than 730 meters high and Sears stands at 527 meters high, how much higher is Burj Khalifa than Sears?
# Golden Label: entailment

burj_khalifa_height_premise = 830
burj_khalifa_height_hypothesis = 730
sears_height_premise = 527
sears_height_hypothesis = 527

# the hypothesis talks about the heights of Burj Khalifa and Sears, also referenced in the premise
if burj_khalifa_height_hypothesis > burj_khalifa_height_premise:
    # check if the 'burj_khalifa_height_hypothesis' contradicts the 'burj_khalifa_height_premise'
    label = "contradiction"
elif sears_height_hypothesis != sears_height_premise:
    # check if the 'sears_height_hypothesis' contradicts the 'sears_height_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

