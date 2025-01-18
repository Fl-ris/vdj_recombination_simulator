"""
VDJ-recombintie opdracht
Autheur: Floris Menninga
Datum: 18-01-2025

Om te kijken waar mijn regex'en matchen in de volledige sequence heb ik de volgende website gebruikt: https://regexr.com/



"""

import re
import random

heavy_chain = "STKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVGERPAQGGRVSAGSQAQRSCLDASRLCSPSPGQQGRPRLPLHPEASARPTHAQGEG"



def file_reader():
    with open("/home/floris/Documenten/Github/vdj_recomb/sequence_file.txt", "r") as seq_text:
        seq_file = seq_text.read()
        return seq_file


def char_after_seq(text_to_split,split, amount):
    """
    Functie om de sequentie te krijgen die achter een bekende sequentie zit. (Om bijvoorbeeld naar de V,D en J segmenten de zoeken aan de hand van RSS segmenten.)
    split: waarachter moet de sequentie gehaald worden.
    amount: hoeveel characters er na.
    """
    #seq_after = text_to_split.split(split)[amount]

    start_index = text_to_split.find(split) + len(split)
    seq_after = text_to_split[start_index:start_index+amount]  
   # print(seq_after)


def rss_finder(seq_file):
    """
    Zoek sequenties die beginnen met "CACAGTG", een 23 nuc
    """

    # 12bp spacer
    rss_regex_12bp = "GGTTTTTGT.{12}CACTGTG"

    # 23bp spacer
    rss_regex_23bp = "CACAGTG.{23}ACAAAAACC"


    rss_regex_12bp_list = re.findall(rss_regex_12bp, seq_file)

    rss_regex_23bp_list = re.findall(rss_regex_23bp, seq_file)

    # print(f"Rss 23bp: {rss_regex_23bp_list} RSS 12bp: {rss_regex_12bp_list}")

    char_after_seq(seq_file, rss_regex_12bp_list[1], 20)

    return rss_regex_12bp_list, rss_regex_23bp_list

def v_finder(rss_regex_12bp_list, rss_regex_23bp_list):

    # ATG tot de 23bp RSS
    start_to_23_rss = "(ATG.*)(CACAGTG.{23}ACAAAAACC)"





    print(start_to_23_rss)


    


    pass

def d_finder(seq):
    pass

def j_finder():
    pass

def in_frame_check():
    pass

def stop_condon_check():
    pass

def print_resultaat():
    pass


if __name__ == "__main__":
    seq_file =  file_reader()
    rss_regex_12bp_list, rss_regex_23bp_list = rss_finder(seq_file)

  #  read_seq()
