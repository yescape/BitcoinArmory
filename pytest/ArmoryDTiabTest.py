'''
Created on Oct 8, 2013

@author: Andy
'''
import sys
sys.path.append('..')
from pytest.Tiab import TiabTest, TOP_TIAB_BLOCK, FIRST_WLT_BALANCE,\
   FIRST_WLT_NAME, SECOND_WLT_NAME, THIRD_WLT_NAME, TIAB_SATOSHI_PORT
from armoryengine.ArmoryUtils import *
from armoryd import AmountToJSON, Armory_Json_Rpc_Server, JSONtoAmount
from armoryengine.BDM import TheBDM
from armoryengine.PyBtcWallet import PyBtcWallet
from armoryengine.Transaction import UnsignedTransaction, PyTx
import unittest

from jasvet import ASv1CS

TX_FILENAME = 'mytxfile'

TEST_WALLET_NAME = 'Test Wallet Name'
TEST_WALLET_DESCRIPTION = 'Test Wallet Description'

TX_ID1_OUTPUT0_VALUE = 63000
TX_ID1_OUTPUT1_VALUE = 139367000

TWO_OF_THREE_LB_NAME = '2fhUSuNL'
TWO_OF_TWO_LB_NAME = 'WZ2pEKAG'

PASSPHRASE1 = 'abcde'
UNLOCK_TIMEOUT = 5
TIAB_DIR = 'tiab'
TEST_TIAB_DIR = os.path.join('test','tiab')
NEED_TIAB_MSG = "This Test must be run with J:/Development_Stuff/bitcoin-testnet-boxV2.7z (Armory jungle disk). Copy to the test directory."

EXPECTED_TIAB_NEXT_ADDR  = 'muEePRR9ShvRm2nqeiJyD8pJRHPuww2ECG'
EXPECTED_UNSPENT_TX1_BAL  = 20.0
EXPECTED_UNSPENT_TX1_CONF = 3
EXPECTED_UNSPENT_TX1_HEX  = '4434b3eab23189af20d56a81a7bc5ac560f42f4097a90f834535cb94a8d5578201000000'
EXPECTED_UNSPENT_TX1_PRI  = 60.0
EXPECTED_UNSPENT_TX5_BAL  = 938.8997
EXPECTED_UNSPENT_TX5_CONF = 8
EXPECTED_UNSPENT_TX5_HEX  = '721507bc7c4cdbd7cf798d362272b2e5941e619f2f300f46ac956933cb42181100000000'
EXPECTED_UNSPENT_TX5_PRI  = 7511.1976
EXPECTED_UNSPENT_TX_TOT   = 964.8997

TIAB_WLT_1_ADDR_1 = 'muxkzd4sitPbMz4BXmkEJKT6ccshxDFsrn'
TIAB_WLT_1_PK_1 = '92vsXfvjpbTj1sN75VSV2M7DWyqoVx5nayp3dE7ZaG9rRVRYU4P'

TIAB_WLT_1_ADDR_2 = 'mtZ2d1jFZ9YNp3Ku5Fb2u8Tfu3RgimBHAD'
TIAB_WLT_1_PK_2 = '934MLhycJEAWL4kMbFt6JRSkNcgEtQXN3ha6Wh8WZyD85cZZZ4N'

TIAB_WLT_1_ADDR_3 = 'mhrpYhQLgYgAvYs1A4E8Z4Dv4ZoZPyLbLS'
TIAB_WLT_1_PK_3 = '91rTQa47dLQhNGDenejW9qxcMTL73GRG347zKfa3qVvzun7ZcNe'
TIAB_WLT_1_PK_UTXO_BAL_3  = 3.0
TIAB_WLT_1_PK_UTXO_HEX_3  = '507b01123e9416eb6de996f64686b7c8290eacd13b9607438a8bab4a78d3afd503000000'

# Has 938.8997 BTC
TIAB_WLT_1_ADDR_8 = 'mikxgMUqkk6Tts1D39Hhx6wKEeQbBH3ons'
TIAB_WLT_1_PK_8 = '92fXG1foeHfn8DYEwTXggCPrFEEY6KpokqoJkp9EhpJw5boc3GY'
TIAB_WLT_1_PK_UTXO_BAL_8  = 938.8997
TIAB_WLT_1_PK_UTXO_HEX_8  = '721507bc7c4cdbd7cf798d362272b2e5941e619f2f300f46ac956933cb42181100000000'

