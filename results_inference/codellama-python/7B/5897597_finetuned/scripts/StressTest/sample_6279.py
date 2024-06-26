# defining the ratios of questions submitted by Rajat, Vikas and Abhishek in the premise and hypothesis
ratio_premise = [7, 3, 2]
ratio_hypothesis = [8, 3, 2]

# comparing the ratios of questions submitted by Rajat, Vikas and Abhishek in the premise and hypothesis
if ratio_premise[0] >= ratio_hypothesis[0] and ratio_premise[1] == ratio_hypothesis[1] and ratio_premise[2] == ratio_hypothesis[2]:
    # check if the ratio of questions submitted by Rajat, Vikas and Abhishek in the premise contradicts the ratio in the hypothesis
    label = "contradiction"
elif ratio_premise[0] < ratio_hypothesis[0] and ratio_premise[1] == ratio_hypothesis[1] and ratio_premise[2] == ratio_hypothesis[2]:
    # check if the ratio of questions submitted by Rajat, Vikas and Abhishek in the premise is less than the ratio in the hypothesis
    label = "entailment"
else:
    # if the ratios of questions submitted by Rajat, Vikas and Abhishek in the premise and hypothesis do not contradict or are less than the other, we can infer neutrality
    label = "neutral"

print(label)
