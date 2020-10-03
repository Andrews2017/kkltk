stopset_kin = {'aba', 'abo', 'aha', 'aho', 'ari', 'ati', 'aya', 'ayo', 'ba', 'baba', 'babo', 'bari', 'be', 'bo', 'bose',
           'bw', 'bwa', 'bwo', 'by', 'bya', 'byo', 'cy', 'cya', 'cyo', 'hafi', 'ibi', 'ibyo', 'icyo', 'iki',
           'imwe', 'iri', 'iyi', 'iyo', 'izi', 'izo', 'ka', 'ko', 'ku', 'kuri', 'kuva', 'kwa', 'maze', 'mu', 'muri',
           'na', 'naho','nawe', 'ngo', 'ni', 'niba', 'nk', 'nka', 'no', 'nta', 'nuko', 'rero', 'rw', 'rwa', 'rwo', 'ry',
           'rya','ubu', 'ubwo', 'uko', 'undi', 'uri', 'uwo', 'uyu', 'wa', 'wari', 'we', 'wo', 'ya', 'yabo', 'yari', 'ye',
           'yo', 'yose', 'za', 'zo'}

stopset_kir = {'aba','abo','aho','ari','ata','ati','ayo','ba','bari','bo','bose','bw','bwa','bwo','ca','cane','co','de',
               'ico','iryo','ivyo','iyo','izo','ko','ku','kuri','kuva','kw','maze','mu','muri','mw','na','naho','nayo',
               'ngo','ni','nk','no','rero','rw','ry','rya','ubu','uko','uri','uwo','uyu','vy','vya','vyo','wa','wo',
               'ya','yari','yo','yose','za','zo'}

class stopwords():
    def __init__(self):
        super().__init__()

    def words(lang):
        if lang == 'kinyarwanda':
            return stopset_kin
        elif lang == 'kirundi':
            return stopset_kir
        else:
            return "Invalid argument. choose between 'kinyarwanda' and 'kirundi'."

if __name__=="__main__":
    stopset = stopwords.words('kirundi')
    print(stopset)