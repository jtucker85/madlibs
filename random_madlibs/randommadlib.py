from sample_madlibs import farming, photo, trackday
import random

if __name__ == "__main__" :
    m = random.choice([farming, photo, trackday])
    m.madlib()