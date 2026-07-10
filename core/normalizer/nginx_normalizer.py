import re

sample = '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'

class NginxNormalizer():

    def __init__(self) -> None:

        IP = r"(?P<ip>\d+\.\d+\.\d+\.\d+)"
        DATE = r"(?P<date>[^]]+)"
        METHODE = r"(?P<methode>GET|POST|PUT|DELETE|HEAD|OPTIONS)"
        PATH = r"(?P<path>\S+)"
        PROTOCOLE = r"(?P<protocole>[^\"]+)"
        STATUS = r"(?P<status>\d+)"
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
            print(match.groupdict())

        return ({})



normalizer = NginxNormalizer()
log = normalizer.normalize_log(sample)

print(log)