TIAB_WLT_2_ADDR_1 = 'mzkKrXNPU6nfBpZCKLmwueb9MvSFaKPDMD'
TIAB_WLT_2_PK_1 = '91jZJ2BnJbk4B6zpqzJqVfbtaq4RMaPPvP7USr9rtWXusSAYrq7'

TIAB_WLT_2_ADDR_2 = 'n2DLXxVZSNBfzXsAm4HewpsfAGBpgTW6DH'
TIAB_WLT_2_PK_2 = '93LLsm4n19Dwbp6zbnmuvHmMjEJFR23h4xstnDnEBYMWSkXaFMT'

TIAB_WLT_2_ADDR_3 = 'mhbmvVedo4i67maX6pfw9trcBWQQ3yXgkB'
TIAB_WLT_2_PK_3 = '92aUXStPSfHDXydGh9MsBnnyacNzJwgWBC4G8W5BiTFkTJpeHEH'

# Has 28.9 BTC
TIAB_WLT_2_ADDR_4 = 'mk7pAQ7YdmnwWaGFCgwiKiEbaGjyEsSVUE'
TIAB_WLT_2_PK_4 = '92gYPs8i6qvSmc8moBAaWLB7M16kX5MBpbGoUygUmQTdrxkNnwR'

TIAB_WLT_3_ADDR_1 = 'mnHywMYRuMyYeamyGhUPJLFSsoWbNAnsNz'
TIAB_WLT_3_PK_1 = '9295sDHkX1xDMzSxit3Bvi8GdLUQq1JFktBQFB8Ca45aLaw8neN'

TIAB_WLT_3_ADDR_2 = 'mpXd2u8fPVYdL1Nf9bZ4EFnqhkNyghGLxL'
TIAB_WLT_3_PK_2 = '92Mic29J44mKLn4qKXm31mMv45BtEnywBnJh36jn1Rk2RT9PTsK'

# has 18.90 BTC
TIAB_WLT_3_ADDR_3 = 'mmfN9oj2wtMTCACKJz7fUcDeAczz4kucvV'
TIAB_WLT_3_PK_3 = '92ymyLuiEUJJz5madzhPtBTa3of46vLXDSuFPNMAA6DMLSeKA8S'

BTC_TO_SEND = 1

TEST_MESSAGE = "All your base are belong to us."

