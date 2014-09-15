#! /usr/bin/env python

import argparse, logging, mandrill, sys
from configobj import ConfigObj
from path import path

logging.basicConfig (level = logging.INFO)
LOG = logging.getLogger (__name__)

class BananaCmd (object):
  def __init__ (self, args):
    self.args = args
    self.client = mandrill.Mandrill (self.args.key)
    self.templ_html = None
    self.templ_text = None

  def cmd_add (self):
    return self.client.templates.add (
      name = self.args.template,
      from_email = self.conf["from_email"],
      from_name = self.conf["from_name"],
      subject = self.conf["subject"],
      code = self.templ_html,
      text = self.templ_text,
      publish = self.args.publish,
      labels = self.conf.get ("labels", []),
    )

  def cmd_info (self):
    rc = self.client.templates.info (name = self.args.template)

  def cmd_update (self):
    return self.client.templates.update (
      name = self.args.template,
      from_email = self.conf["from_email"],
      from_name = self.conf["from_name"],
      subject = self.conf["subject"],
      code = self.templ_html,
      text = self.templ_text,
      publish = self.args.publish,
      labels = self.conf.get ("labels", []),
    )

  def cmd_publish (self):
    return self.client.templates.publish (
      name = self.args.template
    )

  def cmd_delete (self):
    return self.client.templates.delete (
      name = self.args.template
    )

  def cmd_list (self):
    return self.client.templates.list (
      list = self.args.template
    )

  def cmd_time_series (self):
    return self.client.templates.publish (
      name = self.args.template
    )

  def get_context (self):
    self.templ_html = (path (self.args.template) + ".html").text ()
    self.templ_text = (path (self.args.template) + ".txt").text ()
    self.conf = ConfigObj ((path (self.args.template) + ".cfg").lines ())

  def run (self):
    try:
      self.get_context ()
    except Exception as e:
      LOG.error (
        "Problem processing files for template: %s  action: %s -- %s",
        self.args.template, self.args.action, e)
      sys.exit (2)
    act = getattr (self, "cmd_%s" % self.args.action, None)
    if act:
      try:
        rc = act ()
        LOG.info ("%s RC: %s", self.args.action, rc)
        if not self.args.quiet:
          print rc
      except mandrill.Error, e:
       LOG.error ("Mandrill: %s - %s", e.__class__, e)
       raise
    else:
      LOG.error ("No implementation for: %s", seklf.args.action)
      sys.exit (1)

def parse_args ():
  parser = argparse.ArgumentParser (
      description = "Manage and deploy Mandrill templates.")
  actions = ["add" "info", "update", "publish", "delete",
             "list", "time_series",]
  parser.add_argument ("-k", "--key", metavar = "KEY", dest = "key",
                       required = True, help = "Mandrill API key.")
  parser.add_argument ("-t", "--template", metavar = "TEMPLATE",
                       dest = "template", required = True,
                       help = "Template to manipulate.")
  parser.add_argument ("-a", "--action", dest = "action",
                       metavar = "ACTION", required = True,
                       help = "Action to perform: %s" % actions)
  parser.add_argument ("-p", "--publish", action = "store_true",
                       help = "Auto-publish (for add and update).")
  parser.add_argument ("-q", "--quiet", action = "store_true",
                       help = "Suppress normal output.")
  parser.add_argument ("-v", "--verbose", action = "store_true",
                       help = "Output results and operations.")
  args = parser.parse_args ()
  return args

def main ():
  args = parse_args ()
  BananaCmd (args).run ()

if __name__ ==  "__main__":
  main ()
