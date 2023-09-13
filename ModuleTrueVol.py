import pandas as pd
import matplotlib.pyplot as plt

def TrueVol(pd):
  df=pd
  opp=df['Open']
  clo=df['Close']
  voo=df['Volume']
  hig=df['High']
  llo=df['Low']
  upl=[]
  dol=[]
  bll=[]
  upc=0.0
  dlc=0.0
  blc=0.0
  lp=0.0
  for i in range(len(opp)):
    if(lp==0.0):
      lp=opp[i]
    if(opp[i]<clo[i]):
      if(clo[i] >= opp[i] + ((hig[i] - opp[i])/3) and clo[i]>=lp):
        upc+=(voo[i]/1000)
      else:
        if(clo[i] < opp[i] + ((hig[i] - opp[i])/4)):
          dlc+=(voo[i]/1000)
    else:
      if(clo[i] <= opp[i]-((opp[i]-llo[i])/4) and clo[i]<=lp):
        dlc+=(voo[i]/1000)
    upl.append(upc)
    dol.append(dlc)
    blc+=voo[i]/1000
    bll.append(blc/2)
    lp=clo[i]
  ema10=clo.ewm(span=13).mean()
  ema30=clo.ewm(span=35).mean()

  e10=ema10.iloc[-1]
  e30=ema30.iloc[-1]
  score=(e10-e30)+((upc-dlc)/1000)
  print("score:"+ str(int(score)))

  plt.subplot(311)
  plt.title('Price')
  plt.plot(ema10)
  plt.plot(ema30)
  plt.plot(clo)
  plt.grid()

  plt.subplot(312)
  plt.title('Vol')
  plt.plot(voo)
  plt.grid()

  plt.subplot(313)
  plt.plot(upl, label='Buy')
  plt.plot(dol, label='Sell')
  plt.title('TrueVolume')
  plt.grid()
  plt.legend()

  plt.show()
