#!/bin/bash

heroku create cbapi-$CI_ENVIRONMENT_SLUG

# if doesn't succeed, manually add git remote
#if [ $? -ne 0 ]; then
#  heroku git:remote --app=cbapi-$CI_ENVIRONMENT_SLUG
#fi

exit 0
