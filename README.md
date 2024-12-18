# Project-SG_Uni_cutoffs
Plotting the igps of the various courses in the big 3 unis in Singapore using matplotlib, and hopefully catching some interesting patterns and trends that we can look more into and attempt to justify.

The 'Images' folder is where all the images used in the README.md will be stored. 'myenv' is the virtual environment configurations, and uniscrape.py is the main project file code.

## V1: After creating a virtual environment and activating it and creating a requirements.txt file which contains the necessary packages needed, i pip installed all the packages, then imported the packages into the newly created python file, uniscrape.py. I also defined the url variable for the website ill be scraping in the python file.

## V2: Here i use requests to get the html of the website and pass it through beautifulsoup which formats the raw html text by adding indents and making it easier to examine. We can see that the info we want to get is mostly in the 'tbody' tag (Fig 1), so we define those tags as the variable 'content'. When i print(len(content)), i get 4, 1 for each section as u can see in Fig 2. But i dont care about the first Landing Page section, just the last 3 which contain information about NUS, NTU and SMU. So i get rid of the first 'tbody' tag. But inside the next 3 target tags are still a whole lot of html, so to not overload my screen with text i just print all the content in the first section, which contains info on NUS only.

Fig 1:

![alt text](image.png)

Fig 2:

![alt text](image-1.png)

## V3: Here i print out just the years and store them all in a list i defined called 'years' (Fig 3). I also removed each element as i appended them to the list, idk why it just works better for me to work with the rest of the data.

Fig 3:

![alt text](image-1.png)

Then i created the dataframe table, starting with 'years' as the first row (Fig 4):

Fig 4:

![alt text](image-2.png)

## V4: To format the data better, i removed the faculty and school names from the data such as 'Faculty of Law', 'School of Engineering' or 'College of Design and Engineering', and stored them in a separate dictionary. The faculty name is the key and the value is a list of the course names inside.
I did this so as to improve predictability for what kind of value will be at which index. To explain this better, look at Fig 5, Fig 5.1, and Fig 5.2:

Fig 5:

insert_fig_5_link_here

Fig 5.1:

5.1_link_here

Fig 5.2

5.2_link_here

What is interesting that we can see from these figures, are that all the rows that represent the faculty or school name (Medicine, Dentistry, etc), have 52 rows between each of them. 53 + 52 = 105, and 105 + 52 = 157. This makes the data more predictable and easier to organise the rp, gpa, and course places into their respective courses.
Now that i know to separate the data after every multiple of 52 + 1, i can do this (Fig 6, Fig 6.1, and Fig 6.2):

Fig 6:

link_here

Fig 6.1:

link_here

Fig 6.2:

link_here

By editing my code to only print the index up to 52 and then resetting back to 1, we can see that each course has 52 relevant rows, including the row representing the course name.

## V5: