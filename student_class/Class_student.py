class Ensan:

    def __init__(self, esm, sen, ghad, vazn, iq, jensiat):
        self.esm = esm
        self.sen = sen
        self.ghad = ghad  # قد به متر (e:1.75)
        self.vazn = vazn  # وزن به  کیلو گرم 
        self.iq = iq
        self.jensiat = jensiat
        
    def moarefi_kardan(self):
     
     # این متد شخص رو معرفی میکند
     
        print(f"Salam, esm-e man {self.esm} hast. Man {self.sen} salame.")

    def mohasebe_bmi(self):
        
        # محاسبه شاخص توده بدنی
        
        # فرمولvazn / (ghad^2)
        bmi = self.vazn / (self.ghad ** 2)
        print(f"BMI-ye {self.esm} : {bmi:.2f}")
        return bmi

    def afzayesh_sen(self):
        
        # در صورتی که تولدش باشه سن فرد رو ۱ واحد افزایش میدهد.
        
        self.sen += 1
        print(f"Tavalodet mobarak {self.esm} To hala {self.sen} sale shodi.")


class Daneshjoo(Ensan):

    def __init__(self, esm, sen, ghad, vazn, iq, jensiat, shomare_daneshjooi, code_meli, reshteh, moadel, daneshgah):
        
        super().__init__(esm, sen, ghad, vazn, iq, jensiat)
        
        self.daneshgah = daneshgah
        self.shomare_daneshjooi = shomare_daneshjooi
        self.code_meli = code_meli
        self.reshteh = reshteh
        self.moadel = moadel
        self.doroos_entekhab_shode = [ ]  # لیست دروس
        
    def entekhab_vahed(self, dars):
        
        # این متد برای انتخاب واحد درس استفاده میشود.
        
        self.doroos_entekhab_shode.append(dars)
        print(f"{self.esm} dars-e '{dars}' ro ba movafaghiat entekhab kard.")

    def reserve_ghaza(self, rooz):
        
        #برای رزرو غذا در سامانه
        
        print(f"Ghaza baraye {self.esm} dar rooz-e '{rooz}' reserve shod.")

    def namayesh_etelaat_daneshjoo(self):
        
        # اطلاعات کامل دانشجو را نشان می دهد
        
        print("\n--- Etelaat-e Daneshjoo ---")
        self.moarefi_kardan() 
        print(f"Daneshgah {self.Daneshgah}")
        print(f"Reshteh: {self.reshteh}")
        print(f"Shomare Daneshjooi: {self.shomare_daneshjooi}")
        print(f"Code Meli: {self.code_meli}")
        print(f"Moadel: {self.moadel}")
        print(f"Doroos-e Entekhabi: {', '.join(self.doroos_entekhab_shode)}")
        print("--------------------------\n")

#ساختن یک شی در کلاس انسان 

Amir = Ensan(esm="Amir", sen=23, ghad=1.78, vazn=55, iq=140, jensiat="Mard")
Amir.moarefi_kardan()
Amir.mohasebe_bmi()
Amir.afzayesh_sen()

print("--------------------------\n")

# ساختن یک آبجکت از کلاس دانشجو

amir = Daneshjoo(
    shomare_daneshjooi="01121030709003",
    code_meli="5560675431",
    reshteh="Mohandesi control"
    moadel=17
    daneshgah= "Mali Mahart"
)

amir.entekhab_vahed("Brname navisi pishrafte")
amir.entekhab_vahed("Azmayesh gah amalgar")
amir.reserve_ghaza("Shanbe")
amir.namayesh_etelaat_daneshjoo()
amir.afzayesh_sen()
