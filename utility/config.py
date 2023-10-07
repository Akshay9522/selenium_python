import configparser
class read_confg:

    def read_config_file(self,section,key):
        config=configparser.ConfigParser()
        config.read("..\\configure\\config.ini")
        return config.get(section,key)
