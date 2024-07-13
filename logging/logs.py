import logging

#Levels:
#DEBUG enables all three
#INFO enables info and error logs
#ERROR only enables error logs
def logs():
    logging.debug("debug info")
    logging.info("just some info")
    logging.error("an error occured")

def main() -> None:
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)
    logs()

if __name__ == "__main__":
    main()