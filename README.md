# Bird Tracker Data Analysis Microservice

## Communication Contract
1. Communication will take place over Discord.
2. Respond to teammates within 24 hours.
3. A back-up plan for microservices will take effect if a team member has become unresponsive fro over 72 hours.
4. Establish clear deadlines and stick to them.
5. Ask for help when needed and provide help when able.

## How to Request Data
First, ensure that the microservice is running while your main program is running. The microservice will continuously check the tracker_data.csv file for updates.
When changes to the tracker_data.csv file are detected, the microservice will analyse the data in the file.
<br/>
The following is an example of how to call the microservice
```
# Assume 'birdTracker.birds.csv' is and exported file from the bird tracker database
# Open the 'birdTracker.birds.csv' and 'tracker_data.csv' files

with open('birdTracker.birds.csv', 'r') as inputfile:     
  with open('tracker_data.csv', 'w') as trackerfile:
    # Copy the data from 'birdTracker.birds.csv' to 'tracker_data.csv'
    for line in datafile:                            
      trackerfile.write(line)
```

## How to Receive Data from the Microservice
The microservice will analyse the data in the tracker_data.csv file and print the results to the file OutputFile.txt.
<br/>
OutputFile.txt will contain a tuple consisting of:
- Total number of bird sightings
- Species with the most number of sightings
- The number of sightings for the most sighted bird
<br/>
If more than one species has the maximum number of sightings, OutputFile.txt will contain a tuple for each species.
<br/>
<br/>
Here is an example output from OutputFile.txt where there is one species with the maximum number of sightings:

```
(13, 'American Goldfinch', 5)
```
Here is an example output from OutputFile.txt where there is more than one species with the maximum number of sightings:

```
(13, 'American Goldfinch', 5)
(13, 'Eastern Bluebird', 5)
```
Below is an example of how to collect the data from OutputFile.txt:

```
with open('OutputFile.txt', 'r') as file:
  for line in file
    print(line)
```

## UML Diagram
![Drawing](https://github.com/user-attachments/assets/09a94a89-e36a-4165-b139-f107552895fe)

