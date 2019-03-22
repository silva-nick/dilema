import random

class Firm:

  q_table = []
  #holds benefit of making a decision
  p_table = [[]]
  #holds the direct payoff for any action (column) given the other firms action (row)

  learning_rate = .8 #rate at which it values new data
  discount_rate = .4 #rate at which it values future benefit

  def create(self):
    self.p_table = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
    #randomly creates a payoff matrix
    self.q_table = [0,0,0]
    #holds the long term benefit of any given decision

  def run(self, my_action, their_action):
    #runs one trial given two chosen actions

    self.q_table[my_action] = ((1 - self.learning_rate) * self.q_table[my_action]
        + self.learning_rate * (self.p_table[their_action][my_action] + self.discount_rate * self.max_col(self.p_table[their_action])))
    #Changes the current q table value given the payoff of the current situation

    if(self.learning_rate > .005):
        #decreases learning rate and increases discount rate
        self.learning_rate -= .002
        self.discount_rate += .002

  def best_action(self):
    #returns the action with the highest value in the q table
    return self.max_col(self.q_table)

  def printp(self):
    #prints the 3x3 array
    return str(self.p_table[0]) + "\n" + str(self.p_table[1]) + "\n" + str(self.p_table[2])

  def getq(self):
    return self.q_table

  def getp(self):
    return self.p_table

  def max_col(self, table):
    #given a row this returns the index of the largest value in that row
    max = table[0]
    max_col_index = 0
    for i in range(1, len(table)):
      if table[i] > max:
        max = table[i]
        max_col_index = i

    return max_col_index

  def find_nash(self):
    #returns the largest number in each row i.e. the best decision given the other firm's action
    nash_table = []
    for i in range(len(self.p_table[0])):
      nash_table.append(self.max_col(self.p_table[i]))
    return nash_table
