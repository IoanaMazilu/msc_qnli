years_premise = 2
years_hypothesis = 8
interest_rate = 4

# the hypothesis talks about the number of years and interest rate which are also referenced in the premise
if years_premise!= years_hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are not comparable as they refer to different situations
    label = "neutral"

print(label)
