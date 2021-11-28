# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Study Notes of Shawn Solomon                                                      #
# Book Title: Real World Python: A Hacker's Guide to Solving Problems With Code     #
# Book Author: Lee Vaughn                                                           #
# Publishing Company: No Starch Press Inc.                                          #
# Copyright Year: 2021                                                              #
# ISBN-13: 978-1-7185-0063-1                                                        #
# Chapter 1: Saving Shipwrecked Sailors With Bayes’ Rule                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Around the year 1740, Thomas Bayes set out to derive a solution to prove the existance of God. This solution became known as Bayes' Rule. #
# This solution was mostly ignored for over 200 years due to it's tedious mathematics until the invention of the modern computer.           #
# After the ubiuity of the Modern Computer with its faster processors came about, Bayes' Rule is now integral to Data Science today.        #
#                                                                                                                                           #
# P(B/A) or the probability P of hypothesis A given data B.                                                                                 #
#                                                                                                                                           #
#             P(B/A) P(A)                                                                                                                   #
# P(A/B)  =   -----------                                                                                                                   #
#                 P(B)                                                                                                                      #
#                                                                                                                                           #
#                  P(E/G) Pprior (G)                                                                                                        #
# P(G/E)  =   --------------------------                                                                                                    #
#             Sum of P(E/G9) Pprior (G9)                                                                                                    #
#                                                                                                                                           #
# Having to write out a statistical equation and plugging in previous variables is a chore. A computer can be set to do this Automatically. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # #
# Project #1: Search and Rescue     #
# # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                               #
# Objective:                                                                                                    #
# Create a search and rescue game that uses Bayes’ rule to inform player choices on how to conduct a search.    #
#                                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# When importing modules, it's important to remember preferred order is standard, third-party, and user defined modules.

import sys # Import Python in-built Systems Module for standard sets of functions and variables
import random # Import In-Built Random Number Generator Module.
import itertools # Import In-built module for functions creating efficient loop iterators
import numpy as np # Import NumPy mathematical library and call it by variable np
import cv2 as cv # Import OpenCV2 library for real-time computer vision and call it by variable cv

# When assigning constants according to the PEP8 style guide, names should be typed in all caps to let other developers know that these variables should not be changed.

MAP_FILE = 'cape_python.png' # The map file for the mythical region of Cape Python displaying the location where our sailors are lost.

# The constants for search area corners create finite ordered lists called tuples.
# The x and y coordinates are listed with the first two being the upper left and the last two the lower right of the box defining the area. 

SA1_CORNERS = (130, 265, 180, 315)   # (UL-X, UL-Y, LR-X, LR-Y)
SA2_CORNERS = (80, 255, 130, 305)    # (UL-X, UL-Y, LR-X, LR-Y)
SA3_CORNERS = (105, 205, 155, 255)   # (UL-X, UL-Y, LR-X, LR-Y)

# A class is a data type in Object Oriented Programming. OOP is an alternative approach to Functional or Procedural Programming. 
# Very useful for large and complex programs producing code that's easier to update, maintain, and reuse.
# OOP is built around data structures known as objects which consist of data, methods, and the interactions between them. 
# Works well in programs which use interacting objects such as games.
# A class is used as a template from which multiple objects can be created. 

# Creating a class for the search and rescue game.

