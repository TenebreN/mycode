#we will import this code to usopen later

from netmiko import ConnectHandler

def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):
        #create a connection to the switch
        #pass the location of a config file
        try: 
            #open the config file
            config_file=open(config, "r")
            #netmiko needs content of our config file split into lines
            #split into lines
            config_lines= config_file.read().splitlines()
            
            #this is a LIST, each line is one element

            open_connection= ConnectHandler(device_type=devtype,
                            ip=dev_ip,
                            username=dev_un,
                            password=dev_pw)
            open_connection.enable()

            open_connection.send_config_set(config_lines)
            
            open_connection.send_command_expect('write memory')

            open_connection.disconnect()

            return True
        except:
            return False
