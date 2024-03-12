## Deploying on toolforge

* To deploy changes in the code, you havet to log into toolforge, and become the
tool:
```
mylaptop> ssh myuser@login.toolforge.org
myuser@toolforge-sgebastion-10:$ become wikisaurusbot
wikisaurusbot@toolforge-sgebastion-10:$
```

* Then build the new image with the code:
```
wikisaurusbot@toolforge-sgebastion-10:$ toolforge build start https://github.com/wikisaurus/wikisaurusbot
.... takes a bit
```

Any new run of the scheduled jobs will now pull the new image and start running
it. If you want to force a run of a specific job, you can restart it:
```
toolforge job restart sandbox
```


## Adding new jobs
To add a new job, you have to add a new entry to the `Procfile` with the
command you want to run, and a new entry to the `jobs.yaml` file with the
schedule and with the new `Procfile` entry as `command`.

### Accessing the tool home directory
If the job needs to access the tool home directory, you'll have to add the
option `mount: all` to the `jobs.yaml` entry, and use `$TOOL_DATA_DIR` pointer
to the mounted tool home directory within the scripts/code.

### If you need to use environment variables
Then you'll have to create a wrapper script (for now) like the ones under
`scripts` and run that from the `Procfile` entry.


### Logs
By default the logs can only be retrieved with `toolforge jobs logs`, if you
need to have filelogs enabled, you have to add the options `filelogs: true` and
`mount: all` to the `jobs.yaml` entry for that job.


## Authentication
To authenticate, you have to setup the environment variables:
```
PWB_CONSUMER_TOKEN
PWB_CONSUMER_SECRET
PWB_ACCESS_TOKEN
PWB_ACCESS_SECRET
PWB_USERNAME
```

to match the oauth credentials (see https://wikitech.wikimedia.org/wiki/Help:Toolforge/Running_Pywikibot_scripts#Setup).



More information on the toolforge build service here:
https://wikitech.wikimedia.org/wiki/Help:Toolforge/Build_Service
