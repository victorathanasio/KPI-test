
# Welcome to the KPI-intelligence Demo !

This project was executed as a form of a technichal test for the position of summer internship at KPI-intelligence.

## Stage 1: REST API

All the functionalities of the REST API are under the module REST_API and they where implemented using Flask.

NB : For the id, I choosed a new indexation, because there were no consistent property that could be used as a Key in the json. (The nex indexation is just the order in with the elements are in the json).

# Stage 2: Web application

This stage was implemented using the library Dash.

The table in the Home Screen is :
* Scrollable from left to write, and up and down 
* Editable (So it acts as an endpoint,  and you can submit your changes using the button below the table itself)
* Has built-in filters
* Allows hiding undesirable columns.

To access **a page with all the details of a given investment**, you just select it in the table (by clicking in it, and the cell will turn red) and use the button "open in new window" (bellow the table) to see it's details. 


[Here](https://youtu.be/0c9O_Gs5f_U) we have a example of how to use some functionalities !

# Bonus stages

The endpoint in already working from the previous stage

The application can be found in this link (https://kpi-demo0.herokuapp.com/)

Due to the restrained time, here (http://jwallet.ml) you have another application that I developed during a hackaton (last week) with some very cool graphs (they are all interactive, do not hesitate in clicking in the first level of the pie-chart)

# Installation

Create a virtual environment:

```
python3 -m venv /path/to/new/virtual/environment
```

And activate it:

```
source /path/to/venv/bin/activate
```

In case of a problem, looking for the [documentation](https://docs.python.org/3/library/venv.html) is a good option.

After creating it, clone this repository:
```
git clone https://github.com/victorathanasio/KPI-test.git
```


After activating your virtual environment, you now need to download the requirements specified. To do so:
```
pip install -r requirements.txt
```

To run the application:

```
python app.py
```


# Support 

In case of help, feel free to contact Victor ([Github](https://github.com/victorathanasio), [e-mail](victor.athanasio@student-cs.fr), [Linkedin](https://www.linkedin.com/in/victor-athanasio/))


