import os

def read_file_into_list(filename, conversion=None):
    if filename is not None and filename != '':
        self_location = os.path.split(__file__)[0]
        parentdir = os.path.split(self_location)[0]
        filename = os.path.join(parentdir, filename)
        outputlist = []
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                if conversion is not None:
                    tmp = conversion(line)
                    if tmp is not None:
                        outputlist.append(tmp)
                else:
                    outputlist.append(line)
        return outputlist