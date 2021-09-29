# DumbleBot Work in Progress
 Dumbledore AI Chatbot

## Description
DumbleBot is a deep learning chatbot that utilizes a sequential model from Keras to imitate a conversation with Albus Dumbledore from the Harry Potter series. 
The repository includes 
 - the Jupyter Notebook used data collection along with all used and unused training data
 - the final model used 
 - the web application used to demo the model built using Flask

## Motivation 
DumbleBot is a personal project I decided pursue in my spare time with the purpose of creating a holistic start to finish product. My projects up till now have been focused on specific skills and largely with the sole purpose of self learning. Being able to learn specific skills and applying them to concepts that personally interest me is how I’m able to stay focused and not feel burnt out. As a data scientist, I’ve gained a spectrum of skills ranging from data visualizations through dashboards, to applied machine learning and deep learning. However, working at my current job has taught me that in addition to the technical side, the presentability of a project as a product is equally important. For this reason I wanted to learn how to use flask, in order to further develop my product semse as a data scientist 

## Screenshots 
Here's a preview of a the webapp in action
![Screen Shot 2021-09-29 at 21 08 08](https://user-images.githubusercontent.com/42952515/135324788-509fabf8-15a1-4681-b48f-6fd0cf3a2a4a.png)

## Quick Setup 
 

1. Clone the repository
```
$ git clone https://github.com/kayhanliao/DumbleBot.git
$ cd DumbleBot
```
2. Create and activateenviroment (optional, but you really should). I prefer using conda, however virtualenv should work fine. 
```
$ conda create --name myenv 
$ conda activate myenv
```
3. Install dependencies
```
$ pip install -r requirements.txt
```
4. Run in deevelopment server to demo
```
$ python app.py
```
5. Navigate to [http://localhost:5000](http://localhost:5000)

## To-Do
wip
1. Develop UI
2. Improve training data
3. Add customizable username text (Dumbledore will refer to user by their selected name)
4. Dockerize and deploy on personal server or Heroku

## Blog post
