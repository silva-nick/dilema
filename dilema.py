import random

class Firm:

  q_table = []
  p_table = [[]]

  learning_rate = .8 #rate at which it values new data
  discount_rate = .2 #rate at which it values future benefit

  def create(self):
    self.p_table = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
    self.q_table = [0,0,0]
    #holds the long term benefit of any given decision

  def run(self, my_action, their_action):
    self.q_table[my_action] = self.q_table[my_action] + self.learning_rate *(self.p_table[their_action][my_action] - self.discount_rate * self.max_col(self.p_table[their_action]))

    if(self.learning_rate > .005):
        self.learning_rate -= .002
        self.discount_rate += .002
    #self.q_table[x] = self.q_table[x] + self.learning_rate * (x * b1 + self.discount_rate*(self.q_table[2][self.max_col(self.q_table[2][:(self.wealth + 1)])] - self.q_table[1][x]))

  def best_action(self):
    return self.max_col(self.q_table)

  def printp(self):
    return str(self.p_table[0]) + "\n" + str(self.p_table[1]) + "\n" + str(self.p_table[2])

  def getq(self):
      return self.q_table

  def max_col(self, table):
    max = table[0]
    max_col_index = 0
    for i in range(1, len(table)):
      if table[i] > max:
        print (table[i])
        max = table[i]
        max_col_index = i

    return max_col_index

  def find_nash(self):
        nash_table = []
        for i in range(len(self.p_table[0])):
            nash_table.append(self.max_col(self.p_table[i]))
        return nash_table