# These tests need to be run in the TiaB
class ArmoryDTiabTest(TiabTest):
   
   def setUp(self):
      self.verifyBlockHeight()
      # Load the primary file from the test net in a box
      self.fileA    = os.path.join(self.tiab.tiabDirectory, 'tiab','armory','armory_%s_.wallet' % FIRST_WLT_NAME)
      self.wlt = PyBtcWallet().readWalletFile(self.fileA, doScanNow=True)
      fileB    = os.path.join(self.tiab.tiabDirectory, 'tiab','armory','armory_%s_.wallet' % SECOND_WLT_NAME)
      wltB = PyBtcWallet().readWalletFile(fileB, doScanNow=True)
      fileC    = os.path.join(self.tiab.tiabDirectory, 'tiab','armory','armory_%s_.wallet' % THIRD_WLT_NAME)
      wltC = PyBtcWallet().readWalletFile(fileC, doScanNow=True)
      self.jsonServer = Armory_Json_Rpc_Server(self.wlt, inWltSet={SECOND_WLT_NAME : wltB, THIRD_WLT_NAME : wltC},
                           armoryHomeDir=os.path.join(self.tiab.tiabDirectory, 'tiab','armory'))
      TheBDM.registerWallet(self.wlt)
      
   def testActiveWallet(self):
      self.jsonServer.jsonrpc_setactivewallet(FIRST_WLT_NAME)
      result = self.jsonServer.jsonrpc_getactivewallet()
      self.assertEqual(result, FIRST_WLT_NAME)
      
      bogusResult = self.jsonServer.jsonrpc_setactivewallet('bogus wallet name')
      self.assertTrue('does not exist' in bogusResult)
      
   # Tests all of the address meta data functions at once
   def testAddressMetaData(self):
      testInput = {TIAB_WLT_1_ADDR_1:
                     {'chain': 5,
                      'index': 2},
                  TIAB_WLT_1_ADDR_2:
                     {'CrazyField': 'what',
                      '1': 1,
                      '2': 2}}
      self.jsonServer.jsonrpc_setaddressmetadata(testInput)
      testOutput1=self.jsonServer.jsonrpc_getaddressmetadata()
      self.assertEqual(testOutput1, testInput)
      self.jsonServer.jsonrpc_clearaddressmetadata()
      testOutput2=self.jsonServer.jsonrpc_getaddressmetadata()
      self.assertEqual(testOutput2, {})
      
   def testListloadedwallets(self):
      result = self.jsonServer.jsonrpc_listloadedwallets()
      self.assertEqual(len(result.keys()), 3)
      self.assertTrue(FIRST_WLT_NAME in result.values())
      self.assertTrue(SECOND_WLT_NAME in result.values())
      self.assertTrue(THIRD_WLT_NAME in result.values())
      
   def getPrivateKey(self, address):
      hash160 = addrStr_to_hash160(address)[1]
      if self.wlt.isLocked:
         self.wlt.unlock(securePassphrase=SecureBinaryData(PASSPHRASE1),
                               tempKeyLifetime=1000000)
      return self.wlt.addrMap[hash160].binPrivKey32_Plain.toBinStr()
   
   # Test Create lockbox and list loaded lockbox at the same time.
   # Also test set and get active lockbox.
   def testLockboxMethods(self):
      self.assertEqual(self.jsonServer.jsonrpc_getactivelockbox(), None)
      addrFromFirstWlt = self.jsonServer.getPKFromWallet(self.wlt, self.wlt.getHighestUsedIndex())
      actualResult1 = self.jsonServer.jsonrpc_createlockbox(2, 3, addrFromFirstWlt, SECOND_WLT_NAME, THIRD_WLT_NAME)
      self.assertTrue(TWO_OF_THREE_LB_NAME in actualResult1)
      listResult1 = self.jsonServer.jsonrpc_listloadedlockboxes()
      self.assertEqual(len(listResult1.keys()), 1)
      self.assertTrue(TWO_OF_THREE_LB_NAME in listResult1.values())
      
      actualResult2 = self.jsonServer.jsonrpc_createlockbox(2, 2, SECOND_WLT_NAME, THIRD_WLT_NAME)
      self.assertTrue(TWO_OF_TWO_LB_NAME in actualResult2)
      listResult2 = self.jsonServer.jsonrpc_listloadedlockboxes()
      self.assertEqual(len(listResult2.keys()), 2)
      self.assertTrue(TWO_OF_TWO_LB_NAME in listResult2.values())
      self.jsonServer.jsonrpc_setactivelockbox(TWO_OF_TWO_LB_NAME)
      self.assertEqual(self.jsonServer.jsonrpc_getactivelockbox(), TWO_OF_TWO_LB_NAME)
      self.jsonServer.jsonrpc_setactivelockbox(TWO_OF_THREE_LB_NAME)
      self.assertEqual(self.jsonServer.jsonrpc_getactivelockbox(), TWO_OF_THREE_LB_NAME)
      
   def  testVerifysignature(self):
      clearSignMessage = ASv1CS(self.getPrivateKey(TIAB_WLT_1_ADDR_1), TEST_MESSAGE)
      result = self.jsonServer.jsonrpc_verifysignature(clearSignMessage)
      self.assertEqual(result['message'], TEST_MESSAGE)
      self.assertEqual(result['address'], TIAB_WLT_1_ADDR_1)
      
   def  testReceivedfromsigner(self):      
      clearSignMessage2 = ASv1CS(self.getPrivateKey(TIAB_WLT_1_ADDR_3), TEST_MESSAGE)
      result2 = self.jsonServer.jsonrpc_receivedfromsigner(clearSignMessage2)
      self.assertEqual(result2['message'], TEST_MESSAGE)
      self.assertEqual(result2['amount'], 0)
   
   def  testReceivedfromaddress(self):
      result = self.jsonServer.jsonrpc_receivedfromaddress(TIAB_WLT_3_ADDR_3)
      self.assertEqual(result, 0)
      result = self.jsonServer.jsonrpc_receivedfromaddress(TIAB_WLT_1_ADDR_3)
      self.assertEqual(result, 0)
   
   def testGettransaction(self):
      tx = self.jsonServer.jsonrpc_gettransaction('db0ee46beff3a61f38bfc563f92c11449ed57c3d7d5cd5aafbe0114e5a9ceee4')
      self.assertEqual(tx, {'category': 'send', 'inputs': [{'fromtxid': '04b865ecf5fca3a56f6ce73a571a09a668f4b7aa5a7547a5f51fae08eadcdbb5',
                            'ismine': True, 'fromtxindex': 1, 'value': 1000.0, 'address': 'mtZ2d1jFZ9YNp3Ku5Fb2u8Tfu3RgimBHAD'}],
                            'direction': 'send', 'fee': 0.0001, 'totalinputs': 1000.0, 'outputs':
                             [{'address': 'mpXd2u8fPVYdL1Nf9bZ4EFnqhkNyghGLxL', 'value': 20.0, 'ismine': False},
                              {'address': 'mgLjhTCUtbeLPP9fDkBnG8oztWgJaXZQjn', 'value': 979.9999, 'ismine': True}],
                            'txid': 'db0ee46beff3a61f38bfc563f92c11449ed57c3d7d5cd5aafbe0114e5a9ceee4', 'confirmations': 10,
                            'orderinblock': 1, 'mainbranch': True, 'numtxin': 1, 'time': 3947917907L, 'numtxout': 2,
                            'netdiff': -20.0001, 'infomissing': False})
   
   def testGetblock(self):
      block = self.jsonServer.jsonrpc_getblock('0000000064a1ad1f15981a713a6ef08fd98f69854c781dc7b8789cc5f678e01f')
      # This method is broken in a couple ways.
      # For no just verify that raw transaction is correct
      self.assertEqual(block['rawheader'], '02000000d8778a50d43d3e02c4c20bdd0ed97077a3c4bef3e86ce58975f6f43a00000000d25912cfc67228748494d421512c7a6cc31668fa82b72265261558802a89f4c2e0350153ffff001d10bcc285',)
      
   def testGetinfo(self):
      info = self.jsonServer.jsonrpc_getarmorydinfo()
      self.assertEqual(info['blocks'], TOP_TIAB_BLOCK)
      self.assertEqual(info['bdmstate'], 'BlockchainReady')
      self.assertEqual(info['walletversionstr'], '1.35')
      self.assertEqual(info['difficulty'], 1.0)
      self.assertEqual(info['balance'], FIRST_WLT_BALANCE)
      
   def testListtransactions(self):
      txList = self.jsonServer.jsonrpc_listtransactions(100)
      self.assertTrue(len(txList)>10)
      self.assertEqual(txList[0], {'blockhash': '0000000064a1ad1f15981a713a6ef08fd98f69854c781dc7b8789cc5f678e01f',
                  'blockindex': 1, 'confirmations': 31, 'address': 'mtZ2d1jFZ9YNp3Ku5Fb2u8Tfu3RgimBHAD',
                  'category': 'receive', 'account': '',
                  'txid': '04b865ecf5fca3a56f6ce73a571a09a668f4b7aa5a7547a5f51fae08eadcdbb5',
                  'blocktime': 1392588256, 'amount': 1000.0, 'timereceived': 1392588256, 'time': 1392588256})
            
      
   def testGetledgersimple(self):
      ledger = self.jsonServer.jsonrpc_getledgersimple()
      self.assertTrue(len(ledger)>4)
      amountList = [row['amount'] for row in ledger]
      expectedAmountList = [1000.0, 20.0, 30.0, 0.8, 10.0]
      self.assertEqual(amountList[:5], expectedAmountList)
      
      
   def testGetledger(self):
      ledger = self.jsonServer.jsonrpc_getledger()
      self.assertTrue(len(ledger)>6)
      amountList = [row['amount'] for row in ledger]
      expectedAmountList = [1000.0, 20.0, 30.0, 0.8, 10.0, 6.0, 20.0]
      self.assertEqual(amountList, expectedAmountList)
      self.assertEqual(ledger[0]['direction'], 'receive')
      self.assertEqual(len(ledger[0]['recipme']), 1)
      self.assertEqual(ledger[0]['recipme'][0]['amount'], 1000.0)
      self.assertEqual(len(ledger[0]['recipother']), 1)
      self.assertEqual(ledger[0]['recipother'][0]['amount'], 49.997)
      self.assertEqual(len(ledger[0]['senderme']), 0)
      self.assertEqual(len(ledger[0]['senderother']), 21)
 
      self.assertEqual(ledger[1]['direction'], 'send')
      self.assertEqual(len(ledger[1]['senderother']), 0)
      self.assertEqual(len(ledger[1]['senderme']), 1)
      self.assertEqual(ledger[1]['senderme'][0]['amount'], 1000.0)

   def testSendtoaddress(self):
      # Send 1 BTC
      serializedUnsignedTx = \
         self.jsonServer.jsonrpc_createustxtoaddress(TIAB_WLT_3_ADDR_3, \
                                                     BTC_TO_SEND)
      unsignedTx = UnsignedTransaction().unserializeAscii(serializedUnsignedTx)
      # Should have 2 txouts to TIAB_WLT_3_ADDR_3 and the change
      self.assertEqual(len(unsignedTx.decorTxOuts), 2)
      foundTxOut = False
      for txout in unsignedTx.decorTxOuts:
         if script_to_addrStr(txout.binScript) == TIAB_WLT_3_ADDR_3:
            self.assertEqual(txout.value, JSONtoAmount(BTC_TO_SEND))
            foundTxOut = True
      self.assertTrue(foundTxOut)
      
      # Test two paths through signing method and make sure they are equal
      # Wallets in the TIAB start out unencrypted
      serializedSignedTxUnencrypted = self.jsonServer.jsonrpc_signasciitransaction(serializedUnsignedTx,'')
      self.jsonServer.jsonrpc_encryptwallet(PASSPHRASE1)
      serializedSignedTxEncrypted = self.jsonServer.jsonrpc_signasciitransaction(serializedUnsignedTx,PASSPHRASE1)
      # Other tests expect wallet to be unencrypted
      self.wlt.unlock(securePassphrase=SecureBinaryData(PASSPHRASE1),
                            tempKeyLifetime=1000000)
      self.wlt.changeWalletEncryption()
      signedTxUnencrypted = UnsignedTransaction().unserializeAscii(serializedSignedTxUnencrypted)
      signedTxEncrypted = UnsignedTransaction().unserializeAscii(serializedSignedTxEncrypted)
      # check number of outputs 1 Btc goes to a single output and the other goes to change
      self.assertEqual(len(signedTxUnencrypted.decorTxOuts), 2)
      self.assertEqual(len(signedTxEncrypted.decorTxOuts), 2)
      self.assertEqual(signedTxUnencrypted.asciiID, signedTxEncrypted.asciiID)
      self.assertTrue(JSONtoAmount(BTC_TO_SEND) in
             [signedTxEncrypted.decorTxOuts[0].value,
              signedTxEncrypted.decorTxOuts[1].value])
      self.assertTrue(JSONtoAmount(BTC_TO_SEND) in
             [signedTxUnencrypted.decorTxOuts[0].value,
              signedTxUnencrypted.decorTxOuts[1].value])
      f = open(TX_FILENAME, 'w')
      f.write(signedTxEncrypted.serializeAscii())
      f.close()
      txHexToBroadcast = self.jsonServer.jsonrpc_gethextxtobroadcast(TX_FILENAME)
      finalPyTx = PyTx().unserialize(hex_to_binary(txHexToBroadcast))
      self.assertEqual(len(finalPyTx.outputs), 2)
      self.assertTrue(JSONtoAmount(BTC_TO_SEND) in
             [finalPyTx.outputs[0].value,
              finalPyTx.outputs[1].value])


   def testSendmany(self):
      # Send 1 BTC
      serializedUnsignedTx = \
         self.jsonServer.jsonrpc_createustxformany(':'.join([TIAB_WLT_3_ADDR_2, str(BTC_TO_SEND)]), \
                                                   ':'.join([TIAB_WLT_3_ADDR_3, str(BTC_TO_SEND)]))
      unsignedTx = UnsignedTransaction().unserializeAscii(serializedUnsignedTx)
      # Should have 2 txouts to TIAB_WLT_3_ADDR_3 and the change
      self.assertEqual(len(unsignedTx.decorTxOuts), 3)
      txOutsFound = 0
      for txout in unsignedTx.decorTxOuts:
         if script_to_addrStr(txout.binScript) in [TIAB_WLT_3_ADDR_2, TIAB_WLT_3_ADDR_3]:
            self.assertEqual(txout.value, JSONtoAmount(BTC_TO_SEND))
            txOutsFound += 1
      self.assertEqual(txOutsFound, 2)

   def testListUnspent(self):
      actualResult = self.jsonServer.jsonrpc_listunspent()

      self.assertEqual(len(actualResult), 7)
      self.assertEqual(actualResult['Total Balance'], EXPECTED_UNSPENT_TX_TOT)
      self.assertEqual(actualResult['Total UTXOs'], 5)
      self.assertEqual(actualResult['UTXO 00001']['Balance'], \
                       EXPECTED_UNSPENT_TX1_BAL)
      self.assertEqual(actualResult['UTXO 00001']['Confirmations'], \
                       EXPECTED_UNSPENT_TX1_CONF)
      self.assertEqual(actualResult['UTXO 00001']['Hex'], \
                       EXPECTED_UNSPENT_TX1_HEX)
      self.assertEqual(actualResult['UTXO 00001']['Priority'], \
                       EXPECTED_UNSPENT_TX1_PRI)
      self.assertEqual(actualResult['UTXO 00005']['Balance'], \
                       EXPECTED_UNSPENT_TX5_BAL)
      self.assertEqual(actualResult['UTXO 00005']['Confirmations'], \
                       EXPECTED_UNSPENT_TX5_CONF)
      self.assertEqual(actualResult['UTXO 00005']['Hex'], \
                       EXPECTED_UNSPENT_TX5_HEX)
      self.assertEqual(actualResult['UTXO 00005']['Priority'], \
                       EXPECTED_UNSPENT_TX5_PRI)


   def testListAddrUnspent(self):
      totStr = '%s:%s' % (TIAB_WLT_1_ADDR_3, TIAB_WLT_1_ADDR_8)
      totBal = TIAB_WLT_1_PK_UTXO_BAL_3 + TIAB_WLT_1_PK_UTXO_BAL_8
      actualResult = self.jsonServer.jsonrpc_listaddrunspent(totStr)

      self.assertEqual(len(actualResult), 4)
      self.assertEqual(actualResult[TIAB_WLT_1_ADDR_3]['UTXO 00001']['Balance'], \
                       TIAB_WLT_1_PK_UTXO_BAL_3)
      #self.assertEqual(actualResult[TIAB_WLT_1_ADDR_3]['UTXO 00001']['Confirmations'], \
      #                 EXPECTED_UNSPENT_TX2_CONF)
      self.assertEqual(actualResult[TIAB_WLT_1_ADDR_3]['UTXO 00001']['Hex'], \
                       TIAB_WLT_1_PK_UTXO_HEX_3)
      #self.assertEqual(actualResult[TIAB_WLT_1_ADDR_3]['UTXO 00001']['Priority'], \
      #                 EXPECTED_UNSPENT_TX2_PRI)
      self.assertEqual(actualResult[TIAB_WLT_1_ADDR_8]['UTXO 00001']['Balance'], \
                       TIAB_WLT_1_PK_UTXO_BAL_8)
      #self.assertEqual(actualResult[TIAB_WLT_1_ADDR_8]['UTXO 00001']['Confirmations'], \
      #                 EXPECTED_UNSPENT_TX2_CONF)
      self.assertEqual(actualResult[TIAB_WLT_1_ADDR_8]['UTXO 00001']['Hex'], \
                       TIAB_WLT_1_PK_UTXO_HEX_8)
      #self.assertEqual(actualResult[TIAB_WLT_1_ADDR_8]['UTXO 00001']['Priority'], \
      #                 EXPECTED_UNSPENT_TX2_PRI)

      # NB: Ideally, the TAB asserts would be against addresses with multiple
      # UTXOs. As is, this test case works but could be better.
      self.assertEqual(actualResult[TIAB_WLT_1_ADDR_3]['Total Address Balance'], \
                       TIAB_WLT_1_PK_UTXO_BAL_3)
      self.assertEqual(actualResult[TIAB_WLT_1_ADDR_8]['Total Address Balance'], \
                       TIAB_WLT_1_PK_UTXO_BAL_8)
      self.assertEqual(actualResult['Total UTXOs'], 2)
      self.assertEqual(actualResult['Total UTXO Balance'], totBal)


   def testGetNewAddress(self):
      actualResult = self.jsonServer.jsonrpc_getnewaddress()
      self.assertEqual(actualResult, EXPECTED_TIAB_NEXT_ADDR)


   def testGetBalance(self):
      balances = {'spendable' : FIRST_WLT_BALANCE, \
                  'spend' : FIRST_WLT_BALANCE, \
                  'unconf' : 0, \
                  'unconfirmed' :  0, \
                  'total' : FIRST_WLT_BALANCE, \
                  'ultimate'  :  FIRST_WLT_BALANCE, \
                  'unspent' :  FIRST_WLT_BALANCE, \
                  'full' :  FIRST_WLT_BALANCE}
      for balanceType in balances.keys():
         result = self.jsonServer.jsonrpc_getbalance(balanceType)
         self.assertEqual(result,
                          AmountToJSON(self.wlt.getBalance(balanceType)))


if __name__ == "__main__":
   #import sys;sys.argv = ['', 'Test.testName']
   unittest.main()