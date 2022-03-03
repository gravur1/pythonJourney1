###################
#### You can have virtual envs to safely distribute scripts that would depend on modules. 
#### For you to do that, you can configure your virtual env and distribute it as needed.
#### when calling it, you can do something like this as part of a sh script:
# source second_env/bin/activate
# python sqlalchemy_script.py
# deactivate
###################

# Installing the venv module
    # pip install virtualenv --upgrade
# Installing virtual env
    #virtualenv first_env
# Setting python to use python2 as the default versoin
    #virtualenv -p /usr/local/bin/python2 first_env

#Activating a specific venv
    #source first_env/bin/activate
