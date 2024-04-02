
class StrandsDNA:
    all_strands = []

    def add_strands(self, strands):
        self.all_strands += strands.split()

    def get_max_strands(self):
        max_strands = [strand for strand in self.all_strands
                       if len(strand) == len(max(self.all_strands))]

        return ' '.join(sorted(list(set(max_strands))))

dna = StrandsDNA()
dna.add_strands('qwe rrff sgfds gfd f gfdg dfg hgfds nyttd nyttd')
print(dna.get_max_strands())
