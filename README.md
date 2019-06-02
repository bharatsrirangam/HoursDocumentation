# HoursDocumentation
A little program I wrote to record the number of hours worked per day. 
There is a count in the hours.txt file that represents the total number of hours for the current pay period. This can be reset back to 0 for each pay period using the clearhours command (see below). This is super simple and just a fun little project I put together in 15 minutes. Let me know if there's any other useful additions I could add to make the recording of work hours even easier. 

## Getting Started
It is important to note that there are some extra files in this respository on keeping track of money which uses the same code as my Hours Documentation code - just adapted to record purchases over the week, etc. 


### Prerequisites

Make sure to be using Python 3.0 or greater. 
You'll also need to update your .bash_profile file or equivalent to add the appropriate aliases for quick and easy updates to the hours you want to log for that specific day. 

Include the following lines to your .bash_profile file: 

```
alias viewhours='python /Users/Bharat_Srirangam/Desktop/HoursDocumentation/hours.py -view'
alias hoursa='python /Users/Bharat_Srirangam/Desktop/HoursDocumentation/hours.py -a'
alias hours='python /Users/Bharat_Srirangam/Desktop/HoursDocumentation/hours.py'
alias vimhours='vim /Users/Bharat_Srirangam/Desktop/HoursDocumentation/hours.txt'
alias clearhours='python /Users/Bharat_Srirangam/Desktop/HoursDocumentation/hours.py -clear'
```

Here is how to actually use these aliases: 
*In Terminal*

```
$ hours 2.0 // Logs 2 hours for today (with the date) in your hours.txt file (created if orignally non-existent)
$ hoursa -2.0 // Adds 2 hours to the last entry of the current day if it exists, other wise just adds an entry of 2 hours for that day. 
$ viewhours //Displays the entries for the current group of hours.
$ vimhours // Loads your hours.txt file in a vim view to see and possibly edit how many hours you currently have
$ clearhours // Clears the total count for the week from your hours.txt file and creates a new section in the hours.txt file for new hours (useful for biweekly pay periods)
```

### Installing

Just download the repo and assign the proper aliases with the proper paths to the files. 


## Authors

* **Bharat Srirangam** - *Initial work*
