
import logging
import os

def configLogging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    configLogging()
    # Envoi de messages avec différents niveaux de gravité
    logging.debug('Ceci est un message de débogage')
    logging.info('Ceci est un message informatif')
    logging.warning('Ceci est un avertissement')
    logging.error('Ceci est une erreur')
    logging.critical('Ceci est un message critique')


if __name__ == '__main__':
    main()