
# Simple Service with AWS Fargate for Amazon ECS Windows containers

This CDK v2 application deploys a VPC and a load balanced ECS service powered by AWS Fargate for Amazon ECS Windows. It uses
the [publicly available container](mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019) provided by Microsoft which is a basic installation of IIS.

## Install Prerequisites

Make sure you have the latest version of the [CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) and
[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed.

Next, install the dependencies required by this app. It uses `Pipenv` for python dependency management, so make sure
[Pipenv](https://pipenv.pypa.io/en/latest/install/) is installed.

Once installed, run the following:

```bash
pipenv --python 3.9
pipenv shell
pipenv install
```

## Deploy

Once the dependencies are installed, it's time to synthesize and deploy!

```bash
# Synthesize the app and see what it generates
cdk synth
# If the above looks OK, deploy!
cdk deploy
```
