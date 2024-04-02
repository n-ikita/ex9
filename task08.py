class MorseMsg:
    eng_code = {value: key for key, value in
        {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..'}.items()}
    ru_code = {value.replace(' ', ''): key.upper() for key, value in
                  {'а': '.- ', 'б': '-... ', 'в': '.-- ', 'г': '--. ', 'д': '-.. ', 'е': '. ', 'ж': '...- ',
                  'з': '--.. ', 'и': '.. ', 'й': '.--- ', 'к': '-.- ', 'л': '.-.. ', 'м': '-- ', 'н': '-. ',
                  'о': '--- ', 'п': '.--. ', 'р': '.-. ', 'с': '... ', 'т': '- ', 'у': '..- ', 'ф': '..-. ',
                  'х': '.... ', 'ц': '-.-. ', 'ч': '---. ', 'ш': '---- ', 'щ': '--.- ', 'ъ': '.--.-. ',
                  'ь': '-..- ', 'э': '..-.. ', 'ю': '..-- ', 'я': '.-.- '}.items()}

    def __init__(self, morse_str):
        self.morse_str = morse_str

    def eng_decode(self):
        return ''.join(self.eng_code[letter] for letter in self.morse_str.split())

    def ru_decode(self):
        return ''.join(self.eng_code[letter] for letter in self.morse_str.split())

    def get_vowels(self, lang):
        if lang == 'eng':
            return list(self.eng_code[letter] for letter in self.morse_str.split()
                        if self.eng_code[letter] in ['A', 'E', 'I', 'U', 'O'])
        else:
            return list(self.ru_code[letter] for letter in self.morse_str.split()
                        if self.ru_code[letter] in ['Ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'И', 'Ю'])

    def get_consonants(self, lang):
        if lang == 'eng':
            return list(self.eng_code[letter] for letter in self.morse_str.split()
                        if self.eng_code[letter] not in ['A', 'E', 'I', 'U', 'O'])
        else:
            return list(self.ru_code[letter] for letter in self.morse_str.split()
                        if self.ru_code[letter] not in ['Ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'И', 'Ю'])


morse = MorseMsg('... --- ...')
print(morse.eng_decode())
print(morse.get_vowels('eng'))
print(morse.get_consonants('eng'))
