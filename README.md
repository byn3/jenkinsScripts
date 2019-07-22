# jenkinsScripts
DevOps

# Wut do?
Get the max and averages of your Jenkins builds. I'm a pleb without access to download and manage plugins and I needed this info. 

## Prerequisites
* Python
* A text file containing all the URLs of the builds or projects that you want to see

Do the whole cloning and cd into the directory, then run this by typing python3 ./scripts.py.  


### Code explaination 
___
The function scanBirstJenkins will open the file holding all the application URLs and pass them into the only other function, parseURL. 
It tracks and manages total max and average of all the data in here.

The function parseURL fetches the data from the Jenkins API and formats it where we can manipulate and play with it.
I convert the miliseconds to minutes and return mack that one workspace's max and avg, along with printing an array of all build times.  

### Customizations
* If you want more data from the Jenkins API, add those key values into the suffix variable, located right after the open command.  

* If you want to scan different versions to get different data, just change the global variable <version>'s value.  
  
* Uncomment the last line to write down the data and version into a file name of your choice.  

### Potential Bugs:
I made this real fast so there are probably bugs, but for now it seems fine AND IT WORKS ON MY MACHINE (this is supposed to be a meta joke).
If there are any issues that is your fault though. =)
