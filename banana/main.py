#! /usr/bin/env python

import argparse, logging, mandrill
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

  def cmd_add ():
    return client.templates.add (
      name = self.conf["name"],
      from_email = self.conf["from_email"],
      from_name = self.conf["from_name"],
      subject = self.conf["subject"],
      code = self.templ_html,
      text = self.templ_txt,
      publish = self.args.publish,
      labels = self.conf.get ("labels", []),
    )

  def cmd_info ():
    rc = client.templates.info (name = self.conf["name"])

  def cmd_update ():
    return client.templates.update (
      name = self.conf["name"],
      from_email = self.conf["from_email"],
      from_name = self.conf["from_name"],
      subject = self.conf["subject"],
      code = self.templ_html,
      text = self.templ_txt,
      publish = self.args.publish,
      labels = self.conf.get ("labels", []),
    )

  def cmd_publish ():
    return client.templates.publish (
      name = self.conf["name"]
    )

  def cmd_delete ():
    return client.templates.delete (
      name = self.conf["name"]
    )

  def cmd_list ():
    return client.templates.list (
      list = self.conf["name"]
    )

  def cmd_time_series ():
    return client.templates.publish (
      name = self.conf["name"]
    )

  def get_context (self):
    self.templ_html = (path (self.args.template) + ".html").text ()
    self.templ_text = (path (self.args.template) + ".txt").text ()
    self.conf = ConfigObj ((path (self.args.template) + ".cfg".text ()))

  def run (self):
    try:
      self.get_context ()
    except Exception as e:
      LOG.error ("Problem processing files for template: %s  action: %s",
                 self.args.template, self.args.action)
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
  parser.add_argument ("-k", "--key", metavar = "KEY", dest = "key",
                       help = "Mandrill API key.")
  parser.add_argument ("-t", "--template", metavar = "template",
                       dest = "template", required = True,
                       help = "Template to manipulate.")
  parser.add_argument ("-a", "--action", metavar = "ACTION",
                       dest = "act", required = True,
                       help = "Action to perform")
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
