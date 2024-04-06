# Premise: The $300 Slingbox 500 also streams1080p HD content and has a variety of connection options, including HDMI, component and composite for linking to your other devices and television set.
# Hypothesis: Both add HD streaming and the Slingbox 500 adds HDMI and WiFi.
# Golden Label: neutral

price_premise = 300
hd_streaming_premise = True
hdmi_premise = True
wifi_premise = False

hd_streaming_hypothesis = True
hdmi_hypothesis = True
wifi_hypothesis = True

# the hypothesis mentions the HD streaming and the HDMI, which are also mentioned in the premise
# it also mentions WiFi, which is not mentioned in the premise
if hd_streaming_hypothesis != hd_streaming_premise:
    # check if the HD streaming in the hypothesis contradicts the HD streaming reported in the premise
    label = "contradiction"
elif hdmi_hypothesis != hdmi_premise:
    # check if the HDMI from the hypothesis contradicts the HDMI in the premise
    label = "contradiction"
elif wifi_hypothesis != wifi_premise:
    # check if the WiFi from the hypothesis contradicts the WiFi in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

