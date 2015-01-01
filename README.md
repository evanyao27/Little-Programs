Little-Programs
==========

Little programs for various everyday tasks 

<h2> blockinggroup.py </h2>

![Alt text](/blockinggroup.jpg?raw=true "Blocking Group")

<b> Purpose: </b> Help our blocking (rooming) group decide what combination of doubles and triples would be best. Each person assigns to each other person a "utility" rating describing how favorable rooming with the other person would be.  

<b> Design: </b> Uses the independent set algorithm as follows: Create a graph with each node represents a double or triple. For example, if persons A through F are trying to find the optimal rooming group, then one particular node would be A-B in a double, and another node would be A-C-F in a triple. Two nodes are connected if and only if they share a person (i.e. could not possibly happen at the same time). Each node is then assigned a utility rating by taking the average of the utilities of each person for the others within the node. Then, we perform a weighted independent sets algorithm to determine the optimal rooming arrangment. 

<h2> characteranalysis.py </h2> 

![Alt text](/charateranalysis.jpg?raw=true "Character Analysis")

<b> Purpose: </b> Given the text file of a facebook groupchat, this program will analyze and make a graph of the number of characters each person has spoken. It will produce a historgram allowing you to easily see who is the most chatty. 

<b> Design: </b> Very simple - search for each group chat participant's full names and a new line character, such as "Evan Yao\n", which is displayed before each one of that person's messages. 

<h2> grade_sender.ipynb </h2> 

![Alt text](/grade_sender.jpg?raw=true "Grade Sender")

<b> Purpose: </b> Send out grades to students from a CSV file. Displays all their homework scores, the ones that
are dropped, and the their final scores. 

<b> Design: </b> Uses Python to calculate which homeworks to drop, removing the appropriate number of points from the denominator.  

<h2> twentyfoursolver.py </h2> 

![Alt text](/twentyfoursolver.png?raw=true "Twenty-Four Solver")

<b> Purpose: </b> Given 4 numbers between 1 and 13, it checks whether there is a solution to the classic game 24, where you can use +,-,*,/ to form the number 24 with ALL of the 4 numbers. 

<b> Design: </b> A recursive solution: currently has bugs 

<h2>math122.py</h2>

![Alt text](/math122.png?raw=true "Math 122")

<b>Purpose: </b> Solves the following problem: Let G = GL_2(Z/3Z) representing the group of invertible 2 by 2 matrices over the field Z/3Z. How many elements of order 3 are in G? 

<b> Design: </b> Uses numpy's matrix function to iteratively find the order of each 2x2 matrix with non-zero determinant. 

<h2>messages.js</h2>

![Alt text](/messages.png?raw=true "Facebook Messages")

<b> Purpose: </b> After downloading one's facebook data, this program gives you a list of all your facebook message conversation recipients (including groupchats) and provides hyperlinks to each chat. 

<b> Instructions: </b> Click <a href = 'https://www.facebook.com/help/212802592074644' > here </a> to find out how to download your facebook data. Navigate to the HTML folder, and place this Javascript program (messages.js) into that folder. It should also contain an HTML document called "messages.htm". Open it up with a source code editor, and link messages.js with a script, src ="messages.js" tag. Then, open up messages.htm and in a few seconds, you should see that your sidebar now contains all your groupchats! You can click on them to skip directly to them. 

<b> Design: </b> All conversations begin with div with a class of "thread". Therefore, I searched for all these divs, created an ID for them, and then changed the innerHTML of the navigation bar to be links to these ID's. 


