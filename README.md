# Project 

This project is done in the context of my studies : "you have X hours, please code something !".

## Description

This project is an image classifier. 

I love having a look at my holiday's pictures but when it comes to storing them, well... I guess you're like me, I just procrastinate. A friend of mine sends me new pictures from the trip, I forgot to store them properly and my folder becomes a complete mess.

This project aims at helping to classify one's photos : you define periods of time like 'I was at New York from the 18th to the 24th...', and the project will create a folder for you, in which it will store, basing itself on their metadata, the corresponding pictures.

## How to use it 

The code has, for now, two main commands you can run : 
- ```make init``` : will initialize the file to define your periods
- ```make move``` : will create the folder from the period file and move the pictures 

More details lower.

## Detailed commands

### make init

Use : ```make init root_folder=<your_folder>```.

The root folder will be used as the target to create the template for the periods file.

### make move

Use : ```make init root_folder=<your_folder> period_file=<your_period_file>```.

For the root_folder, same as above.

For the period_file, it's an optional parameter. You might have defined the period file somewhere else and you want to point at it.