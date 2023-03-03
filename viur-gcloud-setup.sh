#!/bin/bash
project=$1

if [ -z "$project" ]
then
	echo "Usage: $0 PROJECT_ID"
	exit 1
fi

# Check if user is authorized with gcloud
echo "Check if user is authorized with gcloud..."
gcloud auth print-access-token >/dev/null 2>&1
if [ $? -ne 0 ]
then
  	# app does not seem to exist, will prompt for creation
	echo "##############################################################"
	echo "# Please authenticate your Google user with gcloud SDK to    #"
	echo "# execute administrative commands.                           #"
	echo "# In this step, a separate browser window opens to           #"
	echo "# authenticate.                                              #"
	echo "# This step is only required once on this computer.          #"
	echo "##############################################################"
	echo "Are you ready? [Y/n]"
	read Y

	if [[ ! ( "$Y" = "y" || "$Y" = "Y" || -z "$Y" ) ]]
	then
		echo "User aborted."
		exit 1
	fi

	gcloud auth login --no-browser
	if [ $? -ne 0 ]
	then
		exit 1
	fi
fi

# Check if app already exists
gcloud app describe --project=$project >/dev/null 2>&1
if [ $? -ne 0 ]
then
  	# app does not seem to exist, will prompt for creation
	echo "##############################################################"
	echo "# Please check and confirm that your project is created and  #"
	echo "# connected with a billing account in Google Cloud console.  #"
	echo "# Otherwise, some of the following calls may fail.           #"
	echo "##############################################################"
	echo "Continue? [Y/n]"
	read Y

	if [[ ! ( "$Y" = "y" || "$Y" = "Y" || -z "$Y" ) ]]
	then
		echo "User aborted."
		exit 1
	fi

	set -ex  # enable exit on error

	# Create the app engine app
	gcloud app create --project=$project --region=europe-west3
else
	set -ex  # enable exit on error
fi

# Activate APIs and Services
for service in firestore.googleapis.com iamcredentials.googleapis.com cloudbuild.googleapis.com cloudtasks.googleapis.com cloudscheduler.googleapis.com
do
	gcloud services enable --project=$project $service
done

# Configure Google Cloud Storage
gsutil uniformbucketlevelaccess set on gs://$project.appspot.com/

# Deployment of cron, queue and index settings
pushd deploy
for yaml in cron.yaml queue.yaml index.yaml
do
	gcloud app deploy -q --project=$project $yaml >/dev/null 2>&1
done

set +ex # disable error exit and debug

# Check if app engine default credentials are set
echo "Check if app engine default credentials are set..."
gcloud auth application-default print-access-token >/dev/null 2>&1
if [ $? -ne 0 ]
then
  	# app does not seem to exist, will prompt for creation
	echo "##############################################################"
	echo "# Please authenticate your Google user with gcloud SDK now   #"
	echo "# to set the application default user. This step is required #"
	echo "# to run ViUR applications locally without further           #"
	echo "# credentials that must be supplied from a file.             #"
	echo "# This step is only required once on this computer.          #"
	echo "##############################################################"
	echo "Are you ready? [Y/n]"
	read Y

	if [[ ! ( "$Y" = "y" || "$Y" = "Y" || -z "$Y" ) ]]
	then
		echo "User aborted."
		exit 1
	fi

	gcloud auth application-default login
	if [ $? -ne 0 ]
	then
		exit 1
	fi
fi

echo
echo "##############################################################"
echo "# All done!                                                  #"
echo "# You should now be able to run your project locally with    #"
echo "#                                                            #"
echo "#   viur run                                                 #"
echo "#                                                            #"
echo "# At first run, it might happen that some functions are      #"
echo "# causing error 500 because indexes are not immediately      #"
echo "# served. Therefore, maybe wait a few minutes.               #"
echo "#                                                            #"
echo "# Have a nice day.                                           #"
echo "##############################################################"
echo
