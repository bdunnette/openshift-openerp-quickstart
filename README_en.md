# OpenShift OpenERP quickstart

This quickstart contains an OpenERP installation ready to run on OpenShift. It uses nginx to serve static files and runs under python-2.7.

If you don't have an account yet, go to http://getupcloud.com and register for a free trial.

## Create your app

First, create an application with PostgreSQL:

```
$ rhc app create openerp https://reflector-getupcloud.getup.io/reflect?github=caruccio/openshift-nginx-python postgresql-9
```

Then, merge and push this repo into your new app. Please be patient, this operation may last for a long time.

```
$ cd openerp/
$ git remote add upstream https://github.com/caruccio/openshift-openerp-quickstart.git
$ git pull -s recursive -X theirs upstream master
$ git push
```

That is it!

Point your browser to [https://openerp-$namespace.getup.io](https://openerp-$namespace.getup.io) and login.
Default credentials are:

```
Username: admin
Password: admin
```

## Upgrade

This quickstart ships with a nightly build of opernerp from file http://nightly.openerp.com/7.0/nightly/src/openerp-7.0-20131221-002451.tar.gz

To upgrade openerp source, replace the content of directory `wsgi/openerp` with a new version. Please note that any code customization may be lost

```
$ cd openerp/
$ wget http://nightly.openerp.com/7.0/nightly/src/openerp-7.0-latest.tar.gz
$ tar xvf openerp-7.0-latest.tar.gz
$ mv openerp-7.0-$TIMESTAMP/* wsgi/openerp/
$ git add wsgi/openerp
$ git commit -a -m "Upgrade to version XXX"
$ git push
```
