sreedhar_sravan_premise = 25
sreedhar_sravan_hypothesis = float(input("Enter the number of days Sreedhar and Sravan can do the work together: "))

# the hypothesis talks about the number of days Sreedhar and Sravan can do the work together
if sreedhar_sravan_hypothesis > sreedhar_sravan_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif sreedhar_sravan_hypothesis <= sreedhar_sravan_premise:
    # the hypothesis does not contradict the premise, but cannot be fully entailed from the premise
    label = "neutral"
else:
    # the hypothesis contradicts the premise
    label = "contradiction"

print(label)
