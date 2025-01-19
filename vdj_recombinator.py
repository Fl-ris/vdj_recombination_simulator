"""
VDJ-recombintie opdracht
Autheur: Floris Menninga
Datum: 18-01-2025

Om te kijken waar mijn regex'en matchen in de volledige sequence heb ik de volgende website gebruikt: https://regexr.com/

Commandline gebruik: python vdj_recombinator.py pad_naar_sequence_file


"""

import re
import sys
import random

heavy_chain = "STKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVGERPAQGGRVSAGSQAQRSCLDASRLCSPSPGQQGRPRLPLHPEASARPTHAQGEG"



def file_reader(seq_file_path):
    with open(seq_file_path, "r") as seq_text:
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

    # Volgens dit artikel is er ook een ander motief: https://pmc.ncbi.nlm.nih.gov/articles/PMC308075/
    rss_regex_12bp_7_9 = "CACAGTG.{12}ACAAAAACC"



    # 23bp spacer nonameer naar heptameer <
  #  rss_regex_23bp_9_7 = "ACAAAAACC.{23}CACAGTG"   # Motief volgens powerpoint slide (Geen matches)
    rss_regex_23bp_9_7 = "GGTTTTTGT.{23}CACTGTG" # Complementaire sequentie hiervan had wel matches. 
    # 23bp spacer heptameer naar nonameer >
    rss_regex_23bp_7_9 = "CACAGTG.{23}ACAAAAACC"


    rss_regex_12bp_9_7_list = re.findall(rss_regex_12bp_9_7, seq_file)
    rss_regex_12bp_7_9_list = re.findall(rss_regex_12bp_7_9, seq_file)

    # Placeholder:
    rss_regex_23bp_9_7_list = re.findall(rss_regex_23bp_9_7, seq_file)
    rss_regex_23bp_7_9_list = re.findall(rss_regex_23bp_7_9, seq_file)

    #print(f"Rss 23bp: {rss_regex_12bp_9_7_list} RSS 12bp: ")


    #char_after_seq(seq_file, rss_regex_12bp_list[1], 20)

    return rss_regex_12bp_9_7_list, rss_regex_12bp_7_9_list, rss_regex_23bp_9_7_list, rss_regex_23bp_7_9_list, rss_regex_23bp_9_7, rss_regex_23bp_7_9, rss_regex_12bp_7_9, rss_regex_12bp_9_7

def v_finder(seq_file, rss_regex_23bp_9_7_list, rss_regex_23bp_7_9_list):
    """
    Zoek het ATG tot eerste 23bp RSS segment en zoek v_segmenten: tussen twee 23bp RSS'en.
    """
    # ATG tot de 23bp RSS (V segment)
    start_to_23_rss_motif = "(ATG.*)(CACAGTG.{23}ACAAAAACC)"

    # To-do: opzoeken of het wel ATG tot random 23bp RSS is of tot eerste 23bp RSS.

    rand_rss_regex_23bp_9_7 = random.choice(rss_regex_23bp_9_7_list)
    rand_rss_regex_23bp_7_9 = random.choice(rss_regex_23bp_7_9_list)
    
   # v_motif = "(CACAGTG.{23}ACAAAAACC).*(CACAGTG.{23}ACAAAAACC)"
    v_motif = f"{rss_regex_23bp_7_9}(.*){rss_regex_23bp_7_9}"
    v_segment = re.search(v_motif, seq_file)
    v_segment = v_segment[1]

    # Gebruik re.search i.p.v. findall omdat er anders een korte sequentie bij zit. (Voor onbekende reden)
    start_to_23_rss = re.search(start_to_23_rss_motif, seq_file)
    
    print(f"V-segment: {v_segment}\n")
    #print(start_to_23_rss[1])
    return start_to_23_rss, v_segment, rand_rss_regex_23bp_9_7, rand_rss_regex_23bp_7_9


    
def d_finder(seq_file,  rss_regex_12bp_9_7_list, rss_regex_12bp_7_9_list):

   # Het d segment hoort tussen rand_rss_regex_12bp_9_7 tot rand_rss_regex_12bp_7_9

    found_valid_motif = False
    tries = 0 # Zodat het niet oneindig door blijft gaan.
    while found_valid_motif == False and tries < 20:

        # Try except is nodig omdat hij niet altijd wat kan matchen en in het geval dat het niet kan geeft het een foutmelding.

        try:
            rand_rss_regex_12bp_9_7 = random.choice(rss_regex_12bp_9_7_list)
            rand_rss_regex_12bp_7_9 = random.choice(rss_regex_12bp_7_9_list)

            d_motif = f"{rand_rss_regex_12bp_9_7}(.*){rand_rss_regex_12bp_7_9}"
            d_segment = re.findall(d_motif, seq_file)
            
            print(f"D-segment: {d_segment[1]}\n")
            d_segment = d_segment[1]
            found_valid_motif = True
            
            return d_segment
        
        except:
            print("Random gekozen motief kon niet matchen, misschien de volgende iteratie wel...")
            tries += 1
    print("Random gekozen motief kon niet matchen na 20 pogingen.")
            
        
