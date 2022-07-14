import random


class Hat:
    
    #Setting up constructor to handle variable number of arguements
    def __init__(self, **kwargs):
        self.colours_dict = kwargs
        self.contents = []
        self.contents_copy = []
        
        #Creating list containing the balls as strings according to their colour
        #Iterates through each colour
        for colour in self.colours_dict:
            #Adds i balls to the list for the current colour
            for i in range(self.colours_dict[colour]):
                self.contents.append(colour)
                self.contents_copy.append(colour)


    #Draw function
    def draw(self, num_balls):
        #Resetting the hat
        self.contents = self.contents_copy.copy()
        
        #Creates list to store drawn balls 
        drawn_balls = []
        
        #Returns all balls if num_balls exceeds the total number of balls
        if num_balls >= len(self.contents):
            return self.contents

        #Draws balls at random equal to num_balls
        for i in range(num_balls):
            #Selects a random ball
            selected = random.randint(0, (len(self.contents)-1))
            #Adds the random ball to the drawn list
            drawn_balls.append(self.contents[selected])
            #Removes the selected ball from the bag of balls
            del self.contents[selected]
        
        return(drawn_balls)



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #Setting up variables
    success = 0
    
    #Repeating the experiment n times
    for n in range(num_experiments):
        
        #Drawing the balls at random
        drawn_experiment = hat.draw(num_balls_drawn)
        
        #Determining if the experiment was successful
        conditions_met = True
        for colour in expected_balls:
            #Checks if conditions are met
            if expected_balls[colour] > drawn_experiment.count(colour):
                conditions_met = False
        
        #Adds 1 to the success tally if all expected numbers are met
        if conditions_met == True:
            success += 1
    
    #Estimates probability based on experimental results
    probability = success / num_experiments
    return probability