class Search(): # Define a class named search.
    """Bayesian Search & Rescue game with 3 search areas."""
    def __init__(self, name): # The def __init__() method defines the initial state of the variables in the template. Every object created with this class will recieve it's method.
        # Self parameter references the object being created. Technically a context instance of a method.
        self.name = name # Name is an attribute in reference to the context instance of the method defining the initial variable name in the function.
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR) # The IMREAD_COLOR will add color to the grayscale image source through imread() from the OpenCV2 import module.
        if self.img is None: # If statement looks to see if the map image is not present.
            print('Could not load map file {}'.format(MAP_FILE), # Print error message regarding the map file.
                file=sys.stderr) # Standard Error Stream that only outputs errors as opposed to stdout.
            sys.exit(1) # Exit

        self.area_actual = 0 # Initialize variable area_actual within class and set variable state as 0.
        self.sailor_actual = [0, 0] # Initialize variable sailor_actual as "local" coords within a search area.

        # The instances and attributes here are creating sub-arrays within new variables using numpy and will reference y first before x on a cartesian plane in these instances.
        # The arrays will change the tuple order so that x and y are called appropriately for numpy.
        self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3], # sa1 [UL-Y] : [LR-Y]
                            SA1_CORNERS[0] : SA1_CORNERS[2]] # sa1 [UL-X] : [LR-X]
        self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3], # sa2 [UL-Y] : [LR-Y]
                            SA2_CORNERS[0] : SA2_CORNERS[2]] # sa2 [UL-X] : [LR-X]
        self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3], # sa3 [UL-Y] : [LR-Y]
                            SA3_CORNERS[0] : SA3_CORNERS[2]] # sa3 [UL-X] : [LR-X]

        # Initialize variable and states for the probabilities in search areas 1, 2, and 3 as fractions of 100%.
        self.p1 = 0.2 # Probability of finding sailor in search area 1 set to 20% or 1 out of 5 chance to find.
        self.p2 = 0.5 # Probability of finding sailor in search area 2 set to 50% or 1 out of 2 chance to find.
        self.p3 = 0.3 # Probability of finding sailor in search area 3 set to 30% or 3 out of 10 chance to find.

        # Initialize the search effectiveness probabilities in search areas 1, 2, and 3.
        self.sep1 = 0 # Probability of search effectiveness for search area 1 set to initial state 0.
        self.sep2 = 0 # Probability of search effectiveness for search area 2 set to initial state 0.
        self.sep3 = 0 # Probability of search effectiveness for search area 3 set to initial state 0.

    # Defining a new function to draw map legend, labels, and search area bounding boxes. 
    def draw_map(self, last_known): # Define draw_map() states within the class.
        """Display basemap with scale, last known xy location, search areas."""
        cv.line(self.img, (20, 370), (70, 370), (0, 0, 0), 2) # Draw line segment on image using coordinates for map legend.
        cv.putText(self.img, '0', (8, 370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0)) # Draw text string using font at coordinates for map legend.
        cv.putText(self.img, '50 Nautical Miles', (71, 370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0)) # Draw text string using font at coordinates for map legend.
        cv.rectangle(self.img, (SA1_CORNERS[0], SA1_CORNERS[1]), (SA1_CORNERS[2], SA1_CORNERS[3]), (0, 0, 0), 1) # Draw rectangle 1 using coordinates.
        cv.putText(self.img, '1', (SA1_CORNERS[0] + 3, SA1_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0) # Draw label text string using font at coordinates relating to rectangle 1.
        cv.rectangle(self.img, (SA2_CORNERS[0], SA2_CORNERS[1]), (SA2_CORNERS[2], SA2_CORNERS[3]), (0, 0, 0), 1) # Draw rectangle 2 using coordinates.
        cv.putText(self.img, '2', (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0) # Draw label text string using font at coordinates relating to rectangle 2.
        cv.rectangle(self.img, (SA3_CORNERS[0], SA3_CORNERS[1]), (SA3_CORNERS[2], SA3_CORNERS[3]), (0, 0, 0), 1) # Draw rectangle 3 using coordinates.
        cv.putText(self.img, '3', (SA3_CORNERS[0] + 3, SA3_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0) # Draw label text string using font at coordinates relating to rectangle 3.
        cv.putText(self.img, '+', (last_known), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255)) # Draw indicator text string using font at coordinates for last known position variable.
        cv.putText(self.img, '+ = Last Known Position', (274, 355), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255)) # Draw label text string using font at coordinates for the map legend.
        cv.putText(self.img, '* = Actual Position', (275, 370), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0)) # Draw label text string using font at coordinates for the map legend.
        cv.imshow('Search Area', self.img) # Draw label text string using font at coordinates in self reference to the image.
        cv.moveWindow('Search Area', 750, 10) # Draw label text string using font at coordinates for the map legend.
        cv.waitKey(500) # Wait 500

    # Defining a new function for missing sailor's final location.
    def sailor_final_location(self, num_search_areas): # Define sailor_final_location() states within the class.
        """Return the actual x,y location of the missing sailor."""
        # Find sailor coordinates with respect to any Search Area subarray.
        # self.sailor_actual[0] = np.random.choice(self.sa1.shape[1], 1) # Original line commented out due to publishing error.
        # self.sailor_actual[1] = np.random.choice(self.sa1.shape[0], 1) # Original line commented out due to publishing error.
        # Update to the book exercise correcting error. Correction found at: https://nostarch.com/real-world-python under sub-heading Updates.
        self.sailor_actual[0] = np.random.choice(self.sa1.shape[1]) # Set choice 0 using NumPy and Random modules. Shape is set to 1.
        self.sailor_actual[1] = np.random.choice(self.sa1.shape[0]) # Set choice 1 using NumPy and Random modules. Shape is set to 0.

        area = int(random.triangular(1, num_search_areas + 1)) # Set area as an integer of a triangular distribution from samples over the interval of lower and upper limits.
        
        # If and elseif statements to return x and y coordinates of sailor when called.
        if area == 1: # Check if area is equal to 1 is true.
            x = self.sailor_actual[0] + SA1_CORNERS[0]
            y = self.sailor_actual[1] + SA1_CORNERS[1]
            self.area_actual = 1 # Set object's area_actual variable to 1 if area equals 1 is true. 
        elif area == 2: # Otherwise check if area is equal to 2 is true if not equal to 1.
            x = self.sailor_actual[0] + SA2_CORNERS[0]
            y = self.sailor_actual[1] + SA2_CORNERS[1]
            self.area_actual = 2 # Set object's area_actual variable to 2 if area equals 2 is true.
        elif area == 3: # Otherwise check if area is equal to 3 if not equal to either 1 or 2.
            x = self.sailor_actual[0] + SA3_CORNERS[0]
            y = self.sailor_actual[1] + SA3_CORNERS[1]
            self.area_actual = 3 # Set object's area_actual variable to 3 if area equals 3 is true.
        return x, y # Return function values to the caller.
    
    # Defining a new function to calculate and update search effectivness for each area.
    def calc_search_effectiveness(self):
        """Set decimal search effectiveness value per search area."""
        self.sep1 = random.uniform(0.2, 0.9) # Get a random number in range of tuple a and tuple b dependant on rounding for variable sep1.
        self.sep2 = random.uniform(0.2, 0.9) # Get a random number in range of tuple a and tuple b dependant on rounding for variable sep2.
        self.sep3 = random.uniform(0.2, 0.9) # Get a random number in range of tuple a and tuple b dependant on rounding for variable sep3.

    # Defining a new function to return search results and list of searched coordinates.
    def conduct_search(self, area_num, area_array, effectiveness_prob): # Define conduct_search states area_num, area_array, and effective_prob within the class.
        """Return search results and list of searched coordinates."""
        local_y_range = range(area_array.shape[0]) # Variable for local range of y created and set to the shape 0 of the area array.
        local_x_range = range(area_array.shape[1]) # Variable for local range of x created and set to the shape 1 of the area array.
        coords = list(itertools.product(local_x_range, local_y_range)) # Variable coords is equal to the list of products of the tuple variables local_x_range and local_y_range using itertools.
        random.shuffle(coords)
        coords = coords[:int((len(coords) * effectiveness_prob))] # Variable coords is now equal to the list of itself with integers of itself times length of items times effectiveness_prob.
        loc_actual = (self.sailor_actual[0], self.sailor_actual[1]) # Variable loc_actual is the equal to a tuple of sailor_actual[0] and sailor_actual[1] states.
        
        #If else statement to return strings and coordinates relating to finding or not finding the missing sailor.
        if area_num == self.area_actual and loc_actual in coords: # Check if variable area_num is equal to the values of area_actual and loc_actual within variable coords is true.
            return 'Found in Area {}.'.format(area_num), coords # Return the formatted string value for found sailor and coordinates to caller.
        else: # Otherwise if false.
            return 'Not Found', coords # Return the string and the coordinates for not finding the sailor. 

    # Defining a new function to calculate and revise the probabilities the missing sailor is in a search area.
    def revise_target_probs(self): # Define revise_target_probs() and refer to itself. Here's our Bayesean Maths.
        """Update area target probabilities based on search effectiveness."""
        denom = self.p1 * (1 - self.sep1) + self.p2 * (1 - self.sep2) \
                + self.p3 * (1 - self.sep3) # Create variable denom and have it equal to the sum of the sep1 value minus 1 times p1 plus the sum of sep2 minus 1 times p2 plus the sum of sep3 minus 1 times p3.
        self.p1 = self.p1 * (1 - self.sep1) / denom # The variable within class, p1 is equal to sep1 minus 1 multiplied by itself divided by the value of denom.
        self.p2 = self.p2 * (1 - self.sep2) / denom # The variable within class, p2 is equal to sep2 minus 1 multiplied by itself divided by the value of denom.
        self.p3 = self.p3 * (1 - self.sep3) / denom # The variable within class, p3 is equal to sep3 minus 1 multiplied by itself divided by the value of denom.

