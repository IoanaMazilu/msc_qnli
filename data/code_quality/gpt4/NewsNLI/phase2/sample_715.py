anonymous_call_premise = 18002228477
anonymous_call_hypothesis = 18002228477
information_call_hypothesis = 5624356711

# the hypothesis mentions the number for anonymous calls, which is also referenced in the premise
# but it also mentions an additional number for general information, which cannot be entailed from the premise
if anonymous_call_hypothesis != anonymous_call_premise:
    # check if the number for anonymous calls in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the anonymous calls number in the hypothesis does not contradict the premise, we infer neutrality due to the extra information
    label = "neutral"

print(label)
