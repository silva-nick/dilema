<h1>Nash Equilibrium Simulation</h1>
<p>This program randomly generates a 3x3 decision matrix for 2 firms. It then uses a Q-learning algorithm to find the ideal decision for each firm. This algorithm finds the payoff for the firms decision after each 'round' and then redefines it will make its next decision. The program will iterate for a set number of rounds and finally displays the most favorable decisions for the two firms. </p>

<p>Output Notation: </p>

```bash
Decision #
[r1]
[r2]
[r3]
[payoff 0, p1, p2]
[row of nash optimal solutions]
```

<p>The program then calculates the true nash and cooperative equalibria for the firms and runs a set number of trials to see how often the program reaches either a nash or cooperative equalibrium.</p>
<p>It finds the correct Nash equilibrium some of the time :p</p>
<p>I was inspired to do this project after participating in the UI Highschool Hackathon in which my friends and I tried to simulate an economy in a similar way. I wanted to see how well non-conventional algorithms could predict a simple solution.</p>
