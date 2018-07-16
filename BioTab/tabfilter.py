# -*- coding: utf-8 -*-

class tabfilter:
    def __init__ (self):
        pass

    def output_filter(self, options):
        dict_fil = {}
        with open(options.tabfil, 'r') as tabfil:
            for line in tabfil:
                line = line.rstrip("\n")
                ele = line.split("\t")
                col_index = options.column - 1
                if not line.startswith("#"):
                    dict_fil[ele[col_index]] = 1
        print(dict_fil)
        with open(options.tab, 'r') as tab, open(options.output, 'w') as output: 
            header = next(tab)
            output.write(header)
            for line in tab:
                line = line.rstrip("\n")
                ele = line.split("\t")
                col_index = options.target_column -1
                if ele[col_index] in dict_fil:
                    output.write(line + "\n")
                    

             
