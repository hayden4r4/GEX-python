from tda.client import Client
import TDA_init
from TDformatter import TDformatter as tdf
from prettyprinter import cpprint as pprint
import asyncio

c = TDA_init.init(asyncio=True)

symbol: str = '$SPX.X'

async def get_chains():
    chains_resp = await c.get_option_chain(
        symbol = symbol,
        contract_type = Client.Options.ContractType.ALL,
        strike_range = Client.Options.StrikeRange.ALL,
    )
    return chains_resp

chains_resp = asyncio.get_event_loop().run_until_complete(get_chains())


calls, puts = tdf.ChainFormatter(chains_resp).to_df()

gex_calls: float = calls['gamma'].dot(calls['openInterest']) * 100

gex_puts: float = puts['gamma'].dot(puts['openInterest']) * -100

total_gex: float = gex_calls + gex_puts

print(total_gex)
