FROM python:3.7
MAINTAINER Jordon Kopp (koppj)

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
# TODO: Expose future info endpoint used for build/deploy verification
# Add build-args for ts, hash, version etc
#ARG arg_git_hash
#ARG arg_jenkins_build_num
#ARG arg_jenkins_build_url
#ARG arg_jenkins_build_ts

# Set build-arfs to ENV vars
#ENV COMMIT_HASH=$arg_git_hash
#ENV BUILD_NUM=$arg_jenkins_build_num
#ENV BUILD_URL=$arg_jenkins_build_url
#ENV BUILD_TS=$arg_jenkins_build_ts

ENTRYPOINT ["entry_point.sh"]