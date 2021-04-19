#! /usr/local/bin/python3

import os
import sys
from io import BytesIO, StringIO
from unittest.mock import patch
from unittest import TestCase, main
import json
from bedrock_cgi.service_base import ServiceBase, REQUEST_METHOD, REQUEST_METHOD_POST, REQUEST_METHOD_OPTIONS
from bedrock_cgi.cgi_request import CONTENT_LENGTH, CONTENT_TYPE
from bedrock_cgi.cgi_response import HEADER_CONTENT_TYPE
from bedrock_cgi.constant import true, false, MIME_TYPE_JSON, CHARSET, CHARSET_UTF8

def handleOk (event):
    event.ok ({ "OK": "OK" })

class TestStdIO:
    def __init__(self, string = None):
        if (string == None):
            self.buffer = BytesIO ()
        else:
            self.buffer = BytesIO (string)

    def getValue (self, encoding = CHARSET_UTF8):
        return self.buffer.getvalue()

class Test (TestCase):
    def testBedrockCgi (self):
        os.environ[REQUEST_METHOD] = REQUEST_METHOD_POST
        os.environ[CONTENT_TYPE] = "{}; {}={}".format (MIME_TYPE_JSON, CHARSET, CHARSET_UTF8)
        requestString = json.dumps({ "event": "ok" }, ensure_ascii=false).encode(CHARSET_UTF8)
        os.environ[CONTENT_LENGTH] = "{}".format (len (requestString))
        with patch ("sys.stdin", new = TestStdIO(requestString)), patch("sys.stdout", new=TestStdIO()) as stdOut:
            ServiceBase.respond ()

            response = stdOut.getValue(CHARSET_UTF8)
            # need to read off the header lines first...
            #response = json.loads (response)
            #self.assertEqual()
            #self.assertEqual(stdOut.getvalue().strip(), expected_out)

if __name__ == '__main__':
    main()

#from bedrock_cgi.service_base import ServiceBase

#ServiceBase.respond()

