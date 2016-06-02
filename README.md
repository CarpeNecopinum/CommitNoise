# CommitNoise

Are you jealous of all the fancy commit strips of all the cool people on github?

Is most of your work under NDAs so your github looks like a desert?

Do you want to impress potential employers, who only look at how many commits you made?

Then this is the script for you!

## Installation

Should just work out-of-the-box with Python3.

## Usage
```
usage: commitnoise.py [-h] [--average AVERAGE] [--variance VARIANCE]
                      [--minimum MINIMUM] [--folder FOLDER]
                      [--start-date START_DATE] [--end-date END_DATE]

Create a repository of empty commits to make your github history look good.

optional arguments:
  -h, --help            show this help message and exit
  --average AVERAGE     Number of commits to produce per day on average
  --variance VARIANCE   Variance of the commits per day
  --minimum MINIMUM     Minimal number of commits per day
  --folder FOLDER       Path of the repository to "enhance"
  --start-date START_DATE
                        First day for enhancements to start
  --end-date END_DATE   Last day for enhancements
```
