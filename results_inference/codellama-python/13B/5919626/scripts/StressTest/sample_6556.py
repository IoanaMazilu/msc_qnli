eiffel_tower_visitors = 100
arc_de_triomphe_visitors = 50

# the hypothesis talks about the number of visitors to the Eiffel Tower and Arc de Triomphe
if eiffel_tower_visitors <= arc_de_triomphe_visitors:
    # check if the hypothesis value contradicts the estimate of more than 'arc_de_triomphe_visitors'
    label = "contradiction"
elif eiffel_tower_visitors == arc_de_triomphe_visitors:
    # check if the hypothesis value contradicts the estimate of more than 'arc_de_triomphe_visitors'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of visitors to the Eiffel Tower
    # any number of visitors greater than 'arc_de_triomphe_visitors' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
