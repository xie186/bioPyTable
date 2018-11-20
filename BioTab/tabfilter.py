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
        #print(dict_fil)
        rec_total, rec_output = 0, 0 
        with open(options.tab, 'r') as tab, open(options.output, 'w') as output: 
            if options.header is True:
                header = next(tab)
                output.write(header)
            for line in tab:
                rec_total = rec_total + 1
                line = line.rstrip("\n")
                ele = line.split("\t")
                col_index = options.target_column -1
                if ele[col_index] in dict_fil:
                    rec_output = rec_output + 1 
                    output.write(line + "\n")
                    
        print("There are {total} lines. {output} was ouputted.".format(
                total = rec_total, output = rec_output
              ))
       
