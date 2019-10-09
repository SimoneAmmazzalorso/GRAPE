import configparser

config = configparser.ConfigParser()

config.read('config.ini')

for sec in config.sections():
    print 'Section:',sec
    for key in config[sec]:
        print key,':',config[sec][key]
    print '\n'

print config.getfloat('cosmology','omegam')

#config.getboolean('Asante', fallback=True)

#print 'Asante :',config['cosmology']['Asante']
