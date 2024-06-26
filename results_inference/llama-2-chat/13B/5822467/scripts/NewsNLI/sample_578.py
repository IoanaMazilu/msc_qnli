peacekeepers_premise = 11800
african_led_peacekeepers_premise = 6500
french_troops_premise = 2000

peacekeepers_hypothesis = 11800

# the hypothesis mentions the number of peacekeepers approved for deployment, which is also mentioned in the premise
# however, the premise mentions the number of African-led peacekeeping forces and French troops already operating in the country
# the hypothesis does not provide any information about these existing forces, so we cannot entail or contradict the premise
label = "neutral"

print(label)
