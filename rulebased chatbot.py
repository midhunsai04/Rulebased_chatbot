import re
import random

class Rulebot:
  ### Potential Negative Responses
  negative_responses = ("no","nope","nah","naw","not a chance","sorry")
  ### Exit conversation keywords
  exit_commands = ("quit","pause","exit","goodbye","bye","later")
  ### Random starter question
  random_questions = (
      "why are you here?",
      "are there many humans like you?",
      "what do you consume for sustenance?",
      "Is there intelligent life on this planet?",
      "Does Earth have a leader?",
      "what planets have you visited",
      "What technology do you have on this planet?",
  )

  def __init__(self):
   self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                      'answer_why_intent': r'why\share*',
                      }

  def greet(self):
    self.name = input("what is your name?\n")
    will_help = input(
        f"Hi {self.name},I am Rule-bot. Will you help me learn about your planet?\n")
    if will_help in self.negative_responses:
        print("OK, have a nice earth day!")
        return
    self.chat()
  
  def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, have a nice earth day!")
                return True

  def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

  def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
               return self.answer_why_intent()
        if not found_match:
            return self.no_match_intent()

  def describe_planet_intent(self):
        responses = ("My planet is a utopia of various species.\n",
                   "I am from Opidipus.\n")
        return random.choice(responses)

  def answer_why_intent(self):
        responses = ("I come in peace.\n",
                     "I heard the coffee is good.\n")
        return random.choice(responses)

  def no_match_intent(self):
        responses = (
        "Please tell me more.\n", "Tell me more.\n", "why do you say that?\n", "I see. Can you elaborate?\n",
        "Interesting. Can you tell me more?\n", "I see. How do you think?\n", "why?\n",
        "How do you think I feel when you say that?\n")
        return random.choice(responses)

AlienBot = Rulebot()
AlienBot.greet()