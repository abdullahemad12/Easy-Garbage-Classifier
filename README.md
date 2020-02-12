# Easy Garbage Classifier

This project was part of a hackathon that took place in November 2019. The hackathon 
was sponsored by Raisa and GUC brain under the name of Enviromental Sustainability Hackathon.


## Idea 

Our idea aims at automating the process of garbage classification through having a 
machine/robot looking at a pile of trash, detect the different objects through its camera,
and classify each object into one of 6 classes: 

1. Cardboard
2. Glass
3. Metal 
4. Paper
5. Plastic 
6. Trash 

 
Due to the time constraints, we have only decided to work on the garbage classification task. 
Which, given a photo of a single item, classifies them as one of the 6 classes.The training of the model was done on 
google colab to make use of GPU accelerator. We achieved an accuracy of ~85% on the training data set and ~80% on the testing dataset.

## Run 

To run this project you need the following requirments

1. Numpy
2. Tensorflow 
3. Pillow
4. Keras
5. tkinter
6. OpenCV 

Run the following command to start up the project

python gui.py

## Future Work 

1. Object detection on picture with many items 
2. Robot that actually process the garbage and physically separates them into groups

## Contributers 


| [<img src="https://avatars0.githubusercontent.com/u/20978361" width="150px;" height="150px;"/><br /><sub><b>Abdullah Emad</b></sub>](https://github.com/abdullahemad12) | [<img src="https://avatars3.githubusercontent.com/u/20912763" width="150px;" height="150px;"/><br /><sub><b>Ahmed Shawky</b></sub>](https://github.com/Ahmed-ShawkyEgy)| [<img src="https://avatars0.githubusercontent.com/u/40171045" width="150px;" height="150px;"/><br /><sub><b>Yassin Chaddad</b></sub>](https://github.com/yassinchaddad)
| :---: | :---: | :---: | 