def j_finder(seq_file, rss_regex_23bp_9_7):

    j_motif = f"{rss_regex_23bp_9_7}(.*){rss_regex_23bp_9_7}"

    # To-do: verschil tussen findall() en search() opzoeken... 
    j_segment_list = re.findall(j_motif, seq_file)
    j_segment = random.choice(j_segment_list)
    print(f"J-segment: {j_segment}\n")

    return j_segment


def d_j_combiner(d_segment, j_segment):
    """
    Combineer een willekeurig d segment met een willekeurig j segment.
    """
  
    dj_segment = d_segment + j_segment
    print(f"DJ-segment: {dj_segment}\n")

    # knip rss_regex_12bp_7_9 tot rss_regex_23bp_9_7
    cut_motif_dj_segment = f"{rss_regex_12bp_7_9}(.*){rss_regex_23bp_9_7}"
    # Knip het stuk door de sequentie er tussen te vervangen door een lege string ("")
    dj_segment_cut = re.sub(cut_motif_dj_segment, "", dj_segment)

    print(f"Geknipt dj-segment: {dj_segment_cut}\n")
    return dj_segment_cut

def dj_v_combiner(dj_segment_cut, v_segment):

    # knip rss_regex_12bp_7_9 tot rss_regex_23bp_9_7
    cut_motif_v_segment = f"{rss_regex_23bp_7_9}(.*){rss_regex_12bp_9_7}"
    # Knip het stuk door de sequentie er tussen te vervangen door een lege string ("")
    v_segment_cut = re.sub(cut_motif_v_segment, "", v_segment)

    djv_segment = dj_segment_cut + v_segment_cut

    print(f"Geknipt v-segment: {v_segment_cut}\n")
    print(f"djv-segment: {djv_segment}\n")
    return djv_segment



def in_frame_check(sequence_position):
    """
    Stel vast of het verkergen segment wel in frame is ten opzichte van het start codon.
    De modulo wordt gebruikt zodat gekeken kan worden of de sequentie een meervoud van 3 (een codon) er van weg is. 
    Return True als het in frame is en False als dat niet het geval is. 
    """
    return (sequence_position % 3 == 0)


def stop_condon_check():
    pass


def dna_to_protein(dna_seq):
    """
    Deze functie is afkomstig van het internet en zet DNA om naar eiwit.
    """

    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }
    vdj_protein = ''.join([codon_table.get(dna_seq[i:i+3], '') for i in range(0, len(dna_seq), 3)])

    return vdj_protein


def print_resultaat(protein_list, vdj_protein):
    start_p = "M" # Methionine
    
    
    for i in protein_list:
        protein_i = dna_to_protein(i)
        vdj_gene = start_p + protein_i + heavy_chain
        print(f"VDJ eiwit sequentie: {vdj_gene}\n")


    

if __name__ == "__main__":

    protein_list = []
    
    # Krijg 10 verschillende eiwit sequenties:
    for i in range(10):

        seq_file = file_reader(sys.argv[1])

        rss_regex_12bp_9_7_list, rss_regex_12bp_7_9_list, rss_regex_23bp_9_7_list, rss_regex_23bp_7_9_list, rss_regex_23bp_9_7, rss_regex_23bp_7_9, rss_regex_12bp_7_9, rss_regex_12bp_9_7 = rss_finder(seq_file)

        start_to_23_rss, v_segment, rand_rss_regex_23bp_9_7, rand_rss_regex_23bp_7_9 = v_finder(seq_file, rss_regex_23bp_9_7_list, rss_regex_23bp_7_9_list)

        d_segment = d_finder(seq_file, rss_regex_12bp_9_7_list, rss_regex_12bp_7_9_list)

        j_segment = j_finder(seq_file, rss_regex_23bp_9_7)

        dj_segment_cut = d_j_combiner(d_segment, j_segment)

        djv_segment = dj_v_combiner(dj_segment_cut, v_segment)

        vdj_protein = dna_to_protein(djv_segment)

        protein_list.append(vdj_protein)

    print_resultaat(protein_list, vdj_protein)


