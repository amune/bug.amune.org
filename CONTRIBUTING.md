# Contributions Guidelines

You are welcome to contribute to this project. Here are the guidelines we try to stick to in this project.


* [Question or Problem](#question-or-problem)
* [Filing an Issue](#filing-an-issue)
* [Triaging Issues](#triaging-issues)
* [Feature Requests](#feature-requests)
* [Submission Guidelines](#submission-guidelines)
* [Coding Style](#coding-style)
* [Working Environment setup](#working-environment-setup)
  * [Simple setup](#simple-setup)
    * [Installing Project source code](#initializing-project-source-code)
  * [Detailed setup](#detailed-setup)
    * [Installing virtualenv](#installing-virtualenv)
    * [Installing Project source code](#installing-project-source-code)
    * [Installing Grunt](#installing-grunt)
  * [Configuring The Server](#configuring-the-server)
  * [Starting The Server](#starting-the-server)
* [Coding](#coding)
* [Running Tests](#running-tests)
  * [Functional Tests](#functional-tests)
* [Production Server Setup](#production-server-setup)
* [Acknowledgements](#acknowledgements)


## Question or Problem

If you have a question about the site or about web compatibility in general, feel free to join us in the #webcompat channel on the Mozilla IRC network. [Here's how to join](https://wiki.mozilla.org/IRC#Connect_to_the_Mozilla_IRC_server).

Otherwise, you can try to ping Mike Taylor on the Freenode network with the following command `/msg miketaylr hi I have a question about webcompat.com`.

## Filing an Issue

If you're using webcompat.com and something is confusing, broken, or you think it could be done in a better way, please let us know. Issues are how the project moves forward&mdash;let us know what's bothering you.

* Search the [issues
  list](https://github.com/webcompat/webcompat.com/issues)
  for existing similar issues.  Consider adding to an existing issue if you
  find one.
* Choose a descriptive title.
* Provide a test, snippet of code or screenshot that illustrates the problem. This small
  gesture goes a long way towards getting a speedy fix.

## Triaging Issues

One way to contribute is to triage issues. This could be as simple as confirming a bug, or as complicated as debugging errors and providing fixes. A tiny bit of effort in someone else's issue can go a long way.

## Feature Requests

You can request a new feature by [submitting an issue](#filing-an-issue) to our repo.  If you
would like to implement a new feature then consider what kind of change it is:

* **Major Changes** that you wish to contribute to the project should be discussed first in an issue or irc so that we can better coordinate our efforts, prevent
duplication of work, and help you to craft the change so that it is successfully accepted into the
project.
* **Small Changes** can be crafted and submitted as a Pull Request.


## Submission Guidelines

All code contributions should come in the form of a [pull request](https://help.github.com/articles/creating-a-pull-request), as a topic branch. You'll probably want to [set up a local development environment](#working-environment-setup) to get that far.

* Have a quick search through existing issues and pull requests so you don't waste any of your time.
* Make your changes in a new branch

	`git checkout -b name-of-fix-branch master`

* Create your patch; commit your changes

	`git commit -a`

* Push your branch to GitHub:

	`git push origin name-of-fix-branch`

* In GitHub, send a pull request to `webcompat.com:dev.webcompat.com`*.

To do this, click on the Edit button at the top of the Pull Request page.

![master](https://i.cloudup.com/tgBan6xVWt-2000x2000.png)

Select the `dev.webcompat.com` branch on the left hand side.

![change](https://i.cloudup.com/TZGd2ze3DL-2000x2000.png)

And you should be good to go.

![ready](https://i.cloudup.com/gE8awVDEyE-2000x2000.png)

* Continue discussion in the pull request.

After all that, if you'd like, you can add your name to our humans.txt file.

* `dev.webcompat.com` is our "development" branch where we can test, experiment, and deploy changes to dev.webcompat.com before merging into `master` and pushing to webcompat.com.

## Coding Style

### Python
As we are still very early in the project, we do not have yet that much conventions for naming, routes, APIs. In doubt, ask us or open an issue.  All Python code should pass [pep8](http://pep8.readthedocs.org/en/1.4.6/intro.html).

You can check this by installing the pep8 module.

    sudo pip install pep8

Once at the root of the project you can run it with

    pep8 --show-source --show-pep8 .

That will show you the list of errors and their explanations. Another tool, we have used for checking consistency of the code is `flake8` + `hacking`. [Hacking](https://github.com/openstack-dev/hacking) is a set of [OpenStack guidelines](http://docs.openstack.org/developer/hacking/) which is used by the community for the stability of their projects. You will see that there's nothing really hard about it.

    sudo pip install hacking

will install the relevant flake8 and hacking modules. In the same fashion, if you do

    flake8 .

You will get in return the list of mistakes. Some of the basics recommendations are:

* Modules are sorted by alphabetical order.
* Do not do relative imports (such as `from .foo import bar`)
* Import only modules not function name (because of possible name clashes)
* Group modules by categories (sys, libraries, project)
* When multilines docstrings are used. The first sentence is short and explains the module. Separated by a blank line.
* docstrings sentences are finished by a period.

When in doubt, follow the conventions you see used in the source already.

### CSS

@@something to write by magsout@@

### Javascript

@@something to write by miketaylr@@

## Working Environment setup

For testing code locally, you will need a very basic setup. There are a few requirements. These instructions have been made for working with Linux and MacOSX. If you install it successfully on Windows, we will appreciate a pull request on this documentation.

* Python 2.7
* node 0.10.0
* Github account with a fake repo

### Simple setup
#### Initializing Project source code

We use [Grunt](http://gruntjs.com/) as a task runner to perform certain things (minify + concat JS assets, for example). You need to have [Node.js](http://nodejs.org/download/) installed to be able to run Grunt.

``` bash
# clone the repo
git clone git@github.com:webcompat/webcompat.com.git
# change to directory
cd webcompat.com
# initializing project
[sudo] make init
```

### Detailed setup
#### Installing virtualenv



``` bash
# Install virtualenv
[sudo] pip install virtualenv
```

#### Installing Project source code

``` bash
# clone the repo
git clone git@github.com:webcompat/webcompat.com.git
# change to directory
cd webcompat.com
# set up virtual environment
virtualenv env
source env/bin/activate
# install dependencies
pip install -r requirements.txt
```

#### Installing Grunt

We use [Grunt](http://gruntjs.com/) as a task runner to perform certain things (minify + concat JS assets, for example). You need to have [Node.js](http://nodejs.org/download/) installed to be able to run Grunt. Once that's done, use `npm` to install the grunt dependencies. Version 0.10.0 or above is required.

First install the `grunt-cli` tool:

``` bash
[sudo] npm install -g grunt-cli
[sudo] npm install
grunt
```

### Configuring The Server

To test issue submission, you need to create a fake repo on github. Let's assume your username is `miketaylr`. Create a new repository called `nobody-look-at-this` (or the name of your choice).


``` bash
# set up config.py, filling in appropriate secrets and pointers to repos
cp config.py.example config.py
```

You can now edit `config.py` and

1. provide pointers to [repo issues URIs](https://github.com/webcompat/webcompat.com/blob/dev.webcompat.com/config.py.example#L40-L44). `ISSUES_REPO_URI = "<user>/<repo>/issues"`. With the example, we chose it would be `ISSUES_REPO_URI = "miketaylr/nobody-look-at-this/issues"`
2. It is **mandatory** to create your own personal bot for local development. The [instructions for creating a bot token](http://help.github.com/articles/creating-an-access-token-for-command-line-use) are given on GitHub. Once you created the token you can add it to the variable `BOT_OAUTH_TOKEN = ""`. This is the oauth token we use to report issues on behalf of people who don't want to give GitHub oauth access (or don't have GitHub accounts).
3. [get the secrets](https://github.com/webcompat/webcompat.com/blob/dev.webcompat.com/config.py.example#L24-L38) for config.py

**Note**: If you get a 404 at GitHub when clicking "Login", it means you haven't [filled in the `GITHUB_CLIENT_ID` or `GITHUB_CLIENT_SECRET`](https://github.com/webcompat/webcompat.com/blob/master/config.py.example#L47-L49).

![Auth 404](https://i.cloudup.com/8FDA5bVc7l.png)

### Starting The Server

``` bash
# start local server
python run.py
```

or

``` bash
# start local server
make start
```

You should now have a local instance of the site running at `http://127.0.0.1:5000/`. Please [file bugs](https://github.com/webcompat/webcompat.com/issues/new) if something went wrong!


## Coding


 ``` bash
 # watching CSS and JS
 make watch
 ```


## Running Tests

You can run tests from the project root with the `nosetests` command.

### Functional Tests

We use [Intern](http://theintern.io/) to run functional tests.

To run them, make sure you download the Selenium standalone server from the repo root:

``` bash
wget http://selenium-release.storage.googleapis.com/2.42/selenium-server-standalone-2.42.2.jar
```

The `firefox` binary will also need to be in your `PATH`. Here's how this can be done on OS X:

``` bash
export PATH="/Applications/Firefox.app/Contents/MacOS/:$PATH"
```

Start the Selenium and application servers (in separate terminal tabs or windows):

``` bash
java -jar selenium-server-standalone-2.42.2.jar
source env/bin/activate && python run.py
```

And to run the tests (in a new tab or terminal window):

``` bash
node_modules/.bin/intern-runner config=tests/functional/intern
```

Many tests require the ability to log in with GitHub OAuth. This is achieved by passing in a GitHub username: `user` and password: `pw` as command-line arguments:

``` bash
node_modules/.bin/intern-runner config=tests/functional/intern user=testusername pw=testpassword
```
## Production Server Setup

The current instance of webcompat.com has a nginx front server in front of the Flask application. These are the few things you need to know if you wanted to replicate the current configuration of the server. You will need to adjust for your own environment.

The configuration file is often located at something similar to:

```
/etc/nginx/sites-available/webcompat.com.conf
```

It depends on your local system. So we encourage you to read any documentation of your local server. You would then create a symbolic link to your local /etc/nginx/sites-enabled/. The gist of the nginx configuration file holds into

```nginx
server {
  listen 80;
  root $HOME/webcompat.com;
  error_log $LOGS/nginx-error.log;
  server_name webcompat.com;
  location / {
    # serve static assets, or pass off requests to uwsgi/python
    try_files $HOME/webcompat.com/webcompat/static/$uri $uri @wc;
    }
  location @wc {
    uwsgi_pass unix:///tmp/uwsgi.sock;
    include uwsgi_params;
    }
  }
```

We also have the following content type handlers.

```nginx
##
# Gzip Settings
##

gzip on;
gzip_disable "msie6";

gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_buffers 16 8k;
gzip_http_version 1.0;

# Turn on gzip for all content types that should benefit from it.
gzip_types application/ecmascript;
gzip_types application/javascript;
gzip_types application/json;
gzip_types application/pdf;
gzip_types application/postscript;
gzip_types application/x-javascript;
gzip_types image/svg+xml;
gzip_types text/css;
gzip_types text/csv;
# "gzip_types text/html" is assumed.
gzip_types text/javascript;
gzip_types text/plain;
gzip_types text/xml;
```

We are also using [uWSGI](http://uwsgi-docs.readthedocs.org/en/latest/index.html).

```
upstream uwsgicluster {
  server 127.0.0.1:8080;
}
```

with the following configuration file `uwsgi.conf`

```
# our uWSGI script to run webcompat.com

description "uwsgi service"
start on runlevel [2345]
stop on runlevel [06]

respawn

# .ini files for dev.webcompat.com (development.ini) and webcompat.com (production.ini) are in $HOME/vassals
exec /usr/local/bin/uwsgi --emperor $HOME/vassals
```

We have been using [uWSGI Emperor](http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html) to manage two environments for staging and production. It gives us the possibility to test features which are not yet fully ready for production without messing the actual site.

`production.ini`

```ini
[uwsgi]

socket = $FOO/uwsgi.sock
chmod-socket = 666
chdir = $HOME/webcompat.com/
env = PRODUCTION=1
master = true
module = webcompat
callable = app
logto = $LOGS/uwsgi.log
```

and `staging.ini`

```ini
[uwsgi]

socket = $FOO/uwsgi2.sock
chmod-socket = 666
chdir = $HOME/staging.webcompat.com/
env = DEVELOPMENT=1
module = webcompat
callable = app
logto = $LOGS/staging-uwsgi.log
```

Hopefully this will help you to clear up a few struggles.

## Acknowledgements
A lot of this document was inspired directly by the excellent [Backbone.LayoutManager](https://github.com/tbranyen/backbone.layoutmanager/blob/master/CONTRIBUTING.md), [CouchDB](https://github.com/apache/couchdb/blob/master/src/fauxton/CONTRIBUTING.md), and [Angular.js](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#issue) CONTRIBUTING files.

