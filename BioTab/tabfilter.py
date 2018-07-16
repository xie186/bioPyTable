# -*- coding: utf-8 -*-

class tab2xlsx:
    def __init__ (self):
        pass

    def output_filter(self, options):
        dict_fil = {}
        with open(options.tabfilter, 'r') as tabfil:
            for line in tabfil:
                line = line.rstrip("\n")
                ele = line.split("\t")
                col_index = options.column
                if not line.startswith("#")
                    dict_fil[ele[col_index]] ++

        with open(options.tab, 'r') as tab, open(options.output, 'w') as output: 
            header = next(tab)
            output.write(header)
            for line in tab:
                line = line.rstrip("\n")
                ele = line.split("\t")
                col_index = options.target_column
                if ele[col_index] in dict_fil:
                    output.write(line + "\n")
                    

             
