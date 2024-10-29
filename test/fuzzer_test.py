import unittest, sys
import file_type_fuzzer_xoth42
# pip3.13 install dist/file_type_fuzzer_xoth42-0.0.1-py3-none-any.whl --break-system-packages


class TestGenerator(unittest.TestCase):
    def makeTestFile(name,data):
        with open(testfile+".txt", "wb") as F:
                F.write(testfile)
    def testGeneratedFileCount(self):
        testData = ["\x01","\x02","\x03"]
        makeTestFile("fileCount",data)
        myGen = MutationGenerator()
        