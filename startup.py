import os
import subprocess

# Double check prev db is removed
if os.path.exists("billkills.db"):
  os.remove("billkills.db")

#Setup DB
subprocess.run(['python', 'models.py'])
subprocess.run(['python', 'population.py'])

# Start Game
subprocess.run(['python', 'game.py'])