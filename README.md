# Gamma Exposure Index (GEX) in Python w/ TDAmeritrade  
This script calculates the total [GEX](https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf) for a given ticker.  It utilizes [tda-api](https://github.com/alexgolec/tda-api) to pull option chains from TDAmeritrade.  
  
Interpreting the GEX (_quoted from the [GEX paper](https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf)_): "a GEX figure that is positive implies that option market-makers will hedge their positions in a fashion that stikes volatility (buying into lows, selling into highs). A GEX figure that is negative implies the opposite (selling into lows, buying into highs), thus magnifying market volatility."  
  
### Formulas:  
_For a given strike:_   

_Calls:_    
GEX = Г · OI · 100  
  
_Puts:_    
GEX = Г · OI · -100  
  
where Г is gamma, OI is open interest, and 100 is for the contract to shares adjustment  
  
To calculate total GEX for a given underlying we simply take the dot product of the series of Г and the series of OI for both calls and puts, multiply by 100 and -100 respectively, and then take the sum of the two.