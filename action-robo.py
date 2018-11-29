#!/usr/bin/env python2
# -*-: coding utf-8 -*-

import ConfigParser
from robot import Robot
from hermes_python.hermes import Hermes
import io
import Queue

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section: {option_name : option for option_name, option in self.items(section)} for section in self.sections()}

def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()

class Skill:
    def __init__(self):
        #config = read_configuration_file("config.ini")
        #extra = config["global"].get("extra", False)
        self.robo = Robot()


def callback(hermes, intent_message):
    print "snips callback left"
    hermes.skill.robo.left()

def robo_right(hermes, intent_message):
    print "snips right"
    hermes.skill.robo.right()

def robo_up(hermes, intent_message):
    print "snips face up"
    hermes.skill.robo.up()

def robo_down(hermes, intent_message):
    print "snips face down"
    hermes.skill.robo.down()

def robo_fine(hermes, intent_message):
    print "Snips how are u"
    from datetime import datetime
    result_sentence="I am fine thank you and how are you "
    current_session_id=intentMessage.session_id
    hermes.publish_end_session(current_session_id,result_sentence)
   # hermes.skill.robo.fine()


if __name__ == "__main__":
    skill = Skill()
    with Hermes(MQTT_ADDR) as h:
        h.skill = skill
        h.subscribe_intent("Vishal123:left", callback) \
            .subscribe_intent("Vishal123:right",robo_right)\
            .subscribe_intent("Vishal123:up",robo_up)\
            .subscribe_intent("Vishal123:down",robo_down)\
            .subscribe_intent("Vishal123:fine",robo_fine)\
         .start()
