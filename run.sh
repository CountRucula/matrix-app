#!/bin/bash
# Name of the branch to check
branch="main"

# name of virtual environment
venv=.venv

# Check network connectivity
if ping -c 1 google.com &> /dev/null
then
  echo "Network is accessible."
    # Fetch updates from the remote repository
    git fetch

    # Compare the local and remote branches
    LOCAL=$(git rev-parse @)
    REMOTE=$(git rev-parse @{u})

    if [ $LOCAL != $REMOTE ]; then
        echo "There are changes available to pull."

        # Show the commit message from the available pull
        echo "Commit message from the available pull:"
        git log --oneline $LOCAL..$REMOTE

        sleep 5

        # Pull the changes
        git pull origin $branch
        
        # check if virtual enviroment exists, if not => create one
        if ! [-d $venv/bin]
        then
            echo "Virtual enviroment does not exist."
            python3 -m virtualenv $venv
        fi
        
        # activate venv
        echo "Activating virtual enviroment"
        source $venv/bin/activate

        # install modules
        echo "Installing python modules"
        pip install -r requirements.txt

        # Restart the script
        echo "Restarting the script..."
        sh $0

    else
        echo "No changes available to pull."
    fi
else
  echo "Network is not accessible."
fi

echo "Starting the application..."
sleep 2

export DISPLAY=:0
$venv/bin/python3 src/main.py
