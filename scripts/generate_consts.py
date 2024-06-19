import platform
import subprocess
import sys

CONST_FILE = "curl_cffi/const.py"
CURL_VERSION = sys.argv[1]

uname = platform.uname()


print("extract consts from curl.h")
with open(CONST_FILE, "w") as f:
    f.write("# This file is automatically generated, do not modify it directly.\n\n")
    f.write("from enum import IntEnum\n\n\n")
    f.write("class CurlOpt(IntEnum):\n")
    f.write('    """``CULROPT_`` constancs extracted from libcurl,\n')
    f.write('    see: https://curl.se/libcurl/c/curl_easy_setopt.html"""\n\n')
    cmd = rf"""
        echo '#include "{CURL_VERSION}/include/curl/curl.h"' | gcc -E - | grep -i "CURLOPT_.\+ =" | sed "s/  CURLOPT_/    /g" | sed "s/,//g"
    """  # noqa E501
    output = subprocess.check_output(cmd, shell=True)
    f.write(output.decode())
    f.write(
        """
    if locals().get("WRITEDATA"):
        FILE = locals().get("WRITEDATA")
    if locals().get("READDATA"):
        INFILE = locals().get("READDATA")
    if locals().get("HEADERDATA"):
        WRITEHEADER = locals().get("HEADERDATA")\n\n
"""
    )

    f.write("class CurlInfo(IntEnum):\n")
    f.write('    """``CURLINFO_`` constancs extracted from libcurl,\n')
    f.write('    see: https://curl.se/libcurl/c/curl_easy_getinfo.html"""\n\n')
    cmd = rf"""
        echo '#include "{CURL_VERSION}/include/curl/curl.h"' | gcc -E - | grep -i "CURLINFO_.\+ =" | sed "s/  CURLINFO_/    /g" | sed "s/,//g"
    """  # noqa E501
    output = subprocess.check_output(cmd, shell=True)
    f.write(output.decode())
    f.write(
        """
    if locals().get("RESPONSE_CODE"):
        HTTP_CODE = locals().get("RESPONSE_CODE")\n\n
"""
    )

    f.write("class CurlMOpt(IntEnum):\n")
    f.write('    """``CURLMOPT_`` constancs extracted from libcurl,\n')
    f.write('    see: https://curl.se/libcurl/c/curl_multi_setopt.html"""\n\n')
    cmd = rf"""
        echo '#include "{CURL_VERSION}/include/curl/curl.h"' | gcc -E - | grep -i "CURLMOPT_.\+ =" | sed "s/  CURLMOPT_/    /g" | sed "s/,//g"
    """  # noqa E501
    output = subprocess.check_output(cmd, shell=True)
    f.write(output.decode())
    f.write("\n\n")

    f.write("class CurlECode(IntEnum):\n")
    f.write('    """``CURLECODE_`` constancs extracted from libcurl,\n')
    f.write('    see: https://curl.se/libcurl/c/libcurl-errors.html"""\n\n')
    cmd = rf"""
        echo '#include "{CURL_VERSION}/include/curl/curl.h"' | gcc -E - | grep -i CURLE_ | sed "s/[, ][=0]*//g" | sed "s/CURLE_/    /g" | awk '{{print $0 " = " NR-1}}'
    """  # noqa E501
    output = subprocess.check_output(cmd, shell=True)
    f.write(output.decode())
    f.write("\n\n")

    f.write("class CurlHttpVersion(IntEnum):\n")
    f.write('    """``CURL_HTTP_VERSION`` constants extracted from libcurl, see comments for details."""\n\n')
    f.write("    NONE = 0\n")
    f.write("    V1_0 = 1  # please use HTTP 1.0 in the request */\n")
    f.write("    V1_1 = 2  # please use HTTP 1.1 in the request */\n")
    f.write("    V2_0 = 3  # please use HTTP 2 in the request */\n")
    f.write("    V2TLS = 4  # use version 2 for HTTPS, version 1.1 for HTTP */\n")
    f.write("    V2_PRIOR_KNOWLEDGE = 5  # please use HTTP 2 without HTTP/1.1 Upgrade */\n")
    f.write("    V3 = 30  # Makes use of explicit HTTP/3 without fallback.\n")
    f.write("\n\n")

    f.write("class CurlWsFlag(IntEnum):\n")
    f.write('    """``CURL_WS_FLAG`` constants extracted from libcurl, see comments for details."""\n\n')
    f.write("    TEXT = 1 << 0\n")
    f.write("    BINARY = 1 << 1\n")
    f.write("    CONT = 1 << 2\n")
    f.write("    CLOSE = 1 << 3\n")
    f.write("    PING = 1 << 4\n")
    f.write("    OFFSET = 1 << 5\n")
