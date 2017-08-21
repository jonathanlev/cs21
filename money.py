#Jonathan Leventhal
#cs21 assignment5
#program to convert USD to other currencies

 
USD = 1.0
EUR = 0.90798
GBP = 0.82004
INR = 66.8283
AUD = 1.32438
CAD = 1.32773

#main fn
#input validation for positive $ val
def main():
    user_amount = float(input('USD Amount: '))
    while (user_amount <=0):
        print('Error:',user_amount,' is invalid, USD amount must be positive.')
        user_amount = float(input('USD Amount: '))
    convert_and_display(user_amount)
    
#convert_and_display fn
#accepts $ and prints chart of conversions
def convert_and_display(usd_amt):
    print('Converting')
    print('.')
    print('.')
    print('.')
    print('Your USD Amount Converted to Other Currencies:')
    
    eur_amt = usd_amt*EUR
    gbp_amt = usd_amt*GBP
    inr_amt = usd_amt*INR
    aud_amt = usd_amt*AUD
    cad_amt = usd_amt*CAD
    
    fmtd_usd_amt = format(usd_amt,'.2f')
    fmtd_eur_amt = format(eur_amt,'.2f')
    fmtd_gbp_amt = format(gbp_amt,'.2f')
    fmtd_inr_amt = format(inr_amt,'.2f')
    fmtd_aud_amt = format(aud_amt,'.2f')
    fmtd_cad_amt = format(cad_amt,'.2f')
    
    print(format('USD','10'),format('EUR','10'),format('GBP','10'),format('INR','10'),format('AUD','10'),format('CAD','10'))
    print(format(fmtd_usd_amt,'10'),format(fmtd_eur_amt,'10'),format(fmtd_gbp_amt,'10'),format(fmtd_inr_amt,'10'),format(fmtd_aud_amt,'10'),format(fmtd_cad_amt,'10'))
    
        
main()
