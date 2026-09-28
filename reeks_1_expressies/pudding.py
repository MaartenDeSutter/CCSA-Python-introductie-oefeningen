import math
aantalGekochteStuks = int(input())
prijsPerStuk = float(input())
aantalBenodigdeBarcodes = int(input())
aantalMijlenPerCoupon = int(input())
gespendeerdBedrag = aantalGekochteStuks * prijsPerStuk
aantalMijl = aantalMijlenPerCoupon *  math.floor(aantalGekochteStuks / aantalBenodigdeBarcodes)
print(f"Phillips spendeerde ${gespendeerdBedrag} voor {aantalMijl} frequent flyer mijlen.")