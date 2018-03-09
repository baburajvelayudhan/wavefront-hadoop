# wavefront-hadoop

This python script connect to a Hadoop Yarn cluster and extracts statistics about applications that are running or have finished in the last 5 minutes

# usage
```
python mapreduce.py
```
You should get a response similar to this:
```
usage: mapreduce.py [-h] [--username [USERNAME]] [--password [PASSWORD]] [server]
mapreduce.py: error: server must be provided
```
If the script is not executing, adjust the file permission and the Python interpret path.
