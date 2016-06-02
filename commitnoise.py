#!/usr/bin/env python
from datetime import date, timedelta
from dateutil import rrule
from random import gauss
import os

class CommitNoise:
    def init(self):
        # Some defaults, should somebody decide to use this as a library
        self.average  = 5
        self.variance = 3
        self.minimum  = 0
        self.start    = date.today() - timedelta(days=3)
        self.end      = date.today()

    def setDistribution(self, average, variance):
        self.average  = average
        self.variance = variance

    def setMinimum(self, minimum):
        self.minimum = minimum

    def setDatespan(self, start, end):
        self.start = start
        self.end   = end

    def enhanceRepo(self, repoPath):
        template = "git commit --allow-empty --date={date} -m '{message}'"
        if not os.path.isdir(repoPath):
            os.mkdir(repoPath)
            os.system("git init")
        os.chdir(repoPath)

        for dt in rrule.rrule(rrule.DAILY, dtstart=self.start, until=self.end + timedelta(days=1)):
            num_commits = round(max(self.minimum, gauss(self.average, self.variance)))
            for idx in range(num_commits):
                command = template.format(date=dt.isoformat(), message="Commit no.%d of today." % idx)
                #print(command)
                os.system(command)

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Create a repository of empty commits to make your github history look good.")
    p.add_argument('--average', default=5, type=float, help='Number of commits to produce per day on average')
    p.add_argument('--variance', default=5, type=float, help='Variance of the commits per day')
    p.add_argument('--minimum', default=0, type=int, help='Minimal number of commits per day')
    p.add_argument('--folder', default='noise', help='Path of the repository to "enhance"')
    p.add_argument('--start-date', default=date.today() - timedelta(days=480), help='First day for enhancements to start')
    p.add_argument('--end-date', default=date.today(), help='Last day for enhancements')
    args = p.parse_args()

    noise = CommitNoise()
    noise.setDistribution(args.average, args.variance)
    noise.setDatespan(args.start_date, args.end_date)
    noise.setMinimum(args.minimum)
    noise.enhanceRepo(args.folder)
