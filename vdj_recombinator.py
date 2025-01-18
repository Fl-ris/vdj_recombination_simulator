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

    # 12bp spacer van nonameer naar heptameer <
    rss_regex_12bp_9_7 = "GGTTTTTGT.{12}CACTGTG"
    
    # 12bp spacer van heptameer naar nanomeer >
  # rss_regex_12bp_7_9 = "CACTGTG.{12}GGTTTTTGT"  # Motief volgens powerpoint slide (Geen matches)
    # Volgens dit artikel is er ook een motif: https://pmc.ncbi.nlm.nih.gov/articles/PMC308075/
    rss_regex_12bp_7_9 = "CACAGTG.{12}ACAAAAACC"



    # 23bp spacer nonameer naar heptameer <
    rss_regex_23bp_9_7 = "ACAAAAACC.{23}CACAGTG"
                          
    # 23bp spacer heptameer naar nonameer >
    rss_regex_23bp_7_9 = "CACAGTG.{23}ACAAAAACC"


    rss_regex_12bp_9_7_list = re.findall(rss_regex_12bp_9_7, seq_file)
    rss_regex_12bp_7_9_list = re.findall(rss_regex_12bp_7_9, seq_file)

    # Placeholder:
    rss_regex_23bp_9_7_list = re.findall(rss_regex_23bp_7_9, seq_file)

    rss_regex_23bp_7_9_list = re.findall(rss_regex_23bp_7_9, seq_file)

    print(f"Rss 23bp: {rss_regex_12bp_9_7_list} RSS 12bp: ")


    #char_after_seq(seq_file, rss_regex_12bp_list[1], 20)

    return rss_regex_12bp_9_7_list, rss_regex_12bp_7_9_list, rss_regex_23bp_9_7_list, rss_regex_23bp_7_9_list

def v_finder(seq_file, rss_regex_23bp_9_7_list, rss_regex_23bp_7_9_list):

    # ATG tot de 23bp RSS (V segment)
    start_to_23_rss_motif = "(ATG.*)(CACAGTG.{23}ACAAAAACC)"

    # To-do: opzoeken of het wel ATG tot random 23bp RSS is of tot eerste 23bp RSS.

    rand_rss_regex_23bp_9_7 = random.choice(rss_regex_23bp_9_7_list)
    rand_rss_regex_23bp_7_9 = random.choice(rss_regex_23bp_7_9_list)
    
    # Gebruik re.search i.p.v. findall omdat er anders een korte sequentie bij zit. (Voor onbekende reden)
    start_to_23_rss = re.search(start_to_23_rss_motif, seq_file)

 #   print(rand_rss_regex_12bp_7_9)


    

def d_finder(seq_file,  rss_regex_12bp_9_7_list, rss_regex_12bp_7_9_list):

   # Het d segment hoort tussen 
   # d_motif = rand_rss_regex_12bp_9_7 tot rand_rss_regex_12bp_7_9


    rand_rss_regex_12bp_9_7 = random.choice(rss_regex_12bp_9_7_list)
    rand_rss_regex_12bp_7_9 = random.choice(rss_regex_12bp_7_9_list)

    d_motif = f"{rand_rss_regex_12bp_9_7}(.*){rand_rss_regex_12bp_7_9}"
    start_to_23_rss = re.search(d_motif, seq_file)


    # Try except is nodig omdat hij niet altijd wat kan matchen en in het geval dat het niet kan geeft het een foutmelding....
    try:
        print(f"D-segment: {start_to_23_rss[1]}")
    except:
        print("Random gekozen motief kon niet matchen, volgende keer beter.")



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

    rss_regex_12bp_9_7_list, rss_regex_12bp_7_9_list, rss_regex_23bp_9_7_list, rss_regex_23bp_7_9_list = rss_finder(seq_file)

    v_finder(seq_file, rss_regex_23bp_9_7_list, rss_regex_23bp_7_9_list)

    d_finder(seq_file, rss_regex_12bp_9_7_list, rss_regex_12bp_7_9_list)
  #  read_seq()
