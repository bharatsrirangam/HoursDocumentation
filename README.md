# HoursDocumentation
A little program I wrote to record the number of hours worked per day. 
There is a count in the hours.txt file that represents the total number of hours for the current pay period. This can be reset back to 0 for each pay period using the clearhours command (see below). This is super simple and just a fun little project I put together in 15 minutes. Let me know if there's any other useful additions I could add to make the recording of work hours even easier. 

## Getting Started



### Prerequisites

Make sure to be using Python 3.0 or greater. 
You'll also need to update your .bash_profile file or equivalent to add the appropriate aliases for quick and easy updates to the hours you want to log for that specific day. 

These include following three lines to add to the bash_profile file: 

```
alias hours='python [~path to hours.py~]/hours.py'
alias viewhours='vim [~path to hours.txt~]/hours.txt'
alias clearhours='python [~path to hours.py~]/hours.py clear'
```

Here is how to actually use these aliases: 
*In Terminal*

```
$ hours 2.0 // Logs 2 hours for today (with the date) in your hours.txt file (created if orignally non-existent)
$ viewhours // Loads your hours.txt file in a vim view to see how many hours you currently have
$ clearhours // Clears the total count for the week from your hours.txt file and creates a new section in the hours.txt file for new hours (useful for biweekly pay periods)
```

### Installing

Just download the repo and assign the proper aliases with the proper paths to the files. 


## Authors

* **Bharat Srirangam** - *Initial work*
