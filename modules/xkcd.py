
def sandwich(phenny, input):
  if input.group(1) == 'sudo ':
    phenny.say('Okay')
  else:
    phenny.say('What?  Make it yourself.')
sandwich.name = 'sandwich'
sandwich.rule = ('$nick', r'(sudo )?make me a sandwich')
sandwich.priority = 'low'
