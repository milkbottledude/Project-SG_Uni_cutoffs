# Project-SG_Uni_cutoffs
Plotting the igps of the various courses in the big 3 unis in Singapore using matplotlib, and hopefully catching some interesting patterns and trends that we can look more into and attempt to justify.

The 'Images' folder is where all the images used in the README.md will be stored. 'myenv' is the virtual environment configurations, and uniscrape.py is the main project file code.

## V1: 
After creating a virtual environment and activating it and creating a requirements.txt file which contains the necessary packages needed, i pip installed all the packages, then imported the packages into the newly created python file, uniscrape.py. I also defined the url variable for the website ill be scraping in the python file.

## V2:
Here i use requests to get the html of the website and pass it through beautifulsoup which formats the raw html text by adding indents and making it easier to examine. We can see that the info we want to get is mostly in the 'tbody' tag (Fig 2.1), so we define those tags as the variable 'content'. When i print(len(content)), i get 4, 1 for each section as u can see in Fig 2.2. But i dont care about the first Landing Page section, just the last 3 which contain information about NUS, NTU and SMU. So i get rid of the first 'tbody' tag. But inside the next 3 target tags are still a whole lot of html, so to not overload my screen with text i just print all the content in the first section, which contains info on NUS only.

Fig 2.1:

![alt text](image.png)

Fig 2.2:

![alt text](image-1.png)

## V3:
Here i print out just the years and store them all in a list i defined called 'years' (Fig 3.1). I also removed each element as i appended them to the list, idk why it just works better for me to work with the rest of the data.

Fig 3.1:

![alt text](image-1.png)

Then i created the dataframe table, starting with 'years' as the first row (Fig 3.2):

Fig 3.2:

![alt text](image-2.png)

## V4: 
To format the data better, i removed the faculty and school names from the data such as 'Faculty of Law', 'School of Engineering' or 'College of Design and Engineering', and stored them in a separate dictionary. The faculty name is the key and the value is a list of the course names inside.
I did this so as to improve predictability for what kind of value will be at which index. To explain this better, look at Fig 4.1, Fig 4.2, and Fig 4.3:

Fig 4.1:

link_here

Fig 4.2:

link_here

Fig 4.3:

link_here

What is interesting that we can see from these figures, are that all the rows that represent the faculty or school name (Medicine, Dentistry, etc), have 52 rows between each of them. 53 + 52 = 105, and 105 + 52 = 157. This makes the data more predictable and easier to organise the rp, gpa, and course places into their respective courses.
Now that i know to separate the data after every multiple of 52 + 1, i can do this (Fig 4.4, Fig 4.5, and Fig 4.6):

Fig 4.4:

link_here

Fig 4.5:

link_here

Fig 4.6:

link_here

By editing my code to only print the index up to 52 and then resetting back to 1, we can see that each course has 52 relevant rows, including the row representing the course name.

## V5: 
After scrutinising the way the data was formatted in V4, ive concluded that its kind of crap. So in this version i decided to use the attributes in the elements to be able to distinguish between which element was a faculty, course name, or score and number of course places. I also fixed the figure numbering system, such that the first digit is the chapter in which the figure is in, while the second digit represents the figure number. For example, 'Fig 2.3' represents the 3rd figure in the 2nd chapter. Anyways, back to the code.

One trend i noticed was that most HTML elements representing faculties and schools eg: 'School of Medicine' had a 'colspan' attribute (Fig 5.1), while those that represented course names eg: 'Nursing' had a 'rowspan' attribute (Fig 5.2). As for elements that represented the other important info we want such as gpa and rp score, they did not have either of these attributes (Fig 5.3).

Fig 5.1:

link_here

Fig 5.2:

link_here

Fig 5.3:

link_here

So i decided to edit my code to catch these unique attributes and categorize them as they are, with those with the attribute 'colspan' and 'rowspan' as 'faculty' and 'course name' respectively. However, life is not always sunshine and rainbows.

Using this method, i ran into a couple hiccups. Some elements which did represented neither a faculty nor a course had these attributes (Fig 5.4), which resulted in my code throwing errows in my face multiple times. You can clearly see 'Merged into Engineering' is just a placeholder for empty spaces that dont have a value, but it has the same attributes as both elements that represent faculties as well as course names, rowspan and colspan. Hence i added the variable 'taboo' in my code, which i used to catch unanomalies that arent supposed to have those attributes. Its a manual and unsightly method, but its the best i can come up with at the moment. However its certainly much better than the nonsense i tried to pull in Version 4. We now have all the faculties, the courses under the faculties, and information about said courses all nicely organised (kinda) in the faculty_dict dictionary. In the next versions we will try to make it not just kinda organised but fully organised, theres still plenty of work to do.
 
Fig 5.4:

link_here

I apologise if Fig 5.4 seems overwhelming and has a lot of gobbledegook, you only need to pay attention to the areas circled and underlined. To put better into perspective how the faculty_dict would look like, i printed out the faculties and courses in a reader-friendly way below (Fig 5.5).

Fig 5.5:

link here

The course names have a '-' in front to show that they are under the faculty and school names. I used a simple nested for-loop which i added to the end of my python code, you can see it at the top of Fig 5.5 its very straightforward.

## V6: