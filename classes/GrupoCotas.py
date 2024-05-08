class GrupoCotas:
    def __init__(self,
                 codigo : str,
                 cotas_ativas : str,
                 cotas_excluidas : str,
                 lance_fixo : str,
                 lance_seg_fixo : str,
                 lance_livre : str,
                 lance_limitado : str):
        
        self.codigo = codigo
        self.cotas_ativas = self.get_cotas_ativas(cotas_ativas)
        self.cotas_excluida = self.get_cotas_excluidas(cotas_excluidas)
        self.lance_fixo = self.get_lance_fixo(lance_fixo)
        self.lance_seg_fixo = self.get_lance_seg_fixo(lance_seg_fixo)
        self.lance_livre = self.get_lance_livre(lance_livre)
        self.lance_limitado = self.get_lance_limitado(lance_limitado)
           
      
    def get_cotas_ativas(self,str : str):
        cotas_ativas = []
        return cotas_ativas
    
    def get_cotas_excluidas(self,srt : str):
        cotas_excluidas = []
        return cotas_excluidas     
    
    def get_lance_fixo(self,srt : str):
        lance_fixo = []
        return lance_fixo 
    
    def get_lance_seg_fixo(self,srt : str):
        lance_seg_fixo = []
        return lance_seg_fixo 
    
    def get_lance_livre(self,srt : str):
        lance_livre = []
        return lance_livre 
    
    def get_lance_limitado(self,srt : str):
        lance_limitado = []
        return lance_limitado 