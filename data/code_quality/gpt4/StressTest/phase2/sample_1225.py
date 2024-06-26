photos_octavia_premise = 84
photos_octavia_hypothesis = 24
photos_other_premise = 12
photos_other_hypothesis = 12

# The hypothesis talks about the number of photographs taken by Octavia and other photographers that Jack had framed, which is also referenced in the premise
if photos_octavia_hypothesis >= photos_octavia_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'photos_octavia_premise'
    label = "contradiction"
elif photos_other_hypothesis != photos_other_premise:
    # Check if the number of photographs taken by other photographers in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of photographs by Octavia
    # Any number of photographs less than 'photos_octavia_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
