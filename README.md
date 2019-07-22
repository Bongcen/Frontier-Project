# Frontier-Project (Pelita Harapan University)
# Traffic Light Analysis
**Data Source:**
> [LISA Traffic Light Dataset](https://www.kaggle.com/mbornoe/lisa-traffic-light-dataset)

**Team Member:**
  - [_Bong Cen Choi_](https://github.com/Bongcen)
  - [_Gabriel Dejan P._](https://github.com/gabrieldejan17)
  - [_Joshua Kaven K._](https://github.com/Nevaks)

## Content
The database is collected in San Diego, California, USA. The database provides four day-time and two night-time sequences primarily used for testing, providing 23 minutes and 25 seconds of driving in Pacific Beach and La Jolla, San Diego. The stereo image pairs are acquired using the Point Grey’s Bumblebee XB3 (BBX3-13S2C-60) which contains three lenses which capture images with a resolution of 1280 x 960, each with a Field of View(FoV) of 66°. Where the left camera view is used for all the test sequences and training clips. The training clips consists of 13 daytime clips and 5 nighttime clips.

## Annotations
The annotation.zip contains are two types of annotation present for each sequence and clip. The first annotation type contains information of the entire TL area and what state the TL is in. This annotation file is called frameAnnotationsBOX, and is generated from the second annotation file by enlarging all annotation larger than 4x4. *The second one is annotation marking only the area of the traffic light which is lit and what state it is in*. This second annotation file is called **`frameAnnotationsBULB`**.

The annotations are stored as 1 annotation per line with the addition of information such as class tag and file path to individual image files. With this structure the annotations are stored in a csv file, where the structure is exemplified in below listing:

Filename;Annotation tag;Upper left corner X;Upper left corner Y;Lower right corner X;Lower right corner Y;Origin file;Origin frame number;Origin track;Origin track frame number

## Dataset used in this project: 
[**frameAnnotationsBULB**](https://github.com/Bongcen/Frontier-Project/blob/master/Trained%20Dataset/frameAnnotationsBULB.csv)
 
## Prerequisites
You'll need the following:
- [Orange](https://orange.biolab.si/download)
- [Python Dash](https://dash.plot.ly/)
- Pandas
- Plotly

## Installing
1. Open Command Prompt/Orange Command Prompt that have python and go to your directory
```bash
cd Frontier-Project
```
2. Install the following library
```bash
pip install dash==1.0.2  # The core dash backend (check newest version on dash.plot.ly)
pip install dash-daq==0.1.0  # DAQ components (newly open-sourced!)
pip install pandas
```
3. Run .py program
  ```bash
  python app.py
  ```
4. Wait python's execution program untill it's given the http site
  ```bash
  Running on http://127.0.0.1:8050/
  ```
5. Open your browser, and insert the http
>http://127.0.0.1:8050/
6. Press CTRL+C in your Command Prompt to exit from python's program

## Running the tests
	1. Scatter Graph
		You can set the slider at the above of the Graph to scale the size of data by the day.
		Or you can choose the radioitems at the bottom of the Graph, to see which class data you want to be used.
	2. Bar Graph
		You can't do any input here.
![web](https://github.com/Bongcen/Frontier-Project/blob/master/Screenshots/Web.PNG)

### Coding Style
- **Graph Bar**
```python
    dcc.Graph(id='bar_plot',
			figure=go.Figure
			(
				data=[
					go.Bar(name='Actual', x=df['Annotation'], y=df['tAnnotation']),
					go.Bar(name='RandomForest', x=df['RandomForest'], y=df['tRandomForest'], text=df['RF']),
					go.Bar(name='kNN', x=df['kNN'], y=df['tkNN'], text=df['RF']),
					go.Bar(name='AdaBoost', x=df['AdaBoost'], y=df['tAdaBoost'], text=df['RF'])
					],
					layout=go.Layout(barmode='group'
						#yaxis = go.layout.YAxis(tickformat = '%')
					)
			
			)
		)
```
- **Scatter Plot**
```python
'data': [
	go.Scatter(
		x=dff[dff[selected_methods] == i]['No'],
		y=dff[dff[selected_methods] == i][selected_methods],
		text=dff[dff[selected_methods] == i]['day'],
		mode='markers',
		opacity=0.7,
		marker={
			'size': 15,
			'line': {'width': 0.5, 'color': 'white'}
		},
		name = i
	) for i in dff.Annotation.unique()
],
```
- **Dash Core Component**
	1. RadioItem
	```python
	dcc.RadioItems(
		id='RI',
		options=[
			{'label' : i, 'value': i} for i in ['Annotation','RandomForest','kNN','AdaBoost']
		],
		value='Annotation',
		labelStyle={'display': 'inline-block'}
	)
	```
	2. Range Slider
	```python
	dcc.RangeSlider(
		id='no-slider',
		min=df['No'].min(),
		max=df['No'].max(),
		step=1,
		marks={
			1: 'Day 1',
			2: 'Night 1',
			3: 'Day 2',
			4: 'Night 2'
		},
		value=[df['No'].min(), df['No'].max()]
	)
	```
- **Callback**		
is use for updating the plot with the input data. In this case, we used RadioItem as 'RI' and Range Slider as 'no-slider' for the input data. For the output is a Graph as 'clustering'.
```python
@app.callback(
	Output('clustering', 'figure'),
	[Input('RI', 'value'),
	 Input('no-slider', 'value')])
def update_graph(selected_methods, r_slider):
```

## Deployment
### Test & Score
In here, we train the data with the best 3 models:
1. Random Forest
2. kNN
3. AdaBoost
- The target of this Test & Score evaluation is the "Annotation" Class
- We used K fold Cross validation with number of folds: 5
- Stratified: rearrange the data in a way that each fold has a good representation of the whole dataset.
>![testscore](https://github.com/Bongcen/Frontier-Project/blob/master/Orange%20Documentation/Test%26Score.jpg)
>- Area under ROC is the area under the receiver-operating curve.
>- Classification accuracy is the proportion of correctly classified examples.
>- F-1 is a weighted harmonic mean of precision and recall (see below).
>- Precision is the proportion of true positives among instances classified as positive, e.g. the proportion of Iris virginica correctly identified as Iris virginica.
>- Recall is the proportion of true positives among all positive instances in the data, e.g. the number of sick among all diagnosed as sick.

### Confusion Matrix
In here, we can see Test & Score output from each models that used to train the data. The numbers show correctly and incorrectly classified instances.
>- AdaBoost Model 
![adaboost](https://github.com/Bongcen/Frontier-Project/blob/master/Orange%20Documentation/confusionMatrix(Adaboost).jpg)
>- Random Forest Model 
![randomforest](https://github.com/Bongcen/Frontier-Project/blob/master/Orange%20Documentation/confusionMatrix(RandomForest).jpg)
>- kNN Model 
![knn](https://github.com/Bongcen/Frontier-Project/blob/master/Orange%20Documentation/confusionMatrix(KNN).jpg)

## Acknowledgements
> Jensen MB, Philipsen MP, Møgelmose A, Moeslund TB, Trivedi MM. Vision for Looking at Traffic Lights: Issues, Survey, and Perspectives. I E E E Transactions on Intelligent Transportation Systems. 2016 Feb 3;17(7):1800-1815. Available from, DOI: 10.1109/TITS.2015.2509509

> Philipsen, M. P., Jensen, M. B., Møgelmose, A., Moeslund, T. B., & Trivedi, M. M. (2015, September). Traffic light detection: A learning algorithm and evaluations on challenging dataset. In intelligent transportation systems (ITSC), 2015 IEEE 18th international conference on (pp. 2341-2345). IEEE.