# End of Search class

# New menu function being defined for draw_menu(search_num) to choose search areas
def draw_menu(search_num): # Define draw_menu with reference to the value of search_num.
    """Print menu of choices for conducting area searches."""
    print('\nSearch {}'.format(search_num)) # Print a space and string with dictionary and format with the value of search_num.
    print( # Print Menu choices
        """
        Choose next areas to search:
        0 - Quit
        1 - Search Area 1 twice
        2 - Search Area 2 twice
        3 - Search Area 3 twice
        4 - Search Areas 1 & 2
        5 - Search Areas 1 & 3
        6 - Search Areas 2 & 3
        7 - Start Over
        """
        ) # Finish printing menu choices

# Main function being defined.

def main():
    app = Search('Cape_Python')
    app.draw_map(last_known=(160, 290))
    sailor_x, sailor_y = app.sailor_final_location(num_search_areas=3)
    print("-" * 65)
    print("\nInitial Target (P) Probabilities:")
    print("P1 = {:.3f}, P2 = {:.3f}, P3 = {:.3f}".format(app.p1, app.p2, app.p3))
    search_num = 1

    while True:
        app.calc_search_effectiveness()
        draw_menu(search_num)
        choice = input("Choice: ")
        if choice == "0":
            sys.exit()
        
        elif choice == "1":
            results_1, coords_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coords_2 = app.conduct_search(1, app.sa1, app.sep1)
            app.sep1 = (len(set(coords_1 + coords_2))) / (len(app.sa1)**2)
            app.sep2 = 0
            app.sep3 = 0

        elif choice == "2":
            results_1, coords_1 = app.conduct_search(2, app.sa2, app.sep2)
            results_2, coords_2 = app.conduct_search(2, app.sa2, app.sep2)
            app.sep1 = 0
            app.sep2 = (len(set(coords_1 + coords_2))) / (len(app.sa2)**2)
            app.sep3 = 0

        elif choice == "3":
            results_1, coords_1 = app.conduct_search(3, app.sa3, app.sep3)
            results_2, coords_2 = app.conduct_search(3, app.sa3, app.sep3)
            app.sep1 = 0
            app.sep2 = 0
            app.sep3 = (len(set(coords_1 + coords_2))) / (len(app.sa3)**2)

        elif choice == "4":
            results_1, coords_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coords_2 = app.conduct_search(2, app.sa2, app.sep2)
            app.sep3 = 0

        elif choice == "5":
            results_1, coords_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coords_2 = app.conduct_search(3, app.sa3, app.sep3)
            app.sep2 = 0

        elif choice == "6":
            results_1, coords_1 = app.conduct_search(2, app.sa2, app.sep2)
            results_2, coords_2 = app.conduct_search(3, app.sa3, app.sep3)
            app.sep1 = 0

        elif choice == "7":
            main()

        else:
            print("\nSorry, but that isn't a valid choice.", file=sys.stderr)
            continue

        app.revise_target_probs() # Use Bayes' rule to update target probs.

        print("\nSearch {} Results 1 = {}"
              .format(search_num, results_1), file=sys.stderr)
        print("Search {} Results 2 = {}\n"
              .format(search_num, results_2), file=sys.stderr)
        print("Search {} Effectiveness (E):".format(search_num))
        print("E1 = {:.3f}, E2 = {:.3f}, E3 = {:.3f}"
              .format(app.sep1, app.sep2, app.sep3))

        if results_1 == 'Not Found' and results_2 == 'Not Found':
            print("\nNew Target Probabilities (P) for Search {}:"
            .format(search_num + 1))
            print("P1 = {:.3f}, P2 = {:.3f}, P3 = {:.3f}"
            .format(app.p1, app.p2, app.p3))
        else:
            cv.circle(app.img, (sailor_x, sailor_y), 3, (255, 0, 0), -1)
            cv.imshow('Search Area', app.img)
            cv.waitKey(1500)
            main()
        search_num += 1

# If statement to check if program is the main script and to call main() function to start the game.

if __name__ == '__main__':
    main()

# End of Script

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                                           #
# Further Reading:                                                                                                          #
# The Theory That Would Not Die: How Bayes’ Rule Cracked the Enigma Code, Hunted Down Russian Submarines,                   #
# and Emerged Triumphant from Two Centuries of Controversy (Yale University Press, 2011), by Sharon Bertsch McGrayne        #
#                                                                                                                           #
# A major source of documentation for NumPy is https://docs.scipy.org/doc/                                                  #
#                                                                                                                           #
# Challenge Project #1: Smarter Searches                                                                                    #
# Copy and edit the program so that it keeps track of which coordinates have been searched within an area and excludes      #
# them from future searches (until main() is called again, either because the player finds the sailor or chooses menu       #
# option 7 to restart). Test the two versions of the game to see whether your changes noticeably impact the results.        #
#                                                                                                                           #
# Challenge Project #2: Finding the Best Strategy with MCS                                                                  #
#                                                                                                                           #
#                                                                                                                           #
# Challenge Project #3: Calculating the Probability of Detection                                                            #
#                                                                                                                           #
#                                                                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #