#!/bin/sh

heroku create cbapi-$BITBUCKET_BRANCH

# if doesn't succeed, manually add git remote
#if [ $? -ne 0 ]; then
#  heroku git:remote --app=cbapi-$CI_ENVIRONMENT_SLUG
#fi

# Force exit 0 in case feature has already been deployed to heroku
exit 0
