import re

class NginxNormalizer():

    def __init__(self) -> None:

        IP = r"(?P<source_ip>\d+\.\d+\.\d+\.\d+)"
        DATE = r"(?P<timestamp>[^]]+)"
        METHODE = r"(?P<methode>GET|POST|PUT|DELETE|HEAD|OPTIONS)"
        PATH = r"(?P<path>\S+)"
        PROTOCOLE = r"(?P<protocole>[^\"]+)"
        STATUS = r"(?P<status_code>\d+)"
        SIZE = r"(?P<size>\d+)"

        self.regex = re.compile(rf"""
            {IP}
            \s+-\s+-\s+\[
            {DATE}
            \]\s+"
            {METHODE}
            \s+
            {PATH}
            \s+
            {PROTOCOLE}
            "\s+
            {STATUS}
            \s+
            {SIZE}
        """, re.VERBOSE)
    
    def normalize_log(self, log : str) -> dict:
        
        match = re.search(self.regex, log)
        if match:
            return match.groupdict()
        return ({})