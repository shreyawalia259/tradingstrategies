# Generating Materials on Trading Strategies: Spring 2021

## Introduction 
Being able to predict stock trends in the near future can be very useful in making a profit since you buy and sell at the right times. However, stocks can be very volatile and unexpected events can lead to values that no one saw coming. 

Hence, this project focused on finding strategies that could give a general idea of when would be a good time to buy, hold or sell your stocks. Another point of focus was on finding data visualization techniques that would help visualize and analyze stock performance based on metrics such as RSI. Basically, the idea of the project was to find resources that provided easy to use and accessible information on trying to capture the trends in stock prices. 
<h2>
 
## The Objective
* Evaluating existing trading strategies implemented in Python to potentially create a teaching module for a financial data analysis course.
* Extra: Looking into creating a dashboard tracking stock performance and strategy performance. 
<h2>

## Working Towards the Objective 

### Step 1: Source Evaluation
The first step in starting this project was finding sources that had tried to tackle these problems before and solved them successfully. The sources evaluated and used in the project were provided by Professor Huo in the form of articles were people presented the strategies they had come up with and worked on. The first thing I checked in evaluating each resource was looking at the reporducibility of their code. Of the code was outdated, the websites they used outdated or the libraries hard to find, then it was not accessible to anyone and the point of this porject is to find examples that anyone could implement and reinvent with basic knowledge in python.

This evaluation was noted down in the source evaluation file in the appendix of the github repository where all the articles are divided into two sections: Reproducible and Non-Reproducible. 

After getting the main category down, I wrote a summary for each article talking about the main goals of the author whether they were implementing a strategy, teaching basic analysis of performance metrics or focusing on the visualization of those performance metrics. I also took note of what strategy they were using and what external libraries were needed to run their code successfully. Lastly, I identified the articles that were a good teaching resource separately because of the end goal of possibly using these articles to create a teaching module. 

These summaries of each article was then added to their respective codes as well so that the reader could have a good understanding of what they were running. 

<h3>
 
### Step 2: Reproducing Results and Annotations
In reproducing the results, I ran all the code from the authors' github in Jupyter Notebooks. I quickly realized that a lot of the libraries needed to be installed on my device still in order to run the code. Upon coming across that obstacle, I created an installations file where I put down the installation commands for each required libraries for all the repsective case studies. So the user would have to run this file once and they could easily work on any case study they wanted after.

As stated, the code from each source has a summary at the beginning for understanding what the function of the code is. To further explain all the steps, I added an explanation for each step in the code so that it is easy to follow. It also makes it easier to understand how certain functions work and how to use them even if the user had never seen them before. 

In total there are 7 case studies that were reproducible from all the articles. These case studies include data visualization, forecasting and screening techniques.A lot of them focus on Moving Average Convergence Divergence which is a simple yet effective method of creating a signal to buy and sell for. These case studies are also simple to follow for beginners. Overall, the case studies together provide a good introduction into conducting data analysis on stock prices. 
<h3>
 
### Step 3: Finance Libraries’ Guide
One thing I noticed from the articles is that several of them used the Yfinance library to pull data on stock open, close, high and low prices instead of scraping through the website information. This method looked really simple with a lot of customization options using tickers such as pulling data in 30 minute intervals or monthly or annually. Hence, I created a simple guide on how to install this library, how to use Tickers to pull data and how to convert it into a dataframe to manipulate the data easily.

Another library included in that guide is the Technical Analysis Library(Ta-lib). This library is extremely useful in calculating MACD signal and histogram in one line of code and other such measures. For example any kind of moving average, simple or exponential. And since it can caculate the MACD signal and histogram it is really easy to plot the calculations and see when you should keep or sell your stocks without having to put too much of user effort in. So, I included an installation and use guide for this library too since it is so helpful in implementing any trading strategies and visualizing them. 
<h3>
 
### Step 4: Teaching Module Examples
Since a possible outcome of collecting all the articles and their reproducible code is to create a teaching module from it, I created two examples of teaching modules that can be constructed. One example is teaching all theory first and then including the case studies as something to experiment with and learn application of the taught theory. The other idea includes focusing on each case study indidvually and learning about each tool or technique as it comes in each example.

These ideas are very roughly organized since this is a possible outcome in the future and not a direct result of the project immediately. 
<h3>

### Step 5: Resource Organization
The last step was to organize all the collected articles, their reproducible code and the library guides into a github repository so that anyone could access it and use it as a learning resource. So, it had to be set up in a way that anyone could immediately understand how to navigate the repository, and be able to go through each folder and actually get an introduction to and learn how to visualize, analyze and create strategies on stock price trends. 

So the way I ended up finally organizing all the materials is by including the source evaluation and teaching modules in the appendix because these were more for personal use as outcomes in the project than for an external user. The next step was to take all the reproducible code, and present them as case studies as a main folder. In thsat, I included the source evaluation for each case study separarelty so people could pick and choose what they wanted to learn and apply. I also included the installations file here and the guide to accessing and self implemeneting tools in the Yfinance and TA-lib libraries. I also included a simple explanation of the MACD concept and strategy since it seems to be the most popular applied strategy recently. Finally, I also have a folder on dashboard creation attempts as mentioned later. 
<h3>
 
### Extras: Dashboard Creation
This objective was an added later in the semester. The main purpose of it was to learn how to create a simple dashboard and have a brief guide in it. The starting point of this project was looking at the dashboard created by GaTech CS students. From there I worked on creating a simpler version of the dashboard where I included covid new cases data that updated daily and included projected forecasts by either a research intitute or any other source.

In my research, I found that a lot of people preffered tableau for this sort of implementation and was able to find a guide on the tableau website on how one could create a dashboard containing covid data. I downloaded their example case study and the data from the same source they got theirs. Once I had these two things, I tried to create my own dashboard in tableau that was essentially a replication of the case study they provided. Since this was an additionaly thing to work on and not the original outcome, I have not reached the stage of creating a guide yet. My progress has been learning how to create plots in Tableau and put them in your final dashboard. I stopped just short of adding the projected forecasts of the number of new cases. 
<h3>
 
<h2>
 
## Remarks
This project was very interesting to work on and made me realize the number of ways you can manipulate and analyze the same set of data. It definitely opened my mind to new techniques. I also enjoyed creating the guides on the libraries and annotating all the code in the case studies. Doing that felkt good because hopefully one day this information will be useful to someone someday and it improved my knowledge of the coding language. It also showed me how essential external libraries can be. It was also a great oppurtunity to start learning about how one would go about creating a dashboard.
<h2>

## Future Recommendations
In the future maybe someone can work on finding more articles or authors to create a wholistic study guide and be able to fully convert the found materials into a teaching module so that students or any other user can access it and learn a great deal from it. 
<h2> 






