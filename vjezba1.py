class Razlomak(object):

    def __init__(self,brojnik,nazivnik):
        self._brojnik = int(brojnik)
        self._nazivnik = int(nazivnik)

        #Getters
        @property
        def brojnik(self):
            return self._brojnik

        @property
        def nazivnik(self):
            return self.nazivnik
        #-------------------------

        #Setters
        @brojnik.setter
        def brojnik(self,brojnikVrijednost):
            self._brojnik=brojnikVrijednost


        @nazivnik.setter
        def nazivnik(self,nazivnikVrijednost):
            self._nazivnik=nazivnikVrijednost

        #--------------------------

        #Metoda za skraćivanje razlomaka ako je moguće
            @property
            def skrati(self):
                najmanjiDjeljitelj=None

                if(self.brojnik <= self.nazivnik):
                    manjiBroj = self.brojnik

                else:
                    manjiBroj=self.nazivnik

                for djelitelj in range(2,int(manjiBroj +1)):
                    if(self.brojnik % djelitelj == 0 and self.nazivnik %  djelitelj == 0):
                        najmanjiDjelitelj = djelitelj

                    if(najmanjiDjelitelj == None):
                        print("Razlomak se ne može skratiti.")

                    else:
                        self.nazivnik //= najmanjiDjelitelj
                        self.brojnik //= najmanjiDjelitelj
                        print("Razlomak se može skratiti sa brojem",najmanjiDjelitelj,"te razlomak sada izgleda:",repr(self))


                def __repr__(self):
                    return "Razlomak(" + repr(self.brojnik)+","+ repr(self.nazivnik)+")"

            #------------------------------------------


            #Vježba 1.2-Razlomak

                def __str__(self):
                    return str(self.brojnik) + "," + str(self.nazivnik)

            #__repr__metoda je definirana ranije

                def __eq_(self,other):
                    return(self.brojnik / self.nazivnik) == (other.brojnik / other.nazivnik)

                def __ge__(self,other):
                    return(self.brojnik / self.nazivnik) >= (other.brojnik / other.nazivnik)
                def __lt__(self,other):
                    return(self.brojnik / self.nazivnik) < (other.brojnik / other.nazivnik)


            #----------------------------------------

            #Vježba 1.3-Razlomak
                def __add__(self,other)
                brojnik=(self.brojnik * other.nazivnik) + (other.brojnik * self.nazivnik)
                nazivnik=self.nazivnik * other.nazivnik

                return repr(Razlomak(brojnik,nazivnik))

                def __sub__(self,other):
                brojnik=(self.brojnik * other.nazivnik) - (other.brojnik * self.nazivnik)
                nazivnik=self.nazivnik * other.nazivnik

                return repr(Razlomak(brojnik,nazivnik))

                def __mul__(self,other):
                brojnik=self.brojnik * other.nazivnik
                nazivnik=self.nazivnik * other.nazivnik

                return repr(Razlomak(brojnik,nazivnik))

                def __truediv__(self,other):
                    
                brojnik=self.brojnik / other.nazivnik
                nazivnik=self.nazivnik / other.nazivnik

                return repr(Razlomak(brojnik,nazivnik))
                    
                

            
               

 



        
