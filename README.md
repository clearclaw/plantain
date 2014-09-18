Plantain
========

![Plantain](plantain.jpg)

A commandline tool for managing the lifecycle of Mandrill templates.

In short, `plantain` allows the user to manage their Mandril email
templates from the commandline, perhaps as part of their configuration
management system (eg Salt, Ansible, cfengine, Chef, Puppet, etc).

Install
=======

    `pip install plantain`

or:

    `sudo python setup.py install`

Setup
=====

`plantain` expects each template to consist of three files: an HTML file
(.html) for the HTML fork of the email to be sent, a text file (.txt)
for the text fork, and a configfile (.cfg) for the metadata aspects of
the template (sending address, Subject: header etc).  eg:

```
account_expired.cfg
account_expired.html
account_expired.txt
```

A sample configfile might read:

```
from_name = YourCompany
from_email = robot@yourcompany.com
subject = Account Expiration
```
The keys in the configfile match the keys used by the Mandrill API:

  https://mandrillapp.com/api/docs/

Note that for fields which are lists, such as labels, you must put a
comma after the first item if there's only one item in the list for it
to be recognised as a list (otherwise the list is the list of
characters in the token):

    labels = foo,

Usage
=====

```
$ plantain -h
usage: plantain [-h] -k KEY -t TEMPLATE -a ACTION [-p] [-q] [-v]

Manage and deploy Mandrill templates.

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     Mandrill API key.
  -t TEMPLATE, --template TEMPLATE
                        Template to manipulate.
  -a ACTION, --action ACTION
                        Action to perform: ['addinfo', 'update',
                        'publish', 'delete', 'list', 'time_series']
  -p, --publish         Auto-publish (for add and update).
  -q, --quiet           Suppress normal output.
  -v, --verbose         Output results and operations.
```

Examples
========

Example call to add a new template to Mandrill called "foo_bar":

    $ plantain -k AbbbcdeDeAdBeeFGaFFPA -t foo_bar -a add

Note that this will not "publish" the template.  To do that:

    $ plantain -k AbbbcdeDeAdBeeFGaFFPA -t foo_bar -a publish

Or you can publish at the same time you add or update the template:

    $ plantain -k AbbbcdeDeAdBeeFGaFFPA -t foo_bar -a update -p
