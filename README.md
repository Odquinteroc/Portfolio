# Portfolio

This portfolio is created to store all data analysis, data science and data engineer projects

## Pandas Analysis Project

### Data Exploratory

* In this project we will take stats from certain videos of a channel of youtbe and we are going to analysis using pandas, matplotlib, seaborn, etc. Also we are going to take csv file from web and save it locally using the library urlib.
* I inspected the data using the pandas, to open the data and create a DataFrame we used the function `raw = pandas.read_csv()` and save the data in a variable call row
* I used the pandas function `raw.info` over the DataFrame we retrieve the information of each columns ( Data types, Null values, etc ) to realize what are our datatypes and what are the missing values.
* I used the pandas function `raw.describe()` to generate a descriptive statistics
* the pandas Function `raw.nlargest("# of row", columns)` shows in order highest average percentage viewed
* I made some data explorations to identify patterns using the function `raw.hist()`
* I check correlation of the features (columns), see how the columns correlate, the number closer to 1 indicate a stronger positive correlation on the flip side a number closer to -1 indicate a negative correlation
* to see the data patterns in a better way I plot the data without outliers data to do that I took the videos with the most views, in this case two video perfomr better than the rest, I set up limit for outliers, to exclude those, Iset an upper limit by computing the 99th quantile of the views using the  pandas function `raw["Views"].quantile(0.99)` over the columns views.  digging deeper into the correlation using the seaborn pair plot "sns-pairplot()"computing the chart to get a pairwise relationship for each columns with a contidions over the columns views `sns.pairplot(raw.query("Views < @q_hi"))`

### Cleaning the data

* to clean the data I Created a function to clean the dataframe, with two argument the first is the DataFrame, and seconed the viws threshold set to 500
* Using the function `.drop()` i deleted some columns,
* Using the `.dropna()` function to remove the NaN Values
* I used The `.pipe()` method takes a function as an argument, applies that function to the DataFrame, and returns the result, `.pipe(clean_columns)` methods clean the columns name removes whitespace and replace special charactes
* I reneme the columns  name using the function `.rename("columns_name")`
* The `.assing()` method is used to create a new column o modify the existing one within the assigne method I select the columns that Iwant to change or create,
* the first column take video_publish_time columns and  use  the lambda function to create a function that receives as argument the dataframe and using the pandas functions .to_datetime to change the datatypes as Date object `video_publish_time=lambda df_: pd.to_datetime(df_.video_publish_time)`
* the second columns create a new column days_since_published use the .to_datetime functions with "today" parameters as result get todays date and rest today date with the date since was published and takes de object datetime and takes the days and use .astype to covert it in a integers `days_since_published=lambda df_: (pd.to_datetime("today") - df_.video_publish_time).dt.days.astype(int)`
* the third column create a new columns taking the likes columns and dividing them with the days_since_published and round it with two decimal `likes_to_view_ratio_pct=lambda df_: ((df_.likes / df_.views) * 100).round(2)`
* the fourth column likes_to_view_ratio_pct and using the lamnda function takes the likes columns and dividing them with the viws columns,
* the fifth column comments_to_view_ratio_pct using the lamnda function create a ratio taking ccomments_added column and dividing with the views columns `omments_to_view_ratio_pct=lambda df_: ((df_.comments_added / df_.views) * 100).round(2)`

### Plot the data

* lets see some functions to plot the data
* this function `.set_index("video_publish_time") ` set the index with the value in the columns video_publish_time and sorted it
* using the plotly express library, `px.line()` created a line plot
* The arguments inside the previous functios are:  (dataframe, axis x, axis y, template, hover_name, and the title that will apper )`px.line( df, x=df.index, y=columns, Template="simple_white", hover_name="video_title",title=f"Development{','.join(columns).title()}`
* the hover_name argument it Specifies a column in the DataFrame to provide hover information for each data point.
* I used the function `fig.update_layout(hovermode="x unified", margin=dict(l=0, r=0, t=50, b=5))` to set some change to the plot. hovermode="x unified" is when hovering over data points on the plot, the hover labels will be shown for all traces at the same x-coordinate. This is useful for comparing values across multiple traces.
