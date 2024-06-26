lead_premise = 14
lead_hypothesis = None

# the hypothesis mentions that Mark Webber extends his lead at the top of the Formula One world championship race
# however, the hypothesis does not provide any specific information about the lead, which is mentioned in the premise
if lead_hypothesis is None:
    # check if the hypothesis contradicts the premise by not providing any information about the lead
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, but does not provide any specific information about the lead, we can infer neutrality
    label = "neutral"

print(label)
