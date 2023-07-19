# This code was made by Nidhal LABRI #
import random

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      for _ in range(count):
        self.contents.append(color)
    self.original_contents = self.contents[:]

  def draw(self, number):
    if number >= len(self.contents):
      return self.contents
    # Randomly select 'number' balls from the hat without replacement
    drawn_balls = random.sample(self.contents, number)
    for ball in drawn_balls:
      # Remove the drawn balls from the hat
      self.contents.remove(ball)
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  for _ in range(num_experiments):
    # Reset the hat's contents to the original state for each experiment
    hat.contents = hat.original_contents[:]
    drawn_balls = hat.draw(num_balls_drawn)
    success = True  # Variable to track if the experiment was successful
    for color, count in expected_balls.items():
      if drawn_balls.count(color) < count:
        success = False
        break
    if success:
      successes += 1
  # Calculate the probability of success
  probability = successes / num_experiments
  
  return probability